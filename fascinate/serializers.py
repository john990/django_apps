from fascinate.models import Img, Vote

__author__ = 'kai.wang'


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ImgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Img
        fields = ('width', 'height', 'name', 'path', 'intro', 'crate_at', 'create_ip')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('img_id', 'up', 'down')