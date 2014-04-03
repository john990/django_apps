# coding=utf-8
from django.shortcuts import _get_queryset

__author__ = 'kai.wang'


def get_object_or_empty(cls, *args, **kwargs):
    queryset = _get_queryset(cls)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        pass


def is_none(data, none):
    """
    判断对象是不是None,如果是None，赋值为none
    """
    if data:
        return data
    else:
        return none