from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnalyticsConfig(AppConfig):
    name = "post_service.analytics"
    verbose_name = _("Analytics")
