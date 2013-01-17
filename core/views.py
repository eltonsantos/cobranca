# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def login(request):
	context = {
		"nome" : u"Elton Santos",
		"email" : u"elton.melo.santos@gmail.com",
	}
	return render_to_response('login.html', context, RequestContext(request))



def cadastro(request):
	return render_to_response('cadastro.html')

def emissao(request):
	return render_to_response('emissao.html')