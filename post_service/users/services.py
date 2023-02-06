from rest_framework.generics import get_object_or_404

from post_service.users.models import User


def get_user_by_id(user_id):
    return get_object_or_404(User, id=user_id)
