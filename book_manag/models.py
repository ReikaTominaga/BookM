from accounts.models import CustomUser
from django.db import models
from django import forms

class Book(models.Model):
    """書籍"""

    #statusプルダウンの選択肢

    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社' , max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name

CHOICE = (
    ('0', '貸出可'),
    ('1', '貸出中'),
)

def book_status(forms.Form):
    select = forms.ChoiceField(widget=forms.Select, choices=CHOICE)