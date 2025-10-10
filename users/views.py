#from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweets.serializers import TweetSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import User

class Tweets(APIView):
    def get(self, request, user_pk):
        try:
            user_tweets = User.objects.get(pk=user_pk).tweets.all()
            serializer = TweetSerializer(user_tweets, many=True)
            return Response(serializer.data)

        except User.DoesNotExist:
            raise NotFound




