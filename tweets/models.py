from django.db import models
from django.conf import settings
from common.models import CommonModel

class Tweet(CommonModel):

    """Tweet Model Definition"""

    payload = models.CharField(
        max_length=180,
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.payload

class Like(CommonModel):

    """Like Model Definition"""

    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user.username} Likes {self.tweet.payload}"