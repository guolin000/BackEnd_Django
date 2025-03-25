from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PredictionResult
import time


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')

            # 模拟后端处理延迟
            time.sleep(2)

            # 示例数据
            example_result = {
                'entities': [
                    {'text': '张三', 'type': 'PERSON', 'start': 0, 'end': 2},
                    {'text': '北京', 'type': 'LOCATION', 'start': 3, 'end': 5},
                    {'text': '公司', 'type': 'ORGANIZATION', 'start': 6, 'end': 8}
                ],
                'relations': [
                    {'source': '张三', 'target': '北京', 'type': '位于'},
                    {'source': '张三', 'target': '公司', 'type': '工作于'}
                ]
            }

            return JsonResponse({'code': 0, 'data': example_result, 'message': '成功'})
        except Exception as e:
            return JsonResponse({'code': 1, 'message': str(e)})
    return JsonResponse({'code': 1, 'message': '仅支持POST请求'})


@csrf_exempt
def save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            PredictionResult.objects.create(
                input_text=data.get('input_text', ''),
                result=data.get('result', {}),
                user_id=data.get('user_id', 1)  # 默认用户ID为1，实际应从认证系统获取
            )
            return JsonResponse({'code': 0, 'message': '保存成功'})
        except Exception as e:
            return JsonResponse({'code': 1, 'message': str(e)})
    return JsonResponse({'code': 1, 'message': '仅支持POST请求'})
