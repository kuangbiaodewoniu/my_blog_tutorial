from django.db import models
from django.urls import reverse


class Article(models.Model):
    # 标题
    title = models.CharField(max_length=64)
    # 标签
    category = models.CharField(max_length=64)
    # 日期
    date_time = models.DateTimeField(auto_now_add=True)
    # 正文
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return 'http://127.0.0.1:8000%s' % path

    # def get_absolute_url(self):
    #     path = reverse('detail', kwargs={'id': self.id})
    #     return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']