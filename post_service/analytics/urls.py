from django.urls import path

from post_service.analytics.api.views import LikesByUserAnalyticApiView, LastUserActionAnalyticApiView

app_name = "analytics"

urlpatterns = [
    path("likes/", view=LikesByUserAnalyticApiView.as_view(), name="likes_analytics"),
    path("users/<uuid:user_id>/last_activity/", view=LastUserActionAnalyticApiView.as_view(), name="last_user_activity"),

]
