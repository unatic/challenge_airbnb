from django.contrib import admin
from .models import Tweet, Like
# Register your models here.


class ElonFilter(admin.SimpleListFilter):

    title = "Filter by Keyword"
    parameter_name = "keyword"

    def lookups(self, request, model_admin):
        return [
            ("elon", "Tweets with Elon"),
            ("no_elon", "Tweets without Elon"),
        ]

    def queryset(self, request, tweets):
        keyword = self.value()
        if keyword:
            if keyword == 'elon':
                return tweets.filter(payload__icontains='Elon Musk')
            elif keyword == 'no_elon':
                return tweets.exclude(payload__icontains='Elon Musk')
        else:
            return tweets

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "updated_at",
        "like_count"
    )

    search_fields = (
        "payload",
        "user__username",
    )

    list_filter = (
        ElonFilter,
        "created_at",
    )

    def like_count(self, tweet):
        return tweet.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
        "updated_at",
    )

    search_fields = (
        "user__username",
    )

    list_filter = (
        "created_at",
    )

