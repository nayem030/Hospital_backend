from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PatientSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model= models.Patient
        fields ='__all__'
        

class RegistrationSerializers(serializers.ModelSerializer):
    
    
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email', 'password']
        
        def save(self):
            username = self.validated_data['username']
            email = self.validated_data['email']
            password = self.validated_data['password']
            
            
            
            
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'error' : "Email Already Exists"})
            
            account=User(username=username, email=email)
            account.set_password(password)
            account.is_active=False
            account.save()
            print(account)
            return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
                
        