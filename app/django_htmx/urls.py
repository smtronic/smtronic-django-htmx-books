from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("", include("books.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
