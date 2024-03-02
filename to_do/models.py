from django.db import models


# Create your models here.
# class herdando de models.Model
class to_do(models.Model):
    titulo = models.CharField(
        max_length=100, null=False, blank=False
    )  # Max_length=qts caracteres no maximo, null= n pode ter valores nulos, blank= nao pode ter somente espacos em branco
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateTimeField(null=False, blank=False)
    data_finalizacao = models.DateTimeField(null=True)
