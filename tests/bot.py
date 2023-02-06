import pytest
from factory import Faker
from rest_framework.test import APIClient  # noqa: E402

from post_service.posts.models import Post, PostLike
from tests.users.factories import UserFactory

pytestmark = pytest.mark.django_db

NUMBER_OF_USERS = 4
MAX_POSTS_PER_USER = 5
MAX_LIKES_PER_POSTS = 3


class TestFunctionality:
    def test_whole_cycle(self):
        users = []
        for user in UserFactory.create_batch(size=NUMBER_OF_USERS):
            api_client = APIClient()
            api_client.force_authenticate(user=user)
            users.append((api_client, user))
            post_data = {
                "text": str(Faker("text"))
            }
            # create posts
            for _ in range(MAX_POSTS_PER_USER):
                api_client.post(
                    "/api/posts/",
                    data=post_data,
                    format="json",
                )
        posts = Post.objects.all()
        assert posts.count() == NUMBER_OF_USERS * MAX_POSTS_PER_USER

        for post in posts:
            for index, value in enumerate(users):
                if index < MAX_LIKES_PER_POSTS:
                    value[0].post(
                        f"/api/posts/{str(post.id)}/like/",
                        format="json",
                    )

        assert PostLike.objects.filter(post=Post.objects.all().first()).count() == MAX_LIKES_PER_POSTS
