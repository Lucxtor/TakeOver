import random
import string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Sala, Disciplina, Alunos
from django.db.models import Subquery


# Create your views here.


def takeOver(request):
    return render(request, 'index.html')


def jogar(request):
    return render(request, 'jogo.html')


def submit_cadastrar(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            # next_page = request.GET['next']
            login(request, usuario)
            return redirect('/')
    else:
        messages.error(request, "Algo está errado no seu cadastro, por favor verifique os campos novamente!")
        return render(request, 'login.html')


def cadastrar(request):
    return render(request, 'cadastro.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            # next_page = request.GET['next']
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário e/ou senha inválido!")
            return render(request, 'login.html')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login/')
def minhasSalas(request):
    usuario = request.user
    dados = {'minhasSalas': Sala.objects.filter(adm_sala=usuario),
             'alunoSala': Sala.objects.filter(id__in=Alunos.objects.filter(usuario=usuario).values('sala'))
             }
    return render(request, 'minhasSalas.html', dados)


@login_required(login_url='login/')
def criarSala_cadastro(request):
    disciplinas = {'disciplinas': Disciplina.objects.all()}
    return render(request, 'criarSala_Cadastro.html', disciplinas)


@login_required(login_url='login/')
def submit_criarSala_cadastro(request):
    if request.POST:
        nome_sala = request.POST.get('nomeSala')
        adm_sala = request.user
        conteudo_sala = request.POST.get('conteudo')
        codigo_sala = ''.join(
            random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(7))
        desc_sala = request.POST.get('desc')
        if request.POST.get('opCompartilhar') == "on":
            visibilidade_sala = 'True'
        else:
            visibilidade_sala = 'False'

        disciplina = request.POST.get('disciplina')
        disc = Disciplina.objects.filter(nome_disc=disciplina)
        Sala.objects.create(nome_sala=nome_sala,
                            adm_sala=adm_sala,
                            conteudo_sala=conteudo_sala,
                            codigo_sala=codigo_sala,
                            desc_sala=desc_sala,
                            visibilidade_sala=visibilidade_sala,
                            # disciplina=disc,
                            )
    return redirect('/criarSala_compartilhar/{}'.format(codigo_sala), request)


def criarSala_compartilhar(request, codigoSala):
    minhaSala = {'minhaSala': Sala.objects.filter(codigo_sala=codigoSala)}
    return render(request, 'criarSala_Compartilhar.html', minhaSala)


def salas(request, codigo):
    sala = {'sala': Sala.objects.filter(codigo_sala=codigo)}
    return render(request, 'sala.html', sala)


@login_required(login_url='login/')
def entrarSala(request):
    return render(request, 'entrarSala.html')


@login_required(login_url='login/')
def apagarSala(request, codigo):
    sala = Sala.objects.filter(codigo_sala=codigo)
    adm = User.objects.get(id__in=Sala.objects.filter(codigo_sala=codigo).values('adm_sala'))
    if adm.id == request.user.id:
        sala.delete()
    return redirect('/')

@login_required(login_url='login/')
def user(request):
    return render(request, 'usuario.html')


@login_required(login_url='login/')
def submit_atualizar_user(request):
    if request.POST:
        pass


def eixoCivil(request):
    return render(request, 'eixoCivil.html')


def eixoDiplomatico(request):
    return render(request, 'eixoDiplomatico.html')


def eixoSocial(request):
    return render(request, 'eixoSocial.html')


def eixoEconomico(request):
    return render(request, 'eixoEconomico.html')