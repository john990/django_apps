# coding=utf-8
import json
from django.db.models import Q

from django.shortcuts import render_to_response
from django.template import RequestContext

from base import JsonResponse
from base.common_utils import get_int
from base.view_utils import is_none_to_fill, get_object_or_empty, is_none_raise_404
from fascinate.models import Img, Vote
from base import ToJson

num_per_page = 20
none_data = '["error":"No data"]'
status_normal = 0


def index(request):
    p = Img.objects.order_by('-create_at')[:2]
    is_none_raise_404(p)
    return render_to_response('fascinate/index.html', {'post': p})


def get_post(request, img_id):
    """
     获取与img_id相邻的三个img
    """
    img_id = get_int(img_id)
    request.img_id = img_id
    if img_id == 0:
        index(request)
    else:
        p = Img.objects.filter(pk=img_id).order_by('id')
        is_none_raise_404(p)
    return render_to_response('fascinate/post.html', {'post': p}, context_instance=RequestContext(request))


# API
def api_get_post(request, img_id):
    """
     get img by id
    """
    p = get_object_or_empty(Img, pk=img_id)
    p = is_none_to_fill(p, none_data)
    return JsonResponse.response(p)


def api_get_neighbour_post(request, img_id):
    """
    获取相邻的两个post（img_id+1,img_id-1）
    """
    previous_post = Img.objects.filter(id__lt=img_id, status=status_normal).order_by('-id')[:1]
    next_post = Img.objects.filter(id__gt=img_id, status=status_normal).order_by('id')[:1]

    d = '{"previous":' + ToJson.queryset_to_json(previous_post) + ', next:' + ToJson.queryset_to_json(next_post) + '}'
    return JsonResponse.response(d)


def api_get_post_vote(request, img_id):
    """
    get vote by img id
    """
    votes = Vote.objects.filter(img_id=img_id)
    votes = is_none_to_fill(votes, none_data)
    return JsonResponse.response(votes)


def api_recent(request, page_num):
    """
    获取最新上传的图片
    """
    if page_num or page_num < 0:
        page_num = 1
    images = Img.objects.order_by('-create_at').all()[(page_num - 1) * num_per_page:num_per_page]
    images = is_none_to_fill(images, none_data)
    return JsonResponse.response(images)

