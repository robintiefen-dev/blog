from datetime import date
from django.conf import settings
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    @property
    def age(self):
        if not self.date_of_birth:
            return None

        today = date.today()

        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
