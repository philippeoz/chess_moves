"""myprofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

import django.contrib.auth.views as auth_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from backend.core import urls as core_urls


schema_view = get_schema_view(
   openapi.Info(
      title="Chess Moves API",
      default_version='v1',
      license=openapi.License(name="MIT License"),
   ),
   public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(core_urls)),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
