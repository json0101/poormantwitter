from django.conf.urls import url
from TweetApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^tweet$',views.tweetApi),
    url(r'^tweet/([0-9]+)$',views.tweetApi)
]
