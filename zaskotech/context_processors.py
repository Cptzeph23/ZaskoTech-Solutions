from django.conf import settings


def site_meta(request):
    """Expose the configured public origin to canonical and social metadata."""
    return {'site_url': settings.SITE_URL}
