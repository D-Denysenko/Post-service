from django.db.models import Count

from post_service.posts.models import Post


def list_posts():
    posts = Post.objects.all().select_related("actor")
    return posts


def annotate_likes_and_unlikes_to_posts(posts):
    posts = posts.annotate(
        count_likes=Count("likes"),
        count_unlikes=Count("unlikes")
    )
    return posts

