from typing import Any
from helpers.response import ResponseInfo
from apps.home.serializers import ( CreateOrUpdateHotelSerializer,
                                    # DeleteHotelSerializer,
                                    ListHotelSerializer,
                                    CreateOrUpdateDriverSerializer,
                                    CreateOrUpdateVehicleSerializer)

from rest_framework.permissions import IsAdminUser,IsAdminOrStaff
from drf_yasg.utils import swagger_auto_schema
from helpers.helper import get_object_or_none
from apps.home.models import Hotels,Driver,Vehicle
from rest_framework import generics,status
from rest_framework.response import Response
import os,sys
import logging
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
            serializer  = self.serializer_class(instance,data=request.data,context={'request':request})

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
            serializer                            = self.serializer_class(queryset,many=True,context={'request':request})
            
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
            serializer                            = self.serializer_class(queryset,many=True,context={'request':request})
            
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
            exec_type,exc_obj,exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# list driver
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
            serializer                            = self.serializer_class(queryset,many=True,context={'request':request})
            
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