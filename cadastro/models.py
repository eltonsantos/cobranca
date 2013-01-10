from django.db import models

class Cliente(models.Model):
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=200)

class ClienteDoCliente(models.Model):
	cliente = models.ForeignKey(Cliente)
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=200)