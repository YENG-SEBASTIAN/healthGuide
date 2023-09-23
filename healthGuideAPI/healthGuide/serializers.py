# customuser/serializers.py
from rest_framework import serializers
from healthGuide.models import CustomUser, Patient

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'fullName', 'doctorOrNurseID', 'role', 'department', 'email', 'contact', 'address') 



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'