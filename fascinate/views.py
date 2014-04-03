# coding=utf-8

from django.http.response import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from base import JsonResponse
from base.Utils import get_object_or_empty

from fascinate.models import Img, Vote


num_per_page = 20


def index(request):
    return HttpResponse('index')


def post(request, img_id):
    """
     get img by id
    """
    p = get_object_or_404(Img, pk=img_id)
    return render_to_response('fascinate/post.html', {'post': p})


# API
def api_get_post(request, img_id):
    """
     get img by id
    """
    p = get_object_or_empty(Img, pk=img_id)
    if p is None:
        p = '["aa":"aa"]'
    return JsonResponse.response(p)


def api_get_post_vote(request, img_id):
    """
    get vote by img id
    """
    votes = Vote.objects.filter(img_id=img_id)
    return JsonResponse.response(votes)


def api_recent(request, page_num):
    """
    获取最新上传的图片
    """
    if page_num or page_num < 0:
        page_num = 1
    imgs = Img.objects.order_by('-create_at').all()[(page_num - 1) * num_per_page:num_per_page]
    return JsonResponse.response(imgs)

