from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('servicos/', views.servicos_view, name='servicos'),
    path('servicos/adicionar/', views.adicionar_servico, name='adicionar_servico'),
    path('servicos/alterar/', views.listar_servicos_view, name='listar_servicos'),
    path('servicos/alterar/<int:id>/', views.alterar_servico_view, name='alterar_servico'),
    path('servicos/excluir/', views.servicos_para_excluir, name='servicos_para_excluir'),
    path('servicos/excluir/<int:id>/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('servicos/pesquisar/', views.pesquisar_servico, name='pesquisar_servico'),
]
