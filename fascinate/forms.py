# -*- coding: utf-8 -*-

__author__ = 'kai.wang'

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )