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
    url(r"^$", "core.views.login", name="home"),
    url(r"^cadastro/", "core.views.cadastro"),
    url(r"^principal/", "core.views.principal"),
    #url(r"^cadastro/emissao/", "emissao.views.emissao"),


)
