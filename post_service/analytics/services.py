from django.db.models import Count
from django.db.models.functions import TruncDay

from post_service.posts.models import PostLike


def likes_by_user_analytics(actor, date_from=None, date_to=None, **filters):
    likes = PostLike.objects.filter(actor=actor)
    if date_from:
        likes = likes.filter(created_at__date__gte=date_from)
    if date_to:
        likes = likes.filter(created_at__date__lte=date_to)
    likes = likes.annotate(day=TruncDay('created_at')).values('day').annotate(
        likes_count=Count('id')).values('day', 'likes_count')

    return likes
