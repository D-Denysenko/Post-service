from django.urls import path

from post_service.posts.api.views import CreateListPostApiView, LikePostApiView, UnlikePostApiView

app_name = "posts"


urlpatterns = [
    path("", view=CreateListPostApiView.as_view(), name="create_list_posts"),
    path("<uuid:post_id>/like/", view=LikePostApiView.as_view(), name="like_post"),
    path("<uuid:post_id>/unlike/", view=UnlikePostApiView.as_view(), name="unlike_post"),
]
