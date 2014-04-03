# coding=utf-8
from django.core import serializers

from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http.response import HttpResponse

from base import ModelToJson


__author__ = 'kai.wang'


def response(data):
    """
    把Model、QuerySet、String转换为json，并返回HttpResponse
    """
    if data:
        if isinstance(data, Model):
            return HttpResponse(ModelToJson.to_json(data), content_type="application/json")
        elif isinstance(data, QuerySet):
            return HttpResponse(serializers.serialize('json', data), content_type="application/json")
        else:
            # raise Exception('data is not Model or QuerySet')
            return HttpResponse(data, content_type="application/json")
    else:
        raise Exception('data is empty')