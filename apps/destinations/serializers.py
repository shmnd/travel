from rest_framework import serializers
from apps.destinations.models import Destination,Activity,ActivityImage
from helpers.helper import get_token_user_or_none


class CreateOrUpdateDestinationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False,allow_null=True)
    main_destination_image = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    main_destination_city = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    main_destination_state = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    main_destination_country = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    main_destination_heading = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    main_destination_description = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    destination_highlight_description = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6,required=False,allow_null=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6,required=False,allow_null=True)
    map_link = serializers.URLField(required=False,allow_null=True,allow_blank=True)
    highlight_image = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    highlight_heading = serializers.CharField(required=False,allow_null=True,allow_blank=True) 
    highlight_description = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    best_visit_time = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    avg_cost  = serializers.DecimalField(required=False, allow_null=True, max_digits=10, decimal_places=2)
    # activities = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    travel_guide = serializers.CharField(required=False,allow_null=True,allow_blank=True)

    is_active = serializers.BooleanField(default=True)
    weather = serializers.URLField(required=False,allow_null=True,allow_blank=True)
    currency = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    travel_type = serializers.CharField(required=False,allow_null=True,allow_blank=True)

    class Meta:
        model = Destination
        fields = "__all__"

    def validate(self,attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        request         = self.context.get('request',None)
        user_instance   = get_token_user_or_none(request)

        instance = Destination()
        instance.main_destination_image = validated_data.get("main_destination_image",None)
        instance.main_destination_city = validated_data.get("main_destination_city",None)
        instance.main_destination_state = validated_data.get("main_destination_state",None)
        instance.main_destination_country = validated_data.get("main_destination_country",None)
        instance.main_destination_heading = validated_data.get("main_destination_heading",None)
        instance.main_destination_description = validated_data.get("main_destination_description",None)
        instance.destination_highlight_description = validated_data.get("destination_highlight_description",None)
        instance.latitude = validated_data.get("latitude",None)
        instance.longitude = validated_data.get("longitude",None)
        instance.map_link = validated_data.get("map_link",None)
        instance.highlight_image = validated_data.get("highlight_image",None)
        instance.highlight_heading = validated_data.get("highlight_heading",None)
        instance.highlight_description = validated_data.get("highlight_description",None)
        instance.best_visit_time = validated_data.get("best_visit_time",None)
        instance.avg_cost = validated_data.get("avg_cost",None)
        instance.activities = validated_data.get("activities",None)
        instance.travel_guide = validated_data.get("travel_guide",None)

        instance.is_active = validated_data.get("is_active",True)
        instance.weather = validated_data.get("weather",True)
        instance.currency = validated_data.get("currency",True)
        instance.travel_type = validated_data.get("travel_type",True)

        instance.created_by = user_instance

        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        request                 = self.context.get('request',None)
        user_instance           = get_token_user_or_none(request)

        instance.main_destination_image = validated_data.get("main_destination_image",instance.main_destination_image)
        instance.main_destination_city = validated_data.get("main_destination_city",instance.main_destination_city)
        instance.main_destination_state = validated_data.get("main_destination_state",instance.main_destination_state)
        instance.main_destination_country = validated_data.get("main_destination_country",instance.main_destination_country)
        instance.main_destination_heading = validated_data.get("main_destination_heading",instance.main_destination_heading)
        instance.main_destination_description = validated_data.get("main_destination_description",instance.main_destination_description)
        instance.destination_highlight_description = validated_data.get("destination_highlight_description",instance.destination_highlight_description)
        instance.latitude = validated_data.get("latitude",instance.latitude)
        instance.longitude = validated_data.get("longitude",instance.longitude)
        instance.map_link = validated_data.get("map_link",instance.map_link)
        instance.highlight_image = validated_data.get("highlight_image",instance.highlight_image)
        instance.highlight_heading = validated_data.get("highlight_heading",instance.highlight_heading)
        instance.highlight_description = validated_data.get("highlight_description",instance.highlight_description)
        instance.best_visit_time = validated_data.get("best_visit_time",instance.best_visit_time)
        instance.avg_cost = validated_data.get("avg_cost",instance.avg_cost)
        instance.activities = validated_data.get("activities",instance.activities)
        instance.travel_guide = validated_data.get("travel_guide",instance.travel_guide)

        instance.is_active = validated_data.get("is_active",instance.is_active)
        instance.weather = validated_data.get("weather",instance.weather)
        instance.currency = validated_data.get("currency",instance.currency)
        instance.travel_type = validated_data.get("travel_type",instance.travel_type)

        instance.modified_by    = user_instance

        instance.save()
        return instance
        

class ListAndDeleteDestinationsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = Destination
        fields = "__all__"




class CreateOrUpdateActivityImageSerializer(serializers.ModelSerializer):
    id   = serializers.IntegerField(allow_null=True, required=False)
    activity = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all(),
        required=True
    )
    image = serializers.FileField(allow_null=True,required=False)

    class Meta:
        model = ActivityImage
        fields = ["id","activity", "image"]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        request       = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance = ActivityImage()
        instance.activity   = validated_data.get("activity",None)
        instance.image       = validated_data.get("image",None)

        instance.created_by = user_instance
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request       = self.context.get('request', None)
        user_instance = get_token_user_or_none(request)

        instance.activity           = validated_data.get("activity", instance.activity)
        instance.image       = validated_data.get("image", instance.image)
        
        instance.modified_by = user_instance
        instance.save()
        return instance
    

