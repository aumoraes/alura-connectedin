#from django.conf.utls import patterns, url
from django.contrib import admin
from django.urls import include, path, re_path
#from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth.views import login, logout_then_login
#from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^', views.index)
    #path('', index),
    #path('perfis/', exibir),
    re_path(r'^registrar/$', RegistrarUsuarioView.as_view(), name="registrar"),
    re_path(r'^login/$', login, { 'template_name' : 'login.html'}, name="login"),
    re_path(r'^logout/$', logout_then_login, { 'login_url' : '/login/'}, name="logout"),
    #re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name="exibir"),
    #re_path(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name='convidar'),
    #re_path(r'^convite/(?P<convite_id>\d+)/aceitar$', aceitar, name='aceitar'),
]
