from django.shortcuts import render
from rest_framework import viewsets, permissions, status,mixins
from rest_framework.response import Response
from promotion import serializer
from . import models
from django.db.models import Max
class PromtionView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Promotion.objects.all()
    serializer_class = serializer.PromotionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function 
        """
        is_many = isinstance(request.data, list)
        if not is_many:
            # return super(PromtionView, self).create(request, *args, **kwargs)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Must be a list"})
        else:
            key =self.get_key()
            for x in request.data:
                x["key_prom"]=key
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def get_key(self):
        try:
            return models.Promotion.objects.all().aggregate(Max('key_prom'))['key_prom__max']+1
        except:
            return 1
