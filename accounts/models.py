from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import date
import uuid
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    email = models.EmailField(_('email address'), unique=True,default=uuid.uuid1)
    fullname = models.CharField(null=True,max_length=40)
    dob = models.DateField(default=date.today)
    phonenumber = models.CharField(max_length=10, blank=True)
    passportnumber = models.CharField(max_length=10, blank=True)