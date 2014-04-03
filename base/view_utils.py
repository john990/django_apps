# coding=utf-8
from django.http import Http404
from django.shortcuts import _get_queryset

__author__ = 'kai.wang'


def get_object_or_empty(cls, *args, **kwargs):
    queryset = _get_queryset(cls)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        pass


def is_none_to_fill(data, none):
    """
    判断对象是不是None,如果是None，赋值为none
    """
    if data:
        return data
    else:
        return none


def is_none_raise_404(data):
    """
    判断对象是不是None,如果是None抛出404异常
    """
    if data is None or not data:
        raise Http404('No matches the given query.')

