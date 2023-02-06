from django.db import models

from post_service.utils.base_models import BaseUUIDModel


class Post(BaseUUIDModel):
    actor = models.ForeignKey(
        "users.User",
        related_name="posts",
        on_delete=models.CASCADE,
    )
    edited = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)


class Comment(BaseUUIDModel):
    actor = models.ForeignKey(
        "users.User",
        related_name="comments",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "posts.Post",
        related_name="comments",
        on_delete=models.CASCADE,
    )


class PostLike(BaseUUIDModel):
    actor = models.ForeignKey(
        "users.User",
        related_name="likes",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "posts.Post",
        related_name="likes",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("actor", "post")


class PostUnlike(BaseUUIDModel):
    actor = models.ForeignKey(
        "users.User",
        related_name="unlikes",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "posts.Post",
        related_name="unlikes",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("actor", "post")
