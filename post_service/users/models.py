from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from post_service.utils.base_models import BaseUUIDModel


class User(AbstractUser, BaseUUIDModel):
    """
    Default custom user model for Post Service.
    If adding fields that need to be filled at user signup,
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    last_request = DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
