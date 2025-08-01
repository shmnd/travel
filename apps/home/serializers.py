from rest_framework import serializers
from apps.home.models import Hotels




class CreateOrUpdateHotelSerializer(serializers.ModelSerializer):
    id            = serializers.IntegerField(allow_null=True,required=False)
    hotel_name    = serializers.CharField(allow_null=True,allow_blank=True,required=False)
    hotel_place   = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    hotel_price   = serializers.CharField(required=False,allow_null=True,allow_blank=True)


    class Meta:
        model = Hotels
        fields =['id','hotel_name','hotel_place','hotel_price'] 

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        # request         = self.context.get('request',None)
        # user_instance   = get_token_user_or_none(request)

        instance            = Hotels()
        instance.hotel_name   = validated_data.get("hotel_name",None)
        instance.hotel_place     = validated_data.get('hotel_place',None)
        instance.hotel_price      = validated_data.get('hotel_price',None)
        # instance.created_by = user_instance

        instance.save()
        return instance
    

    def update(self, instance, validated_data):
        # request                 = self.context.get('request',None)
        # user_instance           = get_token_user_or_none(request)
        instance.hotel_name   = validated_data.get("hotel_name",instance.hotel_name)
        instance.hotel_place  = validated_data.get('hotel_place',instance.hotel_place)
        instance.hotel_price  = validated_data.get('hotel_price',instance.hotel_price)
        # instance.modified_by    = user_instance

        instance.save()
        return instance
    
# class DeleteHotelSerializer(serializers.ModelSerializer):
#     id = serializers.ListField(child=serializers.IntegerField(), required=True)

#     class Meta:
#         model = Hotels
#         fields = ['id']

class ListHotelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = Hotels
        fields = ['id', 'hotel_name', 'hotel_place', 'hotel_price']



