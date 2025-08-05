from rest_framework import serializers
from apps.home.models import Hotels,Driver,Vehicle,Cab,CabCategory,HotelImage,Room,RoomImage
from helpers.helper import get_token_user_or_none


class CreateOrUpdateHotelImageSerializer(serializers.ModelSerializer):

    id   = serializers.IntegerField(allow_null=True, required=False)

    hotel = serializers.PrimaryKeyRelatedField(
        queryset=Hotels.objects.all(),
        required=True
    )
    class Meta:
        model = HotelImage
        fields = ["id", "hotel", "image"]


    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        request       = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance = HotelImage()
        instance.hotel   = validated_data.get("hotel",None)
        instance.image       = validated_data.get("image",None)

        instance.created_by = user_instance
        instance.save()
        return instance
    

    def update(self, instance, validated_data):
        request       = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance.hotel           = validated_data.get("hotel", instance.hotel)
        instance.image       = validated_data.get("image", instance.image)
        
        instance.modified_by = user_instance
        instance.save()
        return instance

# Delete hotel image

class DeleteHotelImagesSerializer(serializers.Serializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = HotelImage
        fields = ['id']



# hotel
class CreateOrUpdateHotelSerializer(serializers.ModelSerializer):
    id   = serializers.IntegerField(allow_null=True,required=False)
    name    = serializers.CharField(allow_null=True,allow_blank=True,required=False)
    location = serializers.URLField(required=True)
    address   = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    description   = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    facilities   = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    main_image = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    contact_email = serializers.CharField(required=True,allow_null=True,allow_blank=True)
    contact_phone = serializers.IntegerField(required=True)
    website = serializers.URLField(required=True,allow_null=True,allow_blank=True)
    is_verified = serializers.BooleanField(default=True)
    is_active = serializers.BooleanField(default=True)

    gallery = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=HotelImage.objects.all(),
        required=False
    )

    gallery_details = CreateOrUpdateHotelImageSerializer(source="hotel_images", many=True, read_only=True)


    class Meta:
        model = Hotels
        fields = [
            'id', 'name', 'location', 'address', 'description',
            'facilities', 'main_image',
            'contact_email', 'contact_phone', 'website',
            'is_verified', 'is_active','gallery','gallery_details'
        ]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        request       = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        gallery = validated_data.pop("gallery", [])

        instance = Hotels()
        instance.name           = validated_data.get("name",None)
        instance.location       = validated_data.get("location",None)
        instance.address        = validated_data.get("address",None)
        instance.description    = validated_data.get("description",None)
        instance.facilities     = validated_data.get("facilities",None)
        instance.main_image     = validated_data.get("main_image",None)
        instance.contact_email  = validated_data.get("contact_email",None)
        instance.contact_phone  = validated_data.get("contact_phone",None)
        instance.website        = validated_data.get("website",None)
        instance.is_verified    = validated_data.get("is_verified", True)
        instance.is_active      = validated_data.get("is_active", True)

        instance.created_by = user_instance
        instance.save()

        for image in gallery:
            image.hotel = instance
            image.save()

        return instance
    

    def update(self, instance, validated_data):
        request       = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        gallery = validated_data.pop("gallery", None)

        instance.name           = validated_data.get("name", instance.name)
        instance.location       = validated_data.get("location", instance.location)
        instance.address        = validated_data.get("address", instance.address)
        instance.description    = validated_data.get("description", instance.description)
        instance.facilities     = validated_data.get("facilities", instance.facilities)
        instance.main_image     = validated_data.get("main_image", instance.main_image)
        instance.contact_email  = validated_data.get("contact_email", instance.contact_email)
        instance.contact_phone  = validated_data.get("contact_phone", instance.contact_phone)
        instance.website        = validated_data.get("website", instance.website)
        instance.is_verified    = validated_data.get("is_verified", instance.is_verified)
        instance.is_active      = validated_data.get("is_active", instance.is_active)

        instance.modified_by = user_instance
        instance.save()

        if gallery is not None:
            # detach old images not in the new list
            HotelImage.objects.filter(hotel=instance).exclude(id__in=[img.id for img in gallery]).update(hotel=None)
            for image in gallery:
                image.hotel = instance
                image.save()

        return instance
    
# class DeleteHotelSerializer(serializers.ModelSerializer):
#     id = serializers.ListField(child=serializers.IntegerField(), required=True)

#     class Meta:
#         model = Hotels
#         fields = ['id']

class ListHotelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    hotel_images = CreateOrUpdateHotelImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotels
        fields = "__all__"



# Room
class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ["id", "image"]

class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotels.objects.all())
    hotel_name = serializers.CharField(source="hotel.name", read_only=True)
    gallery = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=RoomImage.objects.all(),
        required=False
    )
    gallery_details = RoomImageSerializer(source="gallery", many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            "id","hotel", "hotel_name","room_type", "name","description",
            "price", "availability", "max_occupancy","facilities","image",
            "gallery",          # for input (IDs of RoomImage)
            "gallery_details",  # for output (nested details)
            "is_active",
        ]



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
    


class DeleteVehicleSerializer(serializers.ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = Vehicle
        fields = ['id']


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
    

class DeleteDriverSerializer(serializers.ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = Driver
        fields = ['id']



# cab category 

class CreateOrUpdateCabCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = CabCategory
        fields = ["id", "name", "description", "is_active"]

    def validate(self, attrs):
        # Add extra validation if needed
        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance = CabCategory()
        instance.name               = validated_data.get("name", None)
        instance.description       = validated_data.get("description", None)
        instance.is_active              = validated_data.get("is_active", None)

        instance.created_by = user_instance
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance.name               = validated_data.get("name", instance.name)
        instance.description       = validated_data.get("description", instance.description)
        instance.is_active              = validated_data.get("is_active", instance.is_active)

        instance.modified_by = user_instance
        instance.save()
        return instance


class DeleteCabCategorySerializer(serializers.ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = CabCategory
        fields = ['id']


# cabs 
class CreateOrUpdateCabSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True, required=False)

    category_id = serializers.PrimaryKeyRelatedField(queryset=CabCategory.objects.all(),source="category")
    category = CreateOrUpdateCabCategorySerializer(read_only=True) 
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all())

    class Meta:
        model = Cab
        fields = [
            "id","category_id","category","vehicle","driver",
            "is_available","price_per_km", "base_fare","description",
            "total_trips","is_verified","is_active",
        ]

    def validate(self, attrs):
        # Example: ensure price_per_km is positive
        if attrs.get("price_per_km", 0) < 0:
            raise serializers.ValidationError({"price_per_km": "Price per km must be positive"})
        # Vehicle validation
        vehicle = attrs.get("vehicle")
        if not vehicle:
            raise serializers.ValidationError({"vehicle": "Vehicle is required."})
        if Cab.objects.filter(vehicle=vehicle).exists() and not self.instance:
            raise serializers.ValidationError({"vehicle": "This vehicle is already assigned to another cab."})

        # Driver validation
        driver = attrs.get("driver")
        if not driver:
            raise serializers.ValidationError({"driver": "Driver is required."})
        if Cab.objects.filter(driver=driver).exists() and not self.instance:
            raise serializers.ValidationError({"driver": "This driver is already assigned to another cab."})

        return attrs

    def create(self, validated_data):
        request = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance = Cab()
        instance.category        = validated_data.get("category")
        instance.vehicle         = validated_data.get("vehicle")
        instance.driver          = validated_data.get("driver")
        instance.is_available    = validated_data.get("is_available", True)
        instance.price_per_km    = validated_data.get("price_per_km", 0.0)
        instance.base_fare       = validated_data.get("base_fare", 0.0)
        instance.description     = validated_data.get("description", "")
        instance.total_trips     = validated_data.get("total_trips", 0)
        instance.is_verified     = validated_data.get("is_verified", False)
        instance.is_active       = validated_data.get("is_active", True)

        instance.created_by = user_instance
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance.category        = validated_data.get("category", instance.category)
        instance.vehicle         = validated_data.get("vehicle", instance.vehicle)
        instance.driver          = validated_data.get("driver", instance.driver)
        instance.is_available    = validated_data.get("is_available", instance.is_available)
        instance.price_per_km    = validated_data.get("price_per_km", instance.price_per_km)
        instance.base_fare       = validated_data.get("base_fare", instance.base_fare)
        instance.description     = validated_data.get("description", instance.description)
        instance.total_trips     = validated_data.get("total_trips", instance.total_trips)
        instance.is_verified     = validated_data.get("is_verified", instance.is_verified)
        instance.is_active       = validated_data.get("is_active", instance.is_active)

        instance.modified_by = user_instance
        instance.save()
        return instance
    

class DeleteCabSerializer(serializers.ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = Cab
        fields = ['id']

