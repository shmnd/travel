from rest_framework import serializers
from .models import Webinar
# from apps.home.models import Cab,Hotels
# from apps.destinations.models import Destination

from helpers.helper import get_token_user_or_none


class CreateOrUpdateWebinarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False,allow_null=True)

    class Meta:
        model = Webinar
        fields = [
            "id", "title", "description", "date", "facilities", "price", "link",
            "duration_minutes", "capacity", "recording_url", "language", "is_active",
            "razorpay_order_id", "razorpay_payment_id", "razorpay_signature", "is_paid"
        ]
        read_only_fields = ["razorpay_order_id", "razorpay_payment_id", "razorpay_signature", "is_paid"]

    def create(self, validated_data):
        request = self.context.get("request")
        user_instance = get_token_user_or_none(request)

        instance = Webinar.objects.create(
            created_by=user_instance,
            **validated_data
        )

        # NOTE: Don't initiate payment here. Just return instance
        return instance

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user_instance = get_token_user_or_none(request)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.modified_by = user_instance
        instance.save()
        return instance


# # Webinar
# class CreateOrUpdateWebinarSerializer(serializers.ModelSerializer):
#     id   = serializers.IntegerField(allow_null=True,required=False)
#     title    = serializers.CharField(allow_null=True,allow_blank=True,required=False)
#     description   = serializers.CharField(required=False,allow_null=True,allow_blank=True)
#     date   = serializers.DateTimeField(required=False,allow_null=True,allow_blank=True)
#     facilities   = serializers.CharField(required=False,allow_null=True,allow_blank=True)
#     price = serializers.DecimalField(required=False,allow_null=True,allow_blank=True)
#     link = serializers.URLField(required=False,allow_null=True,allow_blank=True)
#     duration_minutes = serializers.CharField(required=False,allow_null=True,allow_blank=True)
#     capacity = serializers.IntegerField(required=False,allow_null=True,allow_blank=True)
#     recording_url = serializers.URLField(required=False,allow_null=True,allow_blank=True)
#     language = serializers.IntegerField(required=False,allow_null=True,allow_blank=True)
#     is_active = serializers.IntegerField(required=False,allow_null=True,allow_blank=True)
#     is_active = serializers.BooleanField(default=True)

#     cab = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Cab.objects.all(),
#         required=False
#     )

#     hotel = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Hotels.objects.all(),
#         required=False
#     )

#     destination = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Destination.objects.all(),
#         required=False
#     )

#     class Meta:
#         model = Hotels
#         fields = [
#             'id', 'cab', 'hotel', 'destination', 'description',
#             'facilities', 'main_image',
#             'contact_email', 'contact_phone', 'website',
#             'is_verified', 'is_active','gallery','gallery_details'
#         ]

#     def validate(self, attrs):
#         return super().validate(attrs)

#     def create(self, validated_data):
#         request       = self.context.get('request', None)
#         user_instance = get_token_user_or_none(request)

#         gallery = validated_data.pop("gallery", [])

#         instance = Hotels()
#         instance.name           = validated_data.get("name",None)
#         instance.location       = validated_data.get("location",None)
#         instance.address        = validated_data.get("address",None)
#         instance.description    = validated_data.get("description",None)
#         instance.facilities     = validated_data.get("facilities",None)
#         instance.main_image     = validated_data.get("main_image",None)
#         instance.contact_email  = validated_data.get("contact_email",None)
#         instance.contact_phone  = validated_data.get("contact_phone",None)
#         instance.website        = validated_data.get("website",None)
#         instance.is_verified    = validated_data.get("is_verified", True)
#         instance.is_active      = validated_data.get("is_active", True)

#         instance.created_by = user_instance
#         instance.save()

#         for image in gallery:
#             image.hotel = instance
#             image.save()

#         return instance
    

#     def update(self, instance, validated_data):
#         request       = self.context.get('request', None)
#         user_instance = get_token_user_or_none(request)

#         instance.location       = validated_data.get("location", instance.location)
#         instance.address        = validated_data.get("address", instance.address)
#         instance.description    = validated_data.get("description", instance.description)
#         instance.facilities     = validated_data.get("facilities", instance.facilities)
#         instance.main_image     = validated_data.get("main_image", instance.main_image)
#         instance.contact_email  = validated_data.get("contact_email", instance.contact_email)
#         instance.contact_phone  = validated_data.get("contact_phone", instance.contact_phone)
#         instance.website        = validated_data.get("website", instance.website)
#         instance.is_verified    = validated_data.get("is_verified", instance.is_verified)
#         instance.is_active      = validated_data.get("is_active", instance.is_active)

#         instance.modified_by = user_instance
#         instance.save()

#         return instance
    
# # class DeleteHotelSerializer(serializers.ModelSerializer):
# #     id = serializers.ListField(child=serializers.IntegerField(), required=True)

# #     class Meta:
# #         model = Hotels
# #         fields = ['id']

