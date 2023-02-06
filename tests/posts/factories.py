from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from post_service.posts.models import Post, PostLike
from tests.users.factories import UserFactory


class PostFactory(DjangoModelFactory):
    actor = SubFactory(UserFactory)
    edited = False
    text = Faker("text")

    class Meta:
        model = Post


class PostLikeFactory(DjangoModelFactory):
    actor = SubFactory(UserFactory)
    post = SubFactory(PostFactory)

    class Meta:
        model = PostLike
