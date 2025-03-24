# book/views.py
import chardet
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'dynasty']
    search_fields = ['title', 'author', 'dynasty']

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if 'id' in data:
            del data['id']

        # 检测 content_file 的编码
        if 'content_file' in request.FILES:
            content_file = request.FILES['content_file']
            raw_data = content_file.read()  # 读取文件内容
            result = chardet.detect(raw_data)
            data['content_encoding'] = result['encoding'] or 'utf-8'
            content_file.seek(0)  # 重置文件指针，以便后续保存

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()

        # 如果更新了 content_file，检测新文件的编码
        if 'content_file' in request.FILES:
            content_file = request.FILES['content_file']
            raw_data = content_file.read()
            result = chardet.detect(raw_data)
            data['content_encoding'] = result['encoding'] or 'utf-8'
            content_file.seek(0)  # 重置文件指针

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        if instance.content_file:
            with instance.content_file.open('rb') as f:
                raw_data = f.read()
                encoding = instance.content_encoding or chardet.detect(raw_data)['encoding'] or 'utf-8'
                # 尝试多种编码解码
                fallback_encodings = [encoding, 'utf-8', 'gbk', 'gb2312', 'big5']
                content = None
                for enc in fallback_encodings:
                    try:
                        content = raw_data.decode(enc)
                        break  # 成功解码后退出循环
                    except UnicodeDecodeError:
                        continue
                if content is None:
                    # 如果所有编码都失败，返回错误提示或原始字节数据
                    content = "无法解码文件内容，请检查文件编码"
                data['content'] = content
        return Response(data)
