from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/plots/", include("farms.urls")),
    path("api/auth/", include("rest_framework.urls")),
    path("api/accounts/", include("drf_registration.urls")),
]
