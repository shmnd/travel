from django.urls import path, re_path, include
from . import views


urlpatterns = [

    re_path(r'^Hotels/', include([
        path('create-or-update-Hotel', views.CreateOrUpdateHotel.as_view()),
        path('delete-Hotel', views.DeleteHotelApiView.as_view()),
        path('retrieve-Hotel', views.GetHotelListApiView.as_view()),

    ])),

    re_path(r'^Hotel-Images/', include([
        path('create-or-update-Hotel-images', views.CreateOrUpdateHotelmage.as_view()),
        path('delete-Hotel-images', views.DeleteHotelImageApiView.as_view()),
        path('retrieve-Hotel-images', views.GetHotelImagesListApiView.as_view()),

    ])),

    re_path(r'^Room/', include([
        path('create-or-update-room', views.CreateOrUpdateRoom.as_view()),
        path('delete-room', views.DeleteRoomApiView.as_view()),
        path('retrieve-room', views.GetRoomListApiView.as_view()),

    ])),

    re_path(r'^Room-Images/', include([
        path('create-or-update-room-image', views.CreateOrUpdateRoomImage.as_view()),
        path('delete-room-image', views.DeleteRoomImageApiView.as_view()),
        path('retrieve-room-image', views.GetRoomImagesListApiView.as_view()),

    ])),

    re_path(r'^Driver/', include([
        path('create-or-update-driver', views.CreateOrUpdateDriver.as_view()),
        path('retrive-driver', views.GetDriverListApiView.as_view()),
        path('delete-driver', views.DeleteDriverApiView.as_view()),

    ])),

    re_path(r'^Vehicle/', include([
        path('create-or-update-vehicle', views.CreateOrUpdateVehicle.as_view()),
        path('retrive-vehicle', views.GetVehicleListApiView.as_view()),
        path('delete-vehicle', views.DeleteVehicleApiView.as_view()),

    ])),

    re_path(r'^Cab-Catgory/', include([
        path('create-or-update-cab-category', views.CreateOrUpdateCabCategory.as_view()),
        path('retrive-cab-category', views.GetCabCategoryListApiView.as_view()),
        path('delete-cab-category', views.DeleteCabCategoryApiView.as_view()),

    ])),

    re_path(r'^Cabs/', include([
        path('create-or-update-cabs', views.CreateOrUpdateCab.as_view()),
        path('retrive-cab', views.GetCabListApiView.as_view()),
        path('delete-cab', views.DeleteCabApiView.as_view()),

    ])),



]