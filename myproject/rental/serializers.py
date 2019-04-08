from rest_framework import serializers
from . import models

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friends
        fields = '__all__'

class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Belonging
        fields = '__all__'

class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Borrowed
        fields = '__all__'

