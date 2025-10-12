# config/settings.py (add or confirm)
INSTALLED_APPS = [
    "rest_framework",
    "apps.capstone",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"