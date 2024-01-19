from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    def get_recommended_profiles(self):
        pass

    def get_first_name(self):
        return self.user.first_name

    def get_last_name(self):
        return self.user.last_name

    def get_username(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)
