from rest_framework import generics
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializer

import datetime

class PostListApi(generics.ListAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializer.LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializer.LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializer.LinkSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializer.LinkSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializer.LinkSerializer


class ActiveLinkView(APIView):
    '''
    Returns a list of all active (publicly accessible) links
    '''
    def get(self, request):
        '''
        Invoked whenever a HTTP GET Request is made to this view
        '''
        qs = models.Link.public.all()
        data = serializer.LinkSerializer(qs, many=True).data
        return Response(data, status.HTTP_200_OK)


class RecentLinkView(APIView):
    '''
    Returns a list of recently created active links
    '''
    def get(self, request):
        '''
        Invoked whenever a HTTP GET Request is made to this view 
        '''
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializer.LinkSerializer(qs, many=True).data
        return Response(data, status.HTTP_200_OK)
