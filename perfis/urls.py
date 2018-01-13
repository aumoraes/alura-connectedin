
from django.contrib import admin
from django.urls import include, path, re_path
#from django.conf.utls import patterns, url
#
from perfis.views import index, exibir, convidar, aceitar

urlpatterns = [
    # url(r'^', views.index)
    #path('', index),
    #path('perfis/', exibir),
    re_path(r'^$', index, name="index"),
    re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name="exibir"),
    re_path(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name="convidar"),
    re_path(r'^convite/(?P<convite_id>\d+)/aceitar', aceitar, name="aceitar"),

    #re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name="exibir"),

]
