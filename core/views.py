# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from models import Pessoa
from forms import CadastroUsuarioForm, CadastroPessoasForm, PessoaFisicaForm, PessoaJuridicaForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
@login_required
def cadusuarios(request):
	if request.method == "POST":
		form = CadastroUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/principal/")
		else:
			return render(request, "cadastro-usuarios.html", {"form" : form})

	return render(request, 'cadastro-usuarios.html', {"form" : CadastroUsuarioForm()})	


@login_required
def cadpessoas(request):
	template_name = "core/cadastro-pessoas.html"
	context = {}
	if request.method == "POST":
		form = CadastroPessoasForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/principal/")
	else:
		form = CadastroPessoasForm()
	context['form'] = form
	return render(request, template_name, context)


@login_required
def visualizar(request):
	template_name = "core/visualizar-cadastrados.html"
	context = {}
	pessoa = Pessoa.objects.all()
	context['pessoa'] = pessoa
	return render(request, template_name, context)


# Função que visualiza detalhes dos cadastros
@login_required
def detalhes(request, pessoa_id):
    cadastro = get_object_or_404(Pessoa, pk=pessoa_id)
    template_name = 'core/visualizar-detalhes.html'
    context = {
        'cadastro': cadastro,
    }
    return render(request, template_name, context)


# Funçao usada pra emitir boleto
def emissao(request):
	return render(request, 'emissao.html')