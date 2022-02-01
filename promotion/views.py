from django.shortcuts import render
from rest_framework import viewsets, permissions

from promotion import serializer
from . import models
class PromtionView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Promotion.objects.all()
    serializer_class = serializer.PromotionSerializer
    # permission_classes = [permissions.IsAuthenticated]

