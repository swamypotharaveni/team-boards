from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from team_bords.settings import AUTH_USER_MODEL

from django.db.models.signals import post_save
from django.core.mail import send_mail
from team_bords.settings import EMAIL_HOST_USER
from django.dispatch import receiver
class CustomerUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_verified=models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
class EmailVerifiecation(models.Model):
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    token=models.UUIDField(default=uuid.uuid4,unique=True)
    auto_no_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}-{self.token}"
