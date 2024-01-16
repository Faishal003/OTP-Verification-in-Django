from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_verification_link_valid(self):
        expiration_time = self.created_on + timedelta(minutes=1)
        expiration_time = expiration_time.replace(tzinfo=timezone.utc)  # Make it timezone-aware
        return datetime.now(timezone.utc) <= expiration_time

    def __str__(self):
        return self.user.username