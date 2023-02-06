from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from post_service.posts.api.serializers import CreatePostInputSerializer, CreatePostOutputSerializer, \
    ListPostsOutputSerializer, RetrievePostOutputSerializer
from post_service.posts.selectors import list_posts
from post_service.posts.services import create_post, like_post, delete_like, unlike_post, delete_unlike
from post_service.utils.api_utils import get_request_data


class CreateListPostApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        input_data = get_request_data(CreatePostInputSerializer, request)
        post = create_post(actor=request.user, **input_data)
        data = CreatePostOutputSerializer(post, many=False).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def get(self, requests, *args, **kwargs):
        posts = list_posts()
        data = ListPostsOutputSerializer(posts, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class LikePostApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, post_id, *args, **kwargs):
        post = like_post(actor=request.user, post_id=post_id)
        data = RetrievePostOutputSerializer(post, many=False).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, requests, post_id, *args, **kwargs):
        delete_like(actor=requests.user, post_id=post_id)
        return Response(status=status.HTTP_200_OK)


class UnlikePostApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, post_id, *args, **kwargs):
        post = unlike_post(actor=request.user, post_id=post_id)
        data = RetrievePostOutputSerializer(post, many=False).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, requests, post_id, *args, **kwargs):
        delete_unlike(actor=requests.user, post_id=post_id)
        return Response(status=status.HTTP_200_OK)
