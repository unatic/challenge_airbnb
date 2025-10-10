#from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweets.serializers import TweetSerializer
from .models import User

@api_view(["GET"])
def tweets_by_user(request, user_pk):
    try:
        user_tweets = User.objects.get(pk=user_pk).tweets.all()
        serializer = TweetSerializer(user_tweets, many=True)
        return Response(
            {
                "ok": True,
                "tweets": serializer.data,
            }
        )
    except User.DoesNotExist:
        return Response(
            {
                "ok": False,
            }
        )



