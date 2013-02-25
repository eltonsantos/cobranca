# -*- coding: utf-8 -*-
from django import forms
from models import PessoaFisica
#from models import UserProfile
from django.contrib.auth.forms import UserCreationForm

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

	#class Meta:
	#	model = User
	#	fields = "Tipo de usuário"

class CadastroPessoasForm(forms.ModelForm):
	
	class Meta:
		model = PessoaFisica