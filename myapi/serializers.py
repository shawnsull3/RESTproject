from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'fullName', 'email', 'age')