import os,sys
from typing import Any
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from apps.user.serializers import SuperAdminLoginSerializer
from helpers.response import ResponseInfo
# from rest_framework.permissions import AllowAny

User = get_user_model()


class SuperAdminLoginView(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(SuperAdminLoginView,self).__init__(**kwargs)

    serializer_class    = SuperAdminLoginSerializer
    # permission_classes  = (AllowAny,)

    @swagger_auto_schema(tags=['Admin'])
    def post(self, request):
        try:
            serializer = SuperAdminLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is None:
                self.response_format['status_code']   = status.HTTP_401_UNAUTHORIZED
                self.response_format['status']        = False
                self.response_format['errors']        = "Invalid credentials"
                return Response(self.response_format,status=status.HTTP_401_UNAUTHORIZED)

            if not(user.is_superuser or user.is_staff):
                self.response_format['status_code']   = status.HTTP_403_FORBIDDEN
                self.response_format['status']        = False
                self.response_format['errors']        = "You are not authorized as Super Admin or Staff"
                return Response(self.response_format,status=status.HTTP_403_FORBIDDEN)

            refresh = RefreshToken.for_user(user)

            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username":user.username,
                    "email": user.email,
                    "is_superuser": user.is_superuser,
                    "is_staff": user.is_staff,

                }
            }

            self.response_format['status_code'] = status.HTTP_200_OK
            self.response_format['status'] = True
            self.response_format['data'] = data
            return Response(self.response_format, status=status.HTTP_200_OK)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb             = sys.exc_info()
            fname                                 = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code']   = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status']        = False
            self.response_format['message']       = f'exc_type : {exc_type},fname : {fname},tb_lineno : {exc_tb.tb_lineno},error : {str(e)}'
            return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

