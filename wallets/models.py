from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Wallet(models.Model):
    title = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    date_created = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title