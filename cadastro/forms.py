# -*- coding: utf-8 -*-
from django import forms
from models import Pessoa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroUsuarioForm(UserCreationForm):

	MASTER = "mtr"
	ADMINISTRADOR = "adm"
	USUARIO = "usr"
	TYPE_USER = (
				(MASTER, "Master"),
				(ADMINISTRADOR, "Administrador"),
				(USUARIO, "Usuário"),
				)

	tipo_usuario = forms.ChoiceField(choices=TYPE_USER, label="Tipo de usuário")

	class Meta:
		model = User
		#fields = "Tipo_de_usuario"

class CadastroPessoasForm(forms.ModelForm):
	
	class Meta:
		model = Pessoa


class PessoaFisicaForm(forms.ModelForm):
	
	class Meta:
		model = Pessoa
		fields = ("cpf", "rg")


class PessoaJuridicaForm(forms.ModelForm):
	
	class Meta:
		model = Pessoa
		fields = ("cnpj", "insc_estadual")