from django.db import models


class PredictionResult(models.Model):
    id = models.AutoField(primary_key=True)  # 自动生成的编号
    input_text = models.TextField()  # 输入文本
    result = models.JSONField()  # 预测结果（JSON格式）
    created_at = models.DateTimeField(auto_now_add=True)  # 生成时间
    user_id = models.IntegerField()  # 用户编号

    class Meta:
        db_table = 'prediction_results'
