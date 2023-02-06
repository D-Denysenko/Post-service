from django.utils.timezone import now

from post_service.users.models import User


class SetLastRequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if bool(request.user and request.user.is_authenticated):
            # Update last request time after request finished processing.
            User.objects.filter(pk=request.user.pk).update(last_request=now())
        return response
