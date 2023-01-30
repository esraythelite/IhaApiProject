from rest_framework import serializers
from IhaApp.models import User, Iha

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('UserId', 'UserName', 'FirsName', 'LastName', 'Email', 'Password')


class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Iha
        fields=('IhaId', 'IhaBrand', 'IhaModel', 'IhaCategory', 'IhaWeight', 'IhaLength', 'IhaProductionDate', 'IhaPhotoFileName')