from django.db import models

class Enquete(models.Model):
	perguntas = models.CharField(max_length=200)
	data_publicacao = models.DateTimeField("Data de Publicação")

class Escolha(models.Model):
	enquete = models.ForeignKey(Enquete)
	escolha = models.CharField(max_length=200)
	votos = models.IntegerField()
		