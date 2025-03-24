from django.http import JsonResponse
from neo4j import GraphDatabase
from BackEnd_Django.settings import NEO4J_CONFIG

# Neo4j 连接
driver = GraphDatabase.driver(NEO4J_CONFIG['uri'], auth=NEO4J_CONFIG['auth'])


def run_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        return [record.data() for record in result]


# 知识图谱概览
def overview(request):
    total_nodes = run_query("MATCH (n) RETURN count(n) as count")[0]["count"]
    total_rels = run_query("MATCH ()-[r]->() RETURN count(r) as count")[0]["count"]
    node_types = run_query("CALL db.labels() YIELD label RETURN count(label) as count")[0]["count"]
    rel_types = \
        run_query("CALL db.relationshipTypes() YIELD relationshipType RETURN count(relationshipType) as count")[0][
            "count"]
    return JsonResponse({
        "total_nodes": total_nodes,
        "total_rels": total_rels,
        "node_types": node_types,
        "rel_types": rel_types
    })


# 查询接口
def search(request):
    keyword = request.GET.get('q', '')  # 获取查询参数 q
    # 查询匹配节点及其第一层邻居
    print(f"Received keyword: '{keyword}'")  # 调试输出，确保接收到关键词
    cypher = """
    MATCH (n)
    WHERE toLower(n.name) CONTAINS toLower($keyword)
    OPTIONAL MATCH (n)-[r]->(m)
    RETURN elementId(n) as id, n.name as name, labels(n) as labels,
           collect({target_id: elementId(m), target_name: m.name, target_labels: labels(m), rel_type: type(r)}) as neighbors
    LIMIT 50
    """
    nodes = run_query(cypher, {"keyword": keyword})

    # 处理节点数据，包括第一层邻居
    node_data = []
    seen_ids = set()  # 用于去重
    links = []

    for n in nodes:
        # 添加主节点
        node_id = n["id"]
        if node_id not in seen_ids:
            node_data.append({
                "id": node_id,
                "name": n["name"],
                "type": n["labels"][0]
            })
            seen_ids.add(node_id)

        # 处理邻居节点和关系
        for neighbor in n["neighbors"]:
            if neighbor["target_id"]:  # 确保邻居存在
                target_id = neighbor["target_id"]
                if target_id not in seen_ids:
                    node_data.append({
                        "id": target_id,
                        "name": neighbor["target_name"],
                        "type": neighbor["target_labels"][0]
                    })
                    seen_ids.add(target_id)
                # 添加关系
                links.append({
                    "source": node_id,
                    "target": target_id,
                    "value": neighbor["rel_type"]
                })

    return JsonResponse({
        "nodes": node_data,
        "links": links
    })
