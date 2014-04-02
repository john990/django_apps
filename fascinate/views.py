from django.core import serializers

from django.http.response import HttpResponse

from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.tests.users.serializers import UserSerializer

from base.ModelToJson import ModelToJson

from fascinate.models import Img, Vote
from fascinate.serializers import ImgSerializer


def index(request):
    return HttpResponse('index')


def post(request, img_id):
    """
     get img by id
    """
    p = Img.objects.get(pk=img_id)
    return render_to_response('fascinate/post.html', {'post': p})


@api_view(['POST'])
def api_post(request, img_id):
    """
     get img by id(ajax)
    """
    # p = Img.objects.get(pk=img_id)
    # return HttpResponse(ModelToJson.to_json(p), content_type="application/json")
    model = Img.objects.get(pk=img_id)
    serializer_class = ImgSerializer


# class GetPostById(viewsets.ModelViewSet):
#     queryset = Img.objects.get(pk=img_id)
#     serializer_class = UserSerializer

def ajax_post_vote(request, img_id):
    vote = Vote.objects.filter(img_id=img_id)
    return HttpResponse(serializers.serialize('json', vote), content_type="application/json")
