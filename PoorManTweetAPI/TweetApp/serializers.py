from rest_framework import serializers
from TweetApp.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tweet 
        fields=('TweetId','Name','Content','DateInsert')

