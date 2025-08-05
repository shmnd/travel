from typing import Any
import os,sys
import logging
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAdminOrStaff
from drf_yasg.utils import swagger_auto_schema
from helpers.helper import get_object_or_none
from helpers.response import ResponseInfo

from apps.home.models import Hotels,Driver,Vehicle,Cab,CabCategory,HotelImage,Room,RoomImage

from apps.home.serializers import ( CreateOrUpdateHotelSerializer,
                                    # DeleteHotelSerializer,
                                    ListHotelSerializer,
                                    CreateOrUpdateDriverSerializer,
                                    DeleteDriverSerializer,
                                    CreateOrUpdateVehicleSerializer,
                                    DeleteVehicleSerializer,
                                    CreateOrUpdateCabSerializer,
                                    CreateOrUpdateCabCategorySerializer,
                                    DeleteCabCategorySerializer,
                                    DeleteCabSerializer,
                                    CreateOrUpdateHotelImageSerializer,
                                    DeleteHotelImagesSerializer,
                                    CreateOrUpdateRoomSerializer,
                                    DeleteRoomSerializer,
                                    CreateOrUpdateRoomImageSerializer,
                                    DeleteRoomImagesSerializer
                                )

logger = logging.getLogger(__name__)

# Create your views here.
class CreateOrUpdateHotel(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateHotel,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateHotelSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Hotel'])
    def post(self,request):
        try:
            instance    = get_object_or_none(Hotels,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteHotelApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteHotelApiView,self).__init__(**kwargs)

    serializer_class = ListHotelSerializer  
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Hotel"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id')
            hotels_objects = Hotels.objects.filter(id = ids)
            hotels_objects.delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetHotelListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetHotelListApiView,self).__init__(**kwargs)

    serializer_class    = ListHotelSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Hotel'])
    def get (self,request):
        try:
            queryset = Hotels.objects.all().order_by('id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# Hotel image

class CreateOrUpdateHotelmage(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateHotelmage,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateHotelImageSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Hotel-Images'])
    def post(self,request):
        try:
            instance    = get_object_or_none(HotelImage,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteHotelImageApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteHotelImageApiView,self).__init__(**kwargs)

    serializer_class = DeleteHotelImagesSerializer  
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Hotel-Images"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id')
            HotelImage.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetHotelImagesListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetHotelImagesListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateHotelImageSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Hotel-Images'])
    def get (self,request):
        try:
            queryset = HotelImage.objects.all().order_by('id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# room image =------------------------------------------------------------------------


class CreateOrUpdateRoomImage(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateRoomImage,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateRoomImageSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Room-Images'])
    def post(self,request):
        try:
            instance    = get_object_or_none(RoomImage,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'

            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteRoomImageApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteRoomImageApiView,self).__init__(**kwargs)

    serializer_class = DeleteRoomImagesSerializer  
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Room-Images"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id')
            RoomImage.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetRoomImagesListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetRoomImagesListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateRoomImageSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Room-Images'])
    def get (self,request):
        try:
            queryset = RoomImage.objects.all().order_by('id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Room ------------------------------------------------------------------------------------------------ 

class CreateOrUpdateRoom(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateRoom,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateRoomSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Room'])
    def post(self,request):
        try:
            instance    = get_object_or_none(Room,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class GetRoomListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetRoomListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateRoomSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Room'])
    def get (self,request):
        try:
            queryset = Room.objects.all().order_by('-id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



# delete cab category
class DeleteRoomApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteRoomApiView,self).__init__(**kwargs)

    serializer_class =   DeleteRoomSerializer
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Room"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            Room.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# Driver
 
class CreateOrUpdateDriver(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateDriver,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateDriverSerializer
    permission_classes  = (IsAdminOrStaff,)

    @swagger_auto_schema(tags=['Driver'])
    def post(self,request):
        try:
            instance    = get_object_or_none(Driver,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            print(serializer.data)
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# list driver
class GetDriverListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetDriverListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateDriverSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Driver'])
    def get (self,request):
        try:
            queryset = Driver.objects.all().order_by('id')
            serializer  = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteDriverApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteDriverApiView,self).__init__(**kwargs)

    serializer_class =   DeleteDriverSerializer
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Driver"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            Driver.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Vehicle
 
class CreateOrUpdateVehicle(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateVehicle,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateVehicleSerializer
    permission_classes  = (IsAdminOrStaff,)

    @swagger_auto_schema(tags=['Vehicle'])
    def post(self,request):
        try:
            instance    = get_object_or_none(Vehicle,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            print(serializer.data)
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            # exec_type,exc_obj,exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = e
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# list Vehicle
class GetVehicleListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetVehicleListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateVehicleSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Vehicle'])
    def get (self,request):
        try:
            queryset = Vehicle.objects.all().order_by('id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class DeleteVehicleApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteVehicleApiView,self).__init__(**kwargs)

    serializer_class =   DeleteVehicleSerializer
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Vehicle"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            Vehicle.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Cab Category

class CreateOrUpdateCabCategory(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateCabCategory,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateCabCategorySerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Cab-Category'])
    def post(self,request):
        try:
            instance    = get_object_or_none(CabCategory,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'

            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# list cab category


class GetCabCategoryListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetCabCategoryListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateCabCategorySerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Cab-Category'])
    def get (self,request):
        try:
            queryset = CabCategory.objects.all().order_by('-id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# delete cab category
class DeleteCabCategoryApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteCabCategoryApiView,self).__init__(**kwargs)

    serializer_class =   DeleteCabCategorySerializer
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Cab-Category"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            CabCategory.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Cab

class CreateOrUpdateCab(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateCab,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateCabSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Cabs'])
    def post(self,request):
        try:
            instance    = get_object_or_none(Cab,pk=request.data.get('id',None))
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request}, partial=True)

            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Sucess"
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class GetCabListApiView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(GetCabListApiView,self).__init__(**kwargs)

    serializer_class    = CreateOrUpdateCabSerializer
    permission_classes  = (IsAdminUser,)

    @swagger_auto_schema(tags=['Cabs'])
    def get (self,request):
        try:
            queryset = Cab.objects.all().order_by('-id')
            serializer = self.serializer_class(queryset,many=True,context={'request':request})
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['data']          = serializer.data
            return Response(self.response_format,status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



# delete cab category
class DeleteCabApiView(generics.DestroyAPIView):
    def __init__(self, **kwargs: Any) -> None:
        self.response_format = ResponseInfo().response
        super(DeleteCabApiView,self).__init__(**kwargs)

    serializer_class =   DeleteCabSerializer
    permission_classes = [IsAdminUser,]


    @swagger_auto_schema (tags=["Cabs"],request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            Cab.objects.filter(id__in = ids).delete()
            
            self.response_format['status_code']   = status.HTTP_200_OK
            self.response_format['status']        = True
            self.response_format['message']       = "Deleted success"
            return Response(self.response_format,status=status.HTTP_200_OK)

        except Exception as e:
            exc_type,exc_obj,exc_tb               = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type:{exc_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



