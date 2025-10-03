from django.contrib import admin
from .models import Tweet, Like
# Register your models here.

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

