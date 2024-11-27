from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = "__all__"


class CampaignResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = "__all__"
