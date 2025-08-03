from rest_framework import serializers
from apps.home.models import Hotels,Driver,Vehicle
from helpers.helper import get_token_user_or_none



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
        request         = self.context.get('request',None)
        user_instance   = get_token_user_or_none(request)

        instance            = Hotels()
        instance.hotel_name   = validated_data.get("hotel_name",None)
        instance.hotel_place     = validated_data.get('hotel_place',None)
        instance.hotel_price      = validated_data.get('hotel_price',None)
        instance.created_by = user_instance

        instance.save()
        return instance
    

    def update(self, instance, validated_data):
        request                 = self.context.get('request',None)
        user_instance           = get_token_user_or_none(request)
        instance.hotel_name   = validated_data.get("hotel_name",instance.hotel_name)
        instance.hotel_place  = validated_data.get('hotel_place',instance.hotel_place)
        instance.hotel_price  = validated_data.get('hotel_price',instance.hotel_price)
        instance.modified_by    = user_instance

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





# vehicle

class CreateOrUpdateVehicleSerializer(serializers.ModelSerializer):
    id                  = serializers.IntegerField(allow_null=True, required=False)
    brand               = serializers.CharField(required=True)
    model               = serializers.CharField(required=True)
    registration_number = serializers.CharField(required=True)
    seating_capacity    = serializers.IntegerField(required=True)
    vehicle_type        = serializers.CharField(required=True)
    color               = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    year                = serializers.IntegerField(required=False, allow_null=True)
    insurance_number    = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    insurance_expiry    = serializers.DateField(required=False, allow_null=True)
    vehicle_image       = serializers.FileField(required=False, allow_null=True)
    rc_document         = serializers.FileField(required=False, allow_null=True)
    is_verified         = serializers.BooleanField(default=False)
    is_active           = serializers.BooleanField(default=True)
    fuel                = serializers.ChoiceField(choices=Vehicle.FuelType.choices, required=False, allow_null=True)
    features            = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    # Foreign key (writable)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(),
        required=False,
        allow_null=True
    )

    # Extra read-only fields
    owner_name = serializers.SerializerMethodField()
    is_company_owned = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = [
            "id", "brand", "model", "registration_number", "seating_capacity",
            "vehicle_type", "color", "year", "insurance_number", "insurance_expiry",
            "vehicle_image", "rc_document", "is_verified", "is_active",
            "fuel", "features", "owner", "owner_name", "is_company_owned",
        ]

    def get_owner_name(self, obj):
        """Return the driver's name if assigned, else 'Company Owned'."""
        return obj.owner.name if obj.owner else "Company Owned"

    def get_is_company_owned(self, obj):
        """Return True if no driver is linked."""
        return obj.owner is None

    def create(self, validated_data):
        request = self.context.get("request", None)
        user_instance = get_token_user_or_none(request)

        instance = Vehicle()
        instance.brand = validated_data.get("brand",None)
        instance.model = validated_data.get("model",None)
        instance.registration_number = validated_data.get("registration_number",None)
        instance.seating_capacity = validated_data.get("seating_capacity",None)
        instance.vehicle_type = validated_data.get("vehicle_type",None)
        instance.color = validated_data.get("color",None)
        instance.year = validated_data.get("year",None)
        instance.insurance_number = validated_data.get("insurance_number",None)
        instance.insurance_expiry = validated_data.get("insurance_expiry",None)
        instance.vehicle_image = validated_data.get("vehicle_image",None)
        instance.rc_document = validated_data.get("rc_document",None)
        instance.is_verified = validated_data.get("is_verified", False)
        instance.is_active = validated_data.get("is_active", True)
        instance.fuel = validated_data.get("fuel",None)
        instance.features = validated_data.get("features",None)
        instance.owner = validated_data.get("owner",None)

        instance.created_by = user_instance
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get("request", None)
        user_instance = get_token_user_or_none(request)

        instance.brand = validated_data.get("brand", instance.brand)
        instance.model = validated_data.get("model", instance.model)
        instance.registration_number = validated_data.get("registration_number", instance.registration_number)
        instance.seating_capacity = validated_data.get("seating_capacity", instance.seating_capacity)
        instance.vehicle_type = validated_data.get("vehicle_type", instance.vehicle_type)
        instance.color = validated_data.get("color", instance.color)
        instance.year = validated_data.get("year", instance.year)
        instance.insurance_number = validated_data.get("insurance_number", instance.insurance_number)
        instance.insurance_expiry = validated_data.get("insurance_expiry", instance.insurance_expiry)
        instance.vehicle_image = validated_data.get("vehicle_image", instance.vehicle_image)
        instance.rc_document = validated_data.get("rc_document", instance.rc_document)
        instance.is_verified = validated_data.get("is_verified", instance.is_verified)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.fuel = validated_data.get("fuel", instance.fuel)
        instance.features = validated_data.get("features", instance.features)
        instance.owner = validated_data.get("owner", instance.owner)

        instance.modified_by = user_instance
        instance.save()
        return instance
    





