# coding: utf-8
from django.db import models
#from django.forms.widgets import RadioSelect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import render, redirect, get_object_or_404
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
#from models import UserProfile
from models import PessoaFisica, PessoaJuridica
from forms import CadastroUsuarioForm, CadastroPessoasForm
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
		#msg = "Usuário cadastrado com sucesso!"
		# se o formulário for válido
		if form.is_valid():
			#user = UserProfile()
			#form.cleaned_data['tipo_usuario']			
			# cria um novo usuário apartir dos dados fornecidos
			form.save()
			return HttpResponseRedirect("/principal/")
			#return render(request, "cadastro-usuarios.html", {"form" : form})
		else:
			return render(request, "cadastro-usuarios.html", {"form" : form})

	return render(request, 'cadastro-usuarios.html', {"form" : CadastroUsuarioForm()})	


# Função que cadastra pessoas
@login_required	
def cadpessoas(request):
	template_name = "core/cadastro-pessoas.html"
	context = {}
	if request.method == "POST":
		form = CadastroPessoasForm(request.POST)
		if form.is_valid():
			form.save()
			#cadp = form.save(commit=False)
			#cadp.user = request.user
			#cadp.save()
			return HttpResponseRedirect("/principal/")
	else:
		form = CadastroPessoasForm()
	context['form'] = form
	return render(request, template_name, context)

@login_required
def visualizar(request):
	template_name = "core/visualizar-cadastrados.html"
	context = {}
	cadastros = PessoaFisica.objects.all()
	#paginator = Paginator(cadastros, 10)
	#page = request.GET.get('page', 1)
	#try:
	#	page_obj = paginator.page(page)
	#except PageNotAnInteger:
	#	page_obj = paginator.page(1)
	#except EmptyPage:
	#	page_obj = paginator.page(paginator.num_pages)

	#context['page_obj'] = page_obj
	#context['paginator'] = paginator
	context['cadastros'] = cadastros
	return render(request, template_name, context)	

# Função que visualiza detalhes dos cadastros
@login_required
def detalhes(request, pk):
    cadastro = get_object_or_404(PessoaFisica, pk=pk)
    template_name = 'core/visualizar-detalhes.html'
    context = {
        'cadastro': cadastro,
    }
    return render(request, template_name, context)

# Funçao usada pra emitir boleto
def emissao(request):
	return render(request, 'emissao.html')