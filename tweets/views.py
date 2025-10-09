#from django.shortcuts import render
#from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer

from .models import Tweet

@api_view()
def tweets(request):
    all_tweets = Tweet.objects.all()
    serializer = TweetSerializer(all_tweets, many=True)
    return Response(
        {
            "ok": True,
            "tweets": serializer.data,
        }
    )
'''
def see_all_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "all_tweets.html",
        {            
            "title": "See All Tweets",
            "tweets": tweets,
        },
    )

def see_one_tweet(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        return render(
            request,
            "tweet_detail.html",
            {
                "tweet": tweet,
            },
        )
    except Tweet.DoesNotExist:
        return render(
            request,
            "tweet_detail.html",
            {
                "not_found": True,
            },
        )
'''