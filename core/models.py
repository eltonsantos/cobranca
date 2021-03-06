# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from django.contrib.localflavor.br.forms import BRCNPJField
from django.core.urlresolvers import reverse

class Pessoa(models.Model):
	FORNECEDOR   = "Fornecedor"
	CLIENTE      = "Cliente"
	TERCEIRIZADO = "Terceirizado"
	FUNCIONARIO  = "Funcionário"

	PFISICA   = "Fisica"
	PJURIDICA = "Juridica"

	TYPE_CAD     =  (
					 (FORNECEDOR, "Fornecedor"),
					 (CLIENTE, "Cliente"),
					 (TERCEIRIZADO, "Terceirizado"),
					 (FUNCIONARIO, "Funcionário"),							
					)
	
	TYPE_PES = (
				(PFISICA, "Física"),
				(PJURIDICA, "Jurídica"),
			   )

	tipo_cadastro = models.CharField(choices=TYPE_CAD, verbose_name=u"Tipo de Cadastro", max_length=15)
	tipo_pessoa   = models.CharField(choices=TYPE_PES, verbose_name=u"Tipo de Pessoa", max_length=25)
	nome          = models.CharField(verbose_name=u"Nome", max_length=200)
	telefone      = models.CharField(verbose_name=u"Telefone", max_length=15)
	celular       = models.CharField(verbose_name=u"Celular", max_length=15)
	email         = models.EmailField(verbose_name=u"Email")
	ativo         = models.BooleanField(verbose_name=u"Ativo?", blank=False)
	cpf         = models.CharField(verbose_name=u"CPF", max_length=15)
	rg          = models.CharField(verbose_name=u"RG", max_length=15)
	dt_nasc     = models.DateField(verbose_name=u"Data de nascimento", auto_now_add=True)
	nome_pai    = models.CharField(verbose_name=u"Nome do pai", max_length=200)
	nome_mae    = models.CharField(verbose_name=u"Nome da mãe", max_length=200)
	resp_financ = models.CharField(verbose_name=u"Responsável Financeiro", max_length=200)
	matricula   = models.IntegerField(verbose_name=u"Matrícula", max_length=30)
	salario     = models.CharField(verbose_name=u"Salário", max_length=100)
	comissao    = models.CharField(verbose_name=u"Comissão", max_length=100)
	contratado  = models.BooleanField(verbose_name=u"Contratado?",blank=False)
	nome_fantasia   = models.CharField(verbose_name=u"Nome Fantasia", max_length=200)
	#cnpj            = models.CharField(verbose_name=u"CNPJ", max_length=200)
	cnpj             = BRCNPJField(label='CNPJ', required=False)
	insc_estadual   = models.IntegerField(verbose_name=u"Insc. Estadual", max_length=15)
	contato         = models.CharField(verbose_name=u"Contato", max_length=30)
	telefone_Contato = models.CharField(verbose_name=u"Telefones de Contato", max_length=200)
	fax              = models.CharField(verbose_name=u"Fax", max_length=15)
	nome_logradouro  = models.CharField(verbose_name=u"Nome do Logradouro", max_length=200)
	#tipo_logradouro  = models.CharField(verbose_name=u"Tipo do Logradouro", max_length=50)
	numero     = models.IntegerField(verbose_name=u"Número", max_length=10)
	bairro     = models.CharField(verbose_name=u"Bairro", max_length=50)
	cep        = models.CharField(verbose_name=u"CEP", max_length=10)	
	cidade     = models.CharField(verbose_name=u"Cidade", max_length=80)
	estado     = models.CharField(choices=STATE_CHOICES, verbose_name=u"Estado", max_length=2)

	@models.permalink
	def get_absolute_url(self):
		return ("visualizar-detalhes", (), {'pessoa_id' : self.id})

	def __unicode__(self):
		return self.nome
