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
    #url(r"^$", "core.views.login", name="home"),
    url(r"^$", "django.contrib.auth.views.login", {'template_name' : 'login.html'}, name="login"),    
    url(r"^logout/$", "django.contrib.auth.views.logout", {'next_page' : '/'}, name="logout"),     
    #url(r'^cadastro/', "core.views.cadastro"),
    url(r"^cadastro-usuarios/", "core.views.cadusuarios"),
    url(r"^cadastro-pessoas/", "core.views.cadpessoas"),
    #url(r"^cadastro-pessoa-fisica/", "core.views.cadpessoafisica"),
    #url(r"^cadastro-pessoa-juridica/", "core.views.cadpessoajuridica"),
    url(r"^visualizar-cadastrados/", "core.views.visualizar"),
    url(r"^(?P<pk>\d+)/$", 'core.views.detalhes', name="visualizar-detalhes"),
    url(r"^principal/", "core.views.principal"),
    url(r'^municipios/', include('municipios.urls')),
    #url(r"^cadastro/emissao/", "emissao.views.emissao"),


)