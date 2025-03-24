import chardet
from django.db import models
import os


def book_cover_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"cover_{instance.id}_{instance.title}.{ext}"
    return os.path.join('book_txt', new_name)


def book_content_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"content_{instance.id}_{instance.title}.{ext}"
    return os.path.join('book_txt', new_name)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="书名")
    author = models.CharField(max_length=100, verbose_name="作者")
    dynasty = models.CharField(max_length=50, verbose_name="朝代")
    cover = models.ImageField(upload_to=book_cover_upload_to, null=True, blank=True, verbose_name="封面")
    content_file = models.FileField(upload_to=book_content_upload_to, null=True, blank=True, verbose_name="内容文件")
    content_encoding = models.CharField(max_length=50, null=True, blank=True, verbose_name="内容文件编码")  # 新增字段

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = "书籍"
        db_table = "sys_book"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
