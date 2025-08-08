"""
URL configuration for hotel_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import RedirectView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


schema_view             = get_schema_view(
        openapi.Info(
        title             = "glideGo API",
        default_version   = 'v1',
        description       = "system that helps manage various aspects of a hotels's operations",
        terms_of_service  = "",
        contact           = openapi.Contact(email="shamnad.p@happyclicks.in"),
    ),
    public               = True,
    permission_classes   = [permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect root URL to the Swagger docs
    path('', RedirectView.as_view(url='api/docs/')),
    

    # API base URLs
    path('api/', include([
        path('user/',include('apps.user.urls')),
        path('home/', include('apps.home.urls')),
        path('destination/',include('apps.destinations.urls')),
        path('cabs/',include('apps.cabs.urls')),
        path('webinar/',include('apps.webinar.urls')),



    ])),

    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += staticfiles_urlpatterns()   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)