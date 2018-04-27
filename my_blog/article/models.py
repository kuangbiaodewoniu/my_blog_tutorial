from django.db import models

class Article(models.Model):
    # 标题
    title = models.CharField(max_length=64)
    # 标签
    category = models.CharField(max_length=64)
    # 日期
    date_time = models.DateTimeField(auto_now_add=True)
    # 正文
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']