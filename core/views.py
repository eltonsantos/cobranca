# coding: utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# importar formulário de cadastro de usuário
from django.contrib.auth.forms import UserCreationForm
# importar formulário de login de usuário
from django.contrib.auth.forms import AuthenticationForm
# função que salva o usuário na sessão
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login


# Função que direciona para a página principal
@login_required
def principal(request):
	return render(request, "principal.html")


# Função que será executada como padrão
def login(request):
	# Se o método for igual a POST
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		# se o formulário for válido
		if form.is_valid():
			login(request, form.get_user())
			redirect('principal.html')
		else:
			return render(request, "login.html", {"form" : form})

	#return render(request, "login.html", {"form" : AuthenticationForm()}) 

def logout(request):
	pass

# Função que cadastra usuários
def cadastro(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)

		# se o formulário for válido
		if form.is_valid():
			# cria um novo usuário apartir dos dados fornecidos
			form.save()
			return HttpResponseRedirect("/principal/")
		else:
			return render(request, "cadastro.html", {"form" : form})

	return render(request, 'cadastro.html', {"form" : UserCreationForm()})



# Funçao usada pra emitir boleto
def emissao(request):
	return render(request, 'emissao.html')