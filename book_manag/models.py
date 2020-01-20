from accounts.models import CustomUser
from django.db import models

class Book(models.Model):
    """書籍"""

    #statusプルダウンの選択肢

    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社' , max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name