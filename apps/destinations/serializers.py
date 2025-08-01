from rest_framework import serializers
from apps.destinations.models import Destination


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
    activities = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    travel_guide = serializers.CharField(required=False,allow_null=True,allow_blank=True)

    class Meta:
        model = Destination
        fields = "__all__"

    def validate(self,attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        # request         = self.context.get('request',None)
        # user_instance   = get_token_user_or_none(request)

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

        # instance.created_by = user_instance

        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        # request                 = self.context.get('request',None)
        # user_instance           = get_token_user_or_none(request)

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

        # instance.modified_by    = user_instance

        instance.save()
        return instance
        

class ListAndDeleteDestinationsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = Destination
        fields = "__all__"
