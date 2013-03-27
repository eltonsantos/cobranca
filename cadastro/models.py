# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.br.br_states import STATE_CHOICES
#from django.core.urlresolvers import reverse

class Pessoa(models.Model):

	PFISICA   = "Fisica"
	PJURIDICA = "Juridica"
	
	TYPE_PES = (
				(PFISICA, "Física"),
				(PJURIDICA, "Jurídica"),
			   )

	tipo_pessoa  = models.CharField(choices=TYPE_PES, verbose_name=u"Tipo de Pessoa", max_length=25)
	ativo        = models.BooleanField(verbose_name=u"Ativo?", default=False)
	fornecedor   = models.BooleanField(verbose_name=u"Fornecedor", default=False)
	cliente      = models.BooleanField(verbose_name=u"Cliente", default=False)
	terceirizado = models.BooleanField(verbose_name=u"Terceirizado", default=False)
	funcionario  = models.BooleanField(verbose_name=u"Funcionário", default=False)
	contratado   = models.BooleanField(verbose_name=u"Contratado?", default=False)
	nome         = models.CharField(verbose_name=u"Nome", max_length=200)
	telefone     = models.CharField(verbose_name=u"Telefone", max_length=15)
	celular      = models.CharField(verbose_name=u"Celular", max_length=15)
	fax          = models.CharField(verbose_name=u"Fax", max_length=15)
	email        = models.EmailField(verbose_name=u"Email")
	cpf         = models.CharField(verbose_name=u"CPF", max_length=15, unique=True)
	rg          = models.CharField(verbose_name=u"RG", max_length=15, unique=True)
	dt_nasc     = models.DateField(verbose_name=u"Data de nascimento", help_text="Por exemplo: 20/04/1985")
	nome_pai    = models.CharField(verbose_name=u"Nome do pai", max_length=200)
	nome_mae    = models.CharField(verbose_name=u"Nome da mãe", max_length=200)
	resp_financ = models.CharField(verbose_name=u"Responsável Financeiro", max_length=200)
	matricula   = models.CharField(verbose_name=u"Matrícula", max_length=200)
	salario     = models.DecimalField(verbose_name=u"Salário", max_digits=15, decimal_places=2)
	comissao    = models.CharField(verbose_name=u"Comissão", max_length=100)
	nome_fantasia = models.CharField(verbose_name=u"Nome Fantasia", max_length=200)
	cnpj          = models.CharField(verbose_name=u"CNPJ", max_length=200, unique=True)
	insc_estadual = models.CharField(verbose_name=u"Insc. Estadual", max_length=200)
	dt_fund     = models.DateField(verbose_name=u"Data de Fundação",help_text="Por exemplo: 20/04/1985")
	logradouro = models.CharField(verbose_name=u"Nome do Logradouro", max_length=200)
	numero     = models.CharField(verbose_name=u"Número", max_length=200)
	complemento = models.CharField(verbose_name=u"Complemento", blank=True, max_length=50)
	bairro     = models.CharField(verbose_name=u"Bairro", max_length=50)
	cep        = models.CharField(verbose_name=u"CEP", max_length=10)	
	cidade     = models.CharField(verbose_name=u"Cidade", max_length=80)
	estado     = models.CharField(choices=STATE_CHOICES, verbose_name=u"Estado", max_length=2)

	@models.permalink
	def get_absolute_url(self):
		return ("visualizar-detalhes", (), {'pessoa_id' : self.id})

	def __unicode__(self):
		return self.nome


class RelacaoCliente(models.Model):
	codigo_cliente = models.ManyToManyField(Pessoa, related_name="cc+")
	cliente_indireto = models.ManyToManyField(Pessoa, related_name="ci+")