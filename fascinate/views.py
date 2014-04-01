from django.http.response import HttpResponse
from django.shortcuts import render_to_response

from fascinate.models import Img


def index(request):
    return HttpResponse('index')


def post(request, img_id):
    """
     get img by id
    """
    p = Img.objects.get(pk=img_id)
    return render_to_response('fascinate/post.html', {'post': p})