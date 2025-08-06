from django.urls import path, re_path, include
from . import views


urlpatterns = [

    re_path(r'^Destinations/', include([
        path('create-or-update-Destination', views.CreateOrUpdateDestination.as_view()),
        path('delete-Destination', views.DeletDestination.as_view()),
        path('retrieve-Destination', views.GetDestinationList.as_view()),

     ])),

    re_path(r'^Activity-Image/', include([
        path('create-or-update-activity-image', views.CreateOrUpdateActivityImage.as_view()),
        path('delete-activity-image', views.DeleteActivityImage.as_view()),
        path('retrieve-activity-image', views.GetActivityImageList.as_view()),

     ])),

    re_path(r'^Activity/', include([
        path('create-or-update-activity', views.CreateOrUpdateActivity.as_view()),
        path('delete-activity', views.DeleteActivity.as_view()),
        path('retrieve-activity', views.GetActivityList.as_view()),

     ])),

]