from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('vaga/<int:pk>/', views.vaga_detalhe, name="vaga_detalhe"),
    path('sucesso/', views.candidatura_sucesso, name="candidatura_sucesso"),
    path('vaga/<int:pk>/candidatos/', views.lista_candidatos, name="lista_candidatos"),
]
