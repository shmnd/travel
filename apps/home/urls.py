from django.urls import path, re_path, include
from . import views


urlpatterns = [

    re_path(r'^Hotels/', include([
        path('create-or-update-Hotel', views.CreateOrUpdateHotel.as_view()),
        path('delete-Hotel', views.DeleteHotelApiView.as_view()),
        path('retrieve-Hotel', views.GetHotelListApiView.as_view()),

    ])),

    re_path(r'^Driver/', include([
        path('create-or-update-driver', views.CreateOrUpdateDriver.as_view()),
        path('retrive-driver', views.GetDriverListApiView.as_view()),


    ])),



]