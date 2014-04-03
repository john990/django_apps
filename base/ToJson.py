# coding=utf-8
from datetime import datetime, date
from django.core import serializers

__author__ = 'kai.wang'


def model_to_json(model):
    """
    将model转换为json
    """
    keys = []
    for field in model._meta.fields:
        keys.append(field.name)

    d = {}
    for key in keys:
        value = getattr(model, key)
        if isinstance(value, datetime):
            print value
            value = value.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(value, date):
            print value
            value = value.strftime('%Y-%m-%d')
        d[key] = value
    import json

    return json.dumps(d)


def queryset_to_json(queryset):
    j = '['
    for model in queryset:
        j += model_to_json(model) + ','
    if j != '[':
        j = j[:-1] + ']'
    else:
        j += ']'
    return j

# def queryset_array_to_json(*queryset_array):
#     j = '['
#     for queryset in queryset_array:
#         if queryset:
#             j += '['
#             for model in queryset:
#                 j += model_to_json(model) + ','
#             j = j[:-1] + ']'
#
#
#     j = j[:-1] + ']'
#     return j