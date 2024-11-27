from celery import shared_task
from .models import Campaign, CampaignResult

@shared_task
def call_campaign_numbers(campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
        
        for phone_number in campaign.phone_number.split(","):
            CampaignResult.objects.create(
                name=f"Result for {phone_number}",
                campaign=campaign,
                type="Automated Call",
                phone=phone_number,
                cost=2.5,
                outcome="Success",
                call_duration=30.0, 
                recording="/audio.mp3", 
                summary="Call completed successfully.",
                transcription="Hello, this is an automated call."
            )
        return f"Processed campaign {campaign_id} successfully."
    except Campaign.DoesNotExist:
        print(f"Campaign with id {campaign_id} does not exist.")
        return f"Campaign with id {campaign_id} does not exist."
