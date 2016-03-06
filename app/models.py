from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid

# Create your models here.
class user(models.Model):
    user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.BigIntegerField()
    address_home = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=200)
    secret_code = models.CharField(max_length=200)
    #created = models.DateTimeField(null=True,blank=True)
    #updated = models.DateTimeField(auto_now=True)



class sos(models.Model):
    sos_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_uuid = models.ForeignKey(user,related_name="user", null=True)
    location_list = models.TextField(null=True,blank=True)
    note_list = models.TextField(null=True,blank=True)
    image_list = models.TextField(null=True,blank=True)
    #created = models.DateTimeField(null=True,blank=True)
    status = models.IntegerField(default=1)