# Drive

class CreateOrUpdateDriverSerializer(serializers.ModelSerializer):
    id              = serializers.IntegerField(allow_null=True, required=False)
    name            = serializers.CharField(allow_null=True, allow_blank=True, required=True)
    phone_number    = serializers.CharField(required=True, allow_null=True, allow_blank=True)
    email           = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
    license_number  = serializers.CharField(required=True, allow_null=True, allow_blank=True)
    license_expiry  = serializers.DateField(required=True, allow_null=True)
    address         = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    profile_image   = serializers.FileField(required=False)
    aadhar_number   = serializers.CharField(required=True, allow_null=True, allow_blank=True)
    aadhar_document = serializers.FileField(required=True)
    police_verification = serializers.FileField(required=True)
    is_verified     = serializers.BooleanField(default=False)
    is_active       = serializers.BooleanField(default=False)
    total_rides     = serializers.IntegerField(default=0)

    vehicles = CreateOrUpdateVehicleSerializer(source="owned_vehicles", many=True, read_only=True)

    class Meta:
        model = Driver
        # fields = "__all__"

        fields = [
            'id', 'name', 'phone_number', 'email', 'license_number',
            'license_expiry', 'address', 'profile_image', 'aadhar_number',
            'aadhar_document', 'police_verification', 'is_verified',
            'is_active', 'total_rides','vehicles',
        ]


        
    def validate(self, attrs):
        # Add extra validation if needed
        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance = Driver()
        instance.name               = validated_data.get("name", None)
        instance.phone_number       = validated_data.get("phone_number", None)
        instance.email              = validated_data.get("email", None)
        instance.license_number     = validated_data.get("license_number", None)
        instance.license_expiry     = validated_data.get("license_expiry", None)
        instance.address            = validated_data.get("address", None)
        instance.profile_image      = validated_data.get("profile_image", None)
        instance.aadhar_number      = validated_data.get("aadhar_number", None)
        instance.aadhar_document    = validated_data.get("aadhar_document", None)
        instance.police_verification= validated_data.get("police_verification", None)
        instance.is_verified        = validated_data.get("is_verified", False)
        instance.is_active          = validated_data.get("is_active", True)
        instance.total_rides        = validated_data.get("total_rides", 0)

        instance.created_by = user_instance
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance.name               = validated_data.get("name", instance.name)
        instance.phone_number       = validated_data.get("phone_number", instance.phone_number)
        instance.email              = validated_data.get("email", instance.email)
        instance.license_number     = validated_data.get("license_number", instance.license_number)
        instance.license_expiry     = validated_data.get("license_expiry", instance.license_expiry)
        instance.address            = validated_data.get("address", instance.address)
        instance.profile_image      = validated_data.get("profile_image", instance.profile_image)
        instance.aadhar_number      = validated_data.get("aadhar_number", instance.aadhar_number)
        instance.aadhar_document    = validated_data.get("aadhar_document", instance.aadhar_document)
        instance.police_verification= validated_data.get("police_verification", instance.police_verification)
        instance.is_verified        = validated_data.get("is_verified", instance.is_verified)
        instance.is_active          = validated_data.get("is_active", instance.is_active)
        instance.total_rides        = validated_data.get("total_rides", instance.total_rides)

        instance.modified_by = user_instance
        instance.save()
        return instance