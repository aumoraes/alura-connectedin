from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil, Convite
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods

from django.contrib.auth.models import User

from django.http import HttpResponseForbidden

import logging
logger = logging.getLogger(__name__)


@login_required
@require_http_methods(["GET"])
def index(request):


    perfis = None
    perfil_logado = None

    try:
       perfis = Perfil.objects.all()
    except Exception as error:
        print("Nenhum usuário para mostrar na tela de index")

    try:
       perfil_logado = get_perfil_logado(request)
    except Exception as error:
        print("Nenhum usuário logado %s" %(error))



    return render(request, 'index.html', { 'perfis' : perfis,
   'perfil_logado' : perfil_logado})

@login_required
def exibir(request, perfil_id):

    perfil = None
    perfil_logado = None
    try:
        perfil = Perfil.objects.get(id=perfil_id)
        perfil_logado = get_perfil_logado(request)
    except Exception as error:
        print("Consulta do usuario com o id %s não encontrado" %(perfil_id))

    if perfil == perfil_logado:
        return render(request, 'perfil.html', {'perfil' : perfil, 'perfil_logado' : perfil_logado,
           'perfil_igual_perfil_logado' : True})

    ja_eh_contato = perfil in perfil_logado.contatos.all()

    return render(request, 'perfil.html', {'perfil' : perfil, 'perfil_logado' : perfil_logado,
                   'ja_eh_contato' : ja_eh_contato})

@login_required
@permission_required('perfis.add_convite', raise_exception=False)
def convidar(request, perfil_id):

    if not request.user.has_perm('perfis.add_convite'):
        return HttpResponseForbidden('Acesso negado')

    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index');

@login_required
def get_perfil_logado(request):
    if request.user.is_authenticated:
        pass

    return request.user.perfil

@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
