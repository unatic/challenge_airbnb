from django.db import models
from django.conf import settings
from common.models import CommonModel

class Tweet(CommonModel):

    """Tweet Model Definition"""

    payload = models.CharField(
        max_length=180,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return str(self.user) + " Likes " + str(self.tweet)