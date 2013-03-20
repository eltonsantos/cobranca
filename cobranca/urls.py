# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cobranca.views.home', name='home'),
    # url(r'^cobranca/', include('cobranca.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r"^$", "cadastro.views.login", name="home"),
    url(r"^$", "django.contrib.auth.views.login", {'template_name' : 'login.html'}, name="login"),    
    url(r"^logout/$", "django.contrib.auth.views.logout", {'next_page' : '/'}, name="logout"),     
    #url(r'^cadastro/', "cadastro.views.cadastro"),
    url(r"^cadastro-usuarios/", "cadastro.views.cadusuarios"),
    url(r"^cadastro-pessoas/", "cadastro.views.cadpessoas"),
    url(r"^visualizar-cadastrados/", "cadastro.views.visualizar"),
    url(r"^visualizar-detalhes/(?P<pessoa_id>\d+)/$", 'cadastro.views.detalhes', name="visualizar-detalhes"),
    url(r"^principal/", "cadastro.views.principal"),
    #url(r"^cadastro/emissao/", "emissao.views.emissao"),


)