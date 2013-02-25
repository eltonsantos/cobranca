# -*- coding: utf-8 -*-
from django.db import models
#from django.forms.widgets import RadioSelect
from django.contrib.auth.models import User
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from django.core.urlresolvers import reverse

# Classe que adiciona um novo usuário ao sistema
#class UserProfile(models.Model):
	# acrescentei esse campo
	#user = models.ForeignKey(User, unique=True)

#	MASTER = "mtr"
#	ADMINISTRADOR = "adm"
#	USUARIO = "usr"

#	TYPE_USER = (
#				(MASTER, "Master"),
#				(ADMINISTRADOR, "Administrador"),
#				(USUARIO, "Usuário"),
#				)

#	tipo_usuario = models.CharField(choices=TYPE_USER, verbose_name="Tipo de usuário", max_length=10)
	
# Classe Pessoa
class Pessoa(models.Model):
	FORNECEDOR   = "forn"
	CLIENTE      = "clie"
	TERCEIRIZADO = "terc"
	FUNCIONARIO  = "func"

	PFISICA   = "pf"
	PJURIDICA = "pj"

	TYPE_CAD     =  (
					 (FORNECEDOR, "Fornecedor"),
					 (CLIENTE, "Cliente"),
					 (TERCEIRIZADO, "Terceirizado"),
					 (FUNCIONARIO, "Funcionário"),							
					)
	
	TYPE_PES = (
				(PFISICA, "Pessoa Física"),
				(PJURIDICA, "Pessoa Jurídica"),
			   )
	
	tipo_pessoa   = models.CharField(choices=TYPE_PES, verbose_name=u"Tipo de Pessoa", max_length=2) 
	tipo_cadastro = models.CharField(choices=TYPE_CAD, verbose_name=u"Tipo de Cadastro", max_length=4)
	#cod_cliente   = models.CharField(verbose_name=u"Código do cliente", max_length=100)
	nome          = models.CharField(verbose_name=u"Nome", max_length=200)
	#endereco      = models.ForeignKey("Endereco", verbose_name=u"Endereço", blank=True)
	telefone      = models.CharField(verbose_name=u"Telefone", max_length=15)
	celular       = models.CharField(verbose_name=u"Celular", max_length=15)
	email         = models.EmailField(verbose_name=u"Email")
	ativo         = models.BooleanField(verbose_name=u"Ativo?", blank=True)

	class Meta:
		abstract = True

# Classe Pesssoa Fisica herdando da Classe Pessoa
class PessoaFisica(Pessoa):
	cpf         = models.CharField(verbose_name=u"CPF", max_length=15)
	rg          = models.CharField(verbose_name=u"RG", max_length=15)
	dt_nasc     = models.DateField(verbose_name=u"Data de nascimento", auto_now_add=True)
	nome_pai    = models.CharField(verbose_name=u"Nome do pai", max_length=200)
	nome_mae    = models.CharField(verbose_name=u"Nome da mãe", max_length=200)
	resp_financ = models.CharField(verbose_name=u"Responsável Financeiro", max_length=200)	
	matricula   = models.IntegerField(verbose_name=u"Matrícula", max_length=30)
	#cargo        = Tipo Cargo
	salario     = models.CharField(verbose_name=u"Salário", max_length=100)
	comissao    = models.CharField(verbose_name=u"Comissão", max_length=100)
	#departamento = Tipo Departamento
	contratado  = models.CharField(verbose_name=u"Contratado", max_length=100)

	@models.permalink
	def get_absolute_url(self):
		return ('visualizar-detalhes', (), {'pk': self.pk})

	def __unicode__(self):
		return self.nome

# Classe Pessoa Juridica herdando da Classe Pessoa
class PessoaJuridica(Pessoa):
	nome_fantasia   = models.CharField(verbose_name=u"Nome Fantasia", max_length=200)
	cnpj            = models.CharField(verbose_name=u"CNPJ", max_length=200)
	insc_estadual   = models.IntegerField(verbose_name=u"Insc. Estadual", max_length=15)
	contato         = models.CharField(verbose_name=u"Contato", max_length=30)
	telefoneContato = models.CharField(verbose_name=u"Telefones de Contato", max_length=200)
	fax             = models.CharField(verbose_name=u"Fax", max_length=15)
	#contrato        = Tipo Contrato
	#socios          = Tipo Socios
	#contas          = Tipo Conta
	produto         = models.CharField(verbose_name=u"Produto", max_length=200)
	servico         = models.CharField(verbose_name=u"Serviço", max_length=200)

#class Bairro(Endereco):
#	bairro = models.CharField(verbose_name=u"Bairro", max_length=200)

#class Cidade(Endereco):
#	cidade = models.CharField(verbose_name=u"Cidade", max_length=200)
#	num_ibge = models.IntegerField(verbose_name=u"Número do IBGE", max_length=200)

#class Pais(Endereco):
#	pais = models.CharField(verbose_name=u"País", max_length=200)
#	cod_pais = models.IntegerField(verbose_name=u"Código do país", max_length=200)

# Classe Endereco
class Endereco(models.Model):
	logradouro = models.CharField(verbose_name=u"Nome do Logradouro", max_length=200)
	tipo       = models.CharField(verbose_name=u"Tipo do Logradouro", max_length=50)
#	bairro     = models.ForeignKey(Bairro, verbose_name=u"Bairro")
	numero     = models.IntegerField(verbose_name=u"Número", max_length=10)
#	cidade     = models.ForeignKey(Cidade, verbose_name=u"Cidade")
	estado     = models.CharField(choices=STATE_CHOICES, verbose_name=u"Estado", max_length=2)
#	pais       = models.ForeignKey(Pais, verbose_name=u"País")
	cep        = models.CharField(verbose_name=u"CEP", max_length=200)

class RelacaoClientes(models.Model):
	pk_pjuridica = models.ForeignKey(PessoaJuridica, verbose_name=u"Pessoa Jurídica")
	pk_pfisica   = models.ForeignKey(PessoaFisica, verbose_name=u"Pessoa Física")
