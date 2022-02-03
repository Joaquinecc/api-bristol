from rest_framework import serializers
from . import models
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promotion
        fields = ['prom_name','cod_cliente', 'articulocodigo', 'rank', 'weight',"key_prom"]
