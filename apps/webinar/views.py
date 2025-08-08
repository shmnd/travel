import razorpay
from django.conf import settings
from typing import Any
import os,sys
import logging
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminOrStaff
from drf_yasg.utils import swagger_auto_schema
from helpers.helper import get_object_or_none
from helpers.response import ResponseInfo
from .serializers import CreateOrUpdateWebinarSerializer
from .models import Webinar

import razorpay
from django.conf import settings

razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

class CreateOrUpdateWebinar(generics.GenericAPIView):
    def __init__(self, **kwargs: Any):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateWebinar, self).__init__(**kwargs)

    serializer_class = CreateOrUpdateWebinarSerializer
    permission_classes = (IsAdminOrStaff,)  # adjust as per your requirement

    @swagger_auto_schema(tags=['Webinar'])
    def post(self, request):
        try:
            instance = get_object_or_none(Webinar, pk=request.data.get('id', None))
            serializer = self.serializer_class(
                instance,
                data=request.data,
                context={'request': request},
                partial=True
            )

            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format['status'] = False
                self.response_format['errors'] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)

            webinar = serializer.save()

            # Initiate Razorpay order

            if not webinar.price or webinar.price <= 0:
                raise ValueError("Webinar price must be greater than zero to create payment order.")

            # Create Razorpay order
            order_data = {
                "amount": int(webinar.price * 100),  # in paise
                "currency": "INR",
                "receipt": f"webinar_{webinar.id}",
                "payment_capture": 1  # Auto capture after payment
            }
            order = razorpay_client.order.create(order_data)

            # Save order ID in webinar for future payment verification
            webinar.razorpay_order_id = order["id"]
            webinar.save(update_fields=["razorpay_order_id"])

            self.response_format['status_code'] = status.HTTP_200_OK
            self.response_format['status'] = True
            self.response_format['message'] = "Webinar created and payment order initiated"
            self.response_format['data'] = {
                "webinar": self.serializer_class(webinar).data,
                "razorpay_order": order
            }
            return Response(self.response_format, status=status.HTTP_201_CREATED)

        except Exception as e:
            exec_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.response_format['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status'] = False
            self.response_format['message'] = f"exc_type : {exec_type},fname:{fname},tb_lineno:{exc_tb.tb_lineno},error:{str(e)}"
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
