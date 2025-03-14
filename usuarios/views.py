from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Servico


# Página de login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                form.add_error(None, "Usuário ou senha inválidos.")
                return render(request, 'registration/login.html', {'form': form})
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# Redirecionamento para o dashboard
@login_required
def dashboard(request):
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def servicos_view(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

@login_required
def listar_servicos_view(request):
    servicos = Servico.objects.all()
    return render(request, 'listar_servicos.html', {'servicos': servicos})

@login_required
def adicionar_servico(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data = request.POST['data']
        valor = request.POST['valor']
        descricao = request.POST['descricao']

        servico = Servico(nome=nome, data=data, valor=valor, descricao=descricao)
        servico.save()

        return redirect('servicos') 

    return render(request, 'adicionar_servico.html')

@login_required
def alterar_servico_view(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')

        servico.nome = nome
        servico.data = data
        servico.valor = valor
        servico.descricao = descricao

        servico.save()

        return redirect('servicos')

    return render(request, 'alterar_servico.html', {'servico': servico})


@login_required
def servicos_para_excluir(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos_para_excluir.html', {'servicos': servicos})

@login_required
def confirmar_exclusao(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == "POST":
        servico.delete()
        messages.success(request, "Serviço excluído com sucesso.")
        return redirect('servicos')

    return render(request, 'confirmar_exclusao.html', {'servico': servico})
@login_required
def pesquisar_servico(request):
    query = request.GET.get('q', '')
    servicos = Servico.objects.filter(nome__icontains=query)
    return render(request, 'servicos.html', {'servicos': servicos})