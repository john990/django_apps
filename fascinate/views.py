from django.core import serializers

from django.http.response import HttpResponse
from django.shortcuts import render_to_response

from base.ModelToJson import ModelToJson

from fascinate.models import Img, Vote


def index(request):
    return HttpResponse('index')


def post(request, img_id):
    """
     get img by id
    """
    p = Img.objects.get(pk=img_id)
    return render_to_response('fascinate/post.html', {'post': p})


# API
def api_get_post(request, img_id):
    """
     get img by id(ajax)
    """
    p = Img.objects.get(pk=img_id)
    return HttpResponse(ModelToJson.to_json(p), content_type="application/json")


def api_get_post_vote(request, img_id):
    """
    get vote by img id
    """
    votes = Vote.objects.filter(img_id=img_id)
    return HttpResponse(serializers.serialize('json', votes), content_type="application/json")


