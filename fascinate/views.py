from django.http.response import HttpResponse
from django.shortcuts import render_to_response

from base.ModelToJson import ModelToJson
from fascinate.models import Img


def index(request):
    return HttpResponse('index')


def post(request, img_id):
    """
     get img by id
    """
    p = Img.objects.get(pk=img_id)
    return render_to_response('fascinate/post.html', {'post': p})


def ajax_post(request, img_id):
    """
     get img by id(ajax)
    """
    p = Img.objects.get(pk=img_id)
    return HttpResponse(ModelToJson.to_json(p), content_type="application/json")