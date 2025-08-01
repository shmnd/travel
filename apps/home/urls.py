from django.urls import path, re_path, include
from . import views


urlpatterns = [

    re_path(r'^Hotels/', include([
        path('create-or-update-Hotel', views.CreateOrUpdateHotel.as_view()),
        path('delete-Hotel', views.DeleteHotelApiView.as_view()),
        path('retrieve-Hotel', views.GetHotelListApiView.as_view()),

     ])),

]