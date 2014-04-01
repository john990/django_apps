# coding=utf-8
from django.db import models


class Img(models.Model):
    """ 图片信息 """

    width = models.IntegerField(max_length=5, default=0)
    height = models.IntegerField(max_length=5, default=0)
    name = models.CharField(max_length=100, default='')
    path = models.CharField(max_length=300, default='')
    intro = models.TextField(default='')
    crate_at = models.DateTimeField(auto_now_add=True)
    create_ip = models.CharField(max_length=20, default='')


class Vote(models.Model):
    """ 投票 """
    img = models.ForeignKey(Img)
    up = models.IntegerField(max_length=11, default=0)
    down = models.IntegerField(max_length=11, default=0)