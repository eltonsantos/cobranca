from django.shortcuts import render_to_response
from django.http import HttpResponse

def login(request):
	return render_to_response('login.html')

def cadastro(request):
	return render_to_response('cadastro.html')

def emissao(request):
	return render_to_response('emissao.html')