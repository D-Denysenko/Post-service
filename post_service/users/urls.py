from django.urls import path

from post_service.users.api.views import (
    user_create_view,
)

app_name = "users"
urlpatterns = [
    path("", view=user_create_view, name="create"),

]
