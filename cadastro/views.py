# coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse

def cadastro(request):
	return render_to_response("cadastro.html")