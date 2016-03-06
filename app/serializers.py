from app.models import user, sos
from rest_framework import serializers
from datetime import datetime

class UserSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('user_uuid',) 

class UserSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('user_uuid','first_name', 'last_name', 'dob', 'address_home', 'phone_number', 'emergency_phone', 'emergency_contact', 'secret_code' )  

class UserSerializerDetailGET(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('user_uuid', 'first_name', 'last_name', 'dob', 'address_home', 'phone_number', 'emergency_phone', 'emergency_contact', 'secret_code') 

class UserSerializerDetailPOST(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('user_uuid', 'first_name', 'last_name', 'dob', 'address_home', 'phone_number', 'emergency_phone', 'emergency_contact', 'secret_code') 

class SosSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = sos 
        fields = ('sos_uuid', 'user_uuid' , 'status')

class SosSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = sos 
        fields = ('sos_uuid', 'user_uuid')

class SosSerializerDetailGET(serializers.ModelSerializer):
    class Meta:
        model = sos 
        fields = ('sos_uuid', 'user_uuid', 'location_list', 'note_list', 'image_list', 'status')

 
class SosSerializerDetailPOST(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('location_list',)

class SosSerializerStatusGET(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('status',)

class SosSerializerStatusPOST(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('status',)
 
class SosSerializerNoteGET(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('note_list',)

class SosSerializerNotePOST(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('note_list',)
 
class SosSerializerImageGET(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('image_list',)

class SosSerializerImagePOST(serializers.ModelSerializer):

    class Meta:
        model = sos 
        fields = ('image_list',)
 
