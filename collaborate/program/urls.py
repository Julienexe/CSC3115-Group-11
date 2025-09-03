# apps/capstone/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, ProjectViewSet, OutcomeViewSet

router = DefaultRouter()
router.register(r"programs", ProgramViewSet, basename="program")
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"outcomes", OutcomeViewSet, basename="outcome")

urlpatterns = [
    path("api/", include(router.urls)),
]

# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.capstone.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
