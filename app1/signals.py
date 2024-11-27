from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Campaign
from .tasks import call_campaign_numbers

@receiver(post_save, sender=Campaign)
def trigger_campaign_calls(sender, instance, created, **kwargs):
    if created:
        call_campaign_numbers.delay(instance.id)
