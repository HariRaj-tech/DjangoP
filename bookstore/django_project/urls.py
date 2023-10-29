# django_projects/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Django Admin
    path("anything-but-admin/", admin.site.urls),
    # User management
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("pages.urls")),
    # path("accounts/", include("accounts.urls")),
    path("books/", include("books.urls")),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

if settings.DEBUG:  # new
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
