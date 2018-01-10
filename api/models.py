from django.db import models
from rest_framework.fields import IntegerField

allowed_methods = 'GET','POST'
class Subscription(models.Model):
    id = IntegerField(label='ID', read_only=True)
    name = models.CharField('nome',max_length=100)
    cpf = models.CharField('CPF',max_length=11)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone',max_length=20)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)