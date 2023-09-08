from rest_framework import serializers
from email_app.models import Subscriber
from email_app.models import Campaign

class SubscriberSerializer(serializers.Serializer):
    name = serializers.CharField()
    email_id = serializers.EmailField()

    def create(self, validated_data):
        """
        Create and return a new Subscriber instance, given the validated data.
        """
        return Subscriber.objects.create(**validated_data)


class UnsubscriberSerializer(serializers.Serializer):
    email_id = serializers.EmailField()



# class CampaignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Campaign
#         fields = '__all__'