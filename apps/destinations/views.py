import os,sys
import logging
from typing import Any
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics,status
from rest_framework.response import Response
from helpers.response import ResponseInfo
from helpers.helper import get_object_or_none
from apps.destinations.models import Destination,ActivityImage,Activity
from apps.destinations.serializers import(CreateOrUpdateDestinationSerializer,
                                          DeleteDestiantionSerializer,
                                          CreateOrUpdateActivityImageSerializer,
                                          DeleteActivityImageSerializer,
                                          CreateOrUpdateActivitySerializer,
                                          DeleteActivitySerializer,
                                          )

# Create your views here.

class CreateOrUpdateDestination(generics.GenericAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateDestination,self).__init__(**kwargs)

    serializer_class = CreateOrUpdateDestinationSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(tags=['Destination'])

    def post(self,request):
        try:
            instance = get_object_or_none(Destination,pk=request.data.get('id',None))
            serializer = self.serializer_class(instance,data=request.data,context={'request':request})
            
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        
        
class DeletDestination(generics.DestroyAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(DeletDestination,self).__init__(**kwargs)

    serializer_class = DeleteDestiantionSerializer
    permission_classes = [IsAdminUser,]

    @swagger_auto_schema(tags=['Destination'],request_body=serializer_class)

    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            Destination.objects.filter(id__in=ids).delete()

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


class GetDestinationList(generics.GenericAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(GetDestinationList,self).__init__(**kwargs)

    serializer_class = CreateOrUpdateDestinationSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(tags=['Destination'])
    def get(self,request):
        try:
            queryset = Destination.objects.all().order_by('id')
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

# Activity Image

class CreateOrUpdateActivityImage(generics.GenericAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateActivityImage,self).__init__(**kwargs)

    serializer_class = CreateOrUpdateActivityImageSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(tags=['Activity-Image'])

    def post(self,request):
        try:
            instance = get_object_or_none(ActivityImage,pk=request.data.get('id',None))
            serializer = self.serializer_class(instance,data=request.data,context={'request':request})
            
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        
        
class DeleteActivityImage(generics.DestroyAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(DeleteActivityImage,self).__init__(**kwargs)

    serializer_class = DeleteActivityImageSerializer
    permission_classes = [IsAdminUser,]

    @swagger_auto_schema(tags=['Activity-Image'],request_body=serializer_class)

    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id')
            ActivityImage.objects.filter(id__in=ids).delete()

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


class GetActivityImageList(generics.GenericAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(GetActivityImageList,self).__init__(**kwargs)

    serializer_class = CreateOrUpdateActivityImageSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(tags=['Activity-Image'])
    def get(self,request):
        try:
            queryset = ActivityImage.objects.all().order_by('-id')
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

# Activity


class CreateOrUpdateActivity(generics.GenericAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateActivity,self).__init__(**kwargs)

    serializer_class = CreateOrUpdateActivitySerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(tags=['Activity'])

    def post(self,request):
        try:
            instance = get_object_or_none(Activity,pk=request.data.get('id',None))
            serializer = self.serializer_class(instance,data=request.data,context={'request':request})
            
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        
        
class DeleteActivity(generics.DestroyAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(DeleteActivity,self).__init__(**kwargs)

    serializer_class = DeleteActivitySerializer
    permission_classes = [IsAdminUser,]

    @swagger_auto_schema(tags=['Activity'],request_body=serializer_class)

    def delete(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['error']         = serializer.errors
                return Response(self.response_format,status=status.HTTP_400_BAD_REQUEST)
            
            ids = serializer.validated_data.get('id',[])
            Activity.objects.filter(id__in=ids).delete()

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


class GetActivityList(generics.GenericAPIView):
    def __init__(self, **kwargs:Any):
        self.response_format = ResponseInfo().response
        super(GetActivityList,self).__init__(**kwargs)

    serializer_class = CreateOrUpdateActivitySerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(tags=['Activity'])
    def get(self,request):
        try:
            queryset = Activity.objects.all().order_by('-id')
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

