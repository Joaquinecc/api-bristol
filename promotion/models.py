from django.db import models

# Create your models here.
class Promotion(models.Model):
    cod_cliente = models.CharField( max_length=150)
    articulocodigo = models.CharField( max_length=150)
    prom_name = models.CharField( max_length=150)
    rank= models.PositiveSmallIntegerField()
    weight= models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    key_prom= models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.cod_cliente + " - "+self.articulocodigo


