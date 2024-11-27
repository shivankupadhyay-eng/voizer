from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1.views import AgentViewSet, CampaignViewSet, CampaignResultViewSet

router = DefaultRouter()

router.register('agents', AgentViewSet, basename='agent'),
router.register('campaigns', CampaignViewSet, basename='campaign'),
router.register('campaign-results', CampaignResultViewSet, basename='campaignresult')

urlpatterns = [
    path('api/', include(router.urls)),
]
