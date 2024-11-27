from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    CAMPAIGN_TYPES = [
        ("Inbound", "Inbound"),
        ("Outbound", "Outbound"),
    ]
    CAMPAIGN_STATUSES = [
        ("Running", "Running"),
        ("Paused", "Paused"),
        ("Completed", "Completed"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAMPAIGN_TYPES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=CAMPAIGN_STATUSES, default="Running")
    agents = models.ManyToManyField(Agent, related_name="campaigns")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CampaignResult(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="results")
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField()
    recording = models.FileField(blank=True, null=True)
    summary = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.name
