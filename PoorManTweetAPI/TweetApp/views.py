# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TweetApp.models import Tweet
from TweetApp.serializers import TweetSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def tweetApi(request,id=0):
    if request.method=='GET':
        tweets = Tweet.objects.all()
        tweets_serializer=TweetSerializer(tweets,many=True)
        return JsonResponse(tweets_serializer.data,safe=False)
    elif request.method=='POST':
        tweet_data=JSONParser().parse(request)
        tweets_serializer=TweetSerializer(data=tweet_data)

        if tweets_serializer.is_valid():
            tweets_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='DELETE':
        tweet=Tweet.objects.get(TweetId=id)
        tweet.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
