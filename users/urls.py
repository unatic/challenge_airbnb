from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_pk>/tweets", views.tweets_by_user),
]