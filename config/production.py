
import os

from .settings import *


# Production must never use Django's debug mode.
DEBUG = False

# Keep production secrets outside source control.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]


# Render provides this hostname automatically.
render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if render_hostname:
    ALLOWED_HOSTS = [render_hostname]
    CSRF_TRUSTED_ORIGINS = [f"https://{render_hostname}"]
else:
    ALLOWED_HOSTS = [
        host.strip()
        for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
        if host.strip()
    ]
    CSRF_TRUSTED_ORIGINS = [
        origin.strip()
        for origin in os.environ.get(
            "DJANGO_CSRF_TRUSTED_ORIGINS", ""
        ).split(",")
        if origin.strip()
    ]


# Serve static files through WhiteNoise, directly after SecurityMiddleware.
MIDDLEWARE = [
    MIDDLEWARE[0],
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE[1:],
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# HTTPS settings for a service behind Render's proxy.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"
