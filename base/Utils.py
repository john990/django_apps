from django.shortcuts import _get_queryset

__author__ = 'kai.wang'


def get_object_or_empty(cls, *args, **kwargs):
    queryset = _get_queryset(cls)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        pass