from django.db import transaction

from post_service.posts.models import Post, PostLike, PostUnlike
from post_service.posts.selectors import annotate_likes_and_unlikes_to_posts


def create_post(actor, **input_data):
    post = Post.objects.create(actor=actor, **input_data)
    return post


def like_post(actor, post_id):
    with transaction.atomic():
        post = Post.objects.filter(id=post_id)
        if post.exists():
            like, created = PostLike.objects.get_or_create(actor=actor, post_id=post_id)
            if created:
                delete_unlike(actor=actor, post_id=post_id)

    post = annotate_likes_and_unlikes_to_posts(post).first()

    return post


def delete_like(actor, post_id):
    like = PostLike.objects.filter(actor=actor, post_id=post_id)
    if not like.exists():
        return
    like.delete()


def unlike_post(actor, post_id):
    with transaction.atomic():
        post = Post.objects.filter(id=post_id)
        if not post.exists():
            # ToDo exception
            return
        unlike, created = PostUnlike.objects.get_or_create(actor=actor, post_id=post_id)
        if created:
            delete_like(actor=actor, post_id=post_id)
    post = annotate_likes_and_unlikes_to_posts(post).first()

    return post


def delete_unlike(actor, post_id):
    unlike = PostUnlike.objects.filter(actor=actor, post_id=post_id)
    if not unlike.exists():
        return
    unlike.delete()
