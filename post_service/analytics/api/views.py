from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from post_service.analytics.api.serializers import LikeAnaliticsPerUserOutputSerializer
from post_service.analytics.services import likes_by_user_analytics
from post_service.users.api.serializers import UserLastActionSerializer
from post_service.users.services import get_user_by_id
from post_service.utils.api_utils import get_filter_params


class LikesByUserAnalyticApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        posts = likes_by_user_analytics(actor=request.user, **get_filter_params(request))
        data = LikeAnaliticsPerUserOutputSerializer(posts, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class LastUserActionAnalyticApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id, *args, **kwargs):
        user = get_user_by_id(user_id)
        data = UserLastActionSerializer(user, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

