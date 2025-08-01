from django.urls import path, re_path, include
from . import views


urlpatterns = [

    re_path(r'^Destinations/', include([
        path('create-or-update-Destination', views.CreateOrUpdateDestination.as_view()),
        path('delete-Destination', views.DeletDestination.as_view()),
        path('retrieve-Destination', views.GetDestinationList.as_view()),

     ])),

]