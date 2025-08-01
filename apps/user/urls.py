from django.urls import path, re_path, include
from apps.user.views import SuperAdminLoginView


urlpatterns = [

    re_path(r'^Admin/', include([
        path('superadmin-login', SuperAdminLoginView.as_view()),

    ])),

]
