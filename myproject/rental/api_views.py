from rest_framework import viewsets
from . import models
from . import serializers

class FriendView(viewsets.ModelViewSet):
    queryset = models.Friends.objects.all()
    serializer_class = serializers.FriendSerializer

class BelongingView(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

class BorrowedView(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer