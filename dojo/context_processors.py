# import the settings file
from django.conf import settings


def globalize_oauth_vars(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'GOOGLE_ENABLED': settings.GOOGLE_OAUTH_ENABLED,
            'OKTA_ENABLED': settings.OKTA_OAUTH_ENABLED,
            'AZUREAD_TENANT_OAUTH2_ENABLED': settings.AZUREAD_TENANT_OAUTH2_ENABLED}


def bind_alert_count(request):
    from dojo.models import Alerts
    if not request.user.is_authenticated:
        return {}
    return {'alert_count': Alerts.objects.filter(user_id=request.user).count()}