class DeleteActivityImageSerializer(serializers.ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = ActivityImage
        fields = ['id']


# Activity
class CreateOrUpdateActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    image = serializers.ImageField(required=False, allow_null=True)
    duration = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    start_time = serializers.TimeField(required=False, allow_null=True)
    end_time = serializers.TimeField(required=False, allow_null=True)
    available_dates = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_bookable = serializers.BooleanField(default=True)
    max_participants = serializers.IntegerField(required=False, allow_null=True)
    min_age = serializers.IntegerField(required=False, allow_null=True)
    is_active = serializers.BooleanField(default=True)
    is_featured = serializers.BooleanField(default=False)

    # ManyToMany relation
    activity_gallery = CreateOrUpdateActivityImageSerializer(source="activity_images",many=True, required=False)

    class Meta:
        model = Activity
        fields = [
            "id", "name", "description", "price", "image", "duration",
            "start_time", "end_time", "available_dates", "is_bookable",
            "max_participants", "min_age", "is_active", "is_featured",
            "activity_gallery"#,"activity_gallery_id",
        ]

    def validate(self, attrs):
        # custom validation (optional)
        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get("request", None)
        user_instance = get_token_user_or_none(request)

        instance = Activity()
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.price = validated_data.get("price")
        instance.image = validated_data.get("image")
        instance.duration = validated_data.get("duration")
        instance.start_time = validated_data.get("start_time")
        instance.end_time = validated_data.get("end_time")
        instance.available_dates = validated_data.get("available_dates")
        instance.is_bookable = validated_data.get("is_bookable", True)
        instance.max_participants = validated_data.get("max_participants")
        instance.min_age = validated_data.get("min_age")
        instance.is_active = validated_data.get("is_active", True)
        instance.is_featured = validated_data.get("is_featured", False)

        instance.created_by = user_instance
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get("request", None)
        user_instance = get_token_user_or_none(request)


        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.image = validated_data.get("image", instance.image)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.start_time = validated_data.get("start_time", instance.start_time)
        instance.end_time = validated_data.get("end_time", instance.end_time)
        instance.available_dates = validated_data.get("available_dates", instance.available_dates)
        instance.is_bookable = validated_data.get("is_bookable", instance.is_bookable)
        instance.max_participants = validated_data.get("max_participants", instance.max_participants)
        instance.min_age = validated_data.get("min_age", instance.min_age)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.is_featured = validated_data.get("is_featured", instance.is_featured)

        instance.modified_by = user_instance  
        instance.save()
        return instance


class DeleteActivitySerializer(serializers.ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = Activity
        fields = ['id']

