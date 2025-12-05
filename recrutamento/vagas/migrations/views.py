from django.shortcuts import render, get_object_or_404, redirect
from .models import Vaga, Candidatura
from .forms import CandidaturaForm

def index(request):
    vagas = Vaga.objects.all()
    return render(request, "vagas/index.html", {"vagas": vagas})

def vaga_detalhe(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)

    if request.method == "POST":
        form = CandidaturaForm(request.POST, request.FILES)
        if form.is_valid():
            candidato = form.save()
            Candidatura.objects.create(vaga=vaga, candidato=candidato)
            return redirect("candidatura_sucesso")
    else:
        form = CandidaturaForm()

    return render(request, "vagas/vaga_detalhe.html", {"vaga": vaga, "form": form})

def candidatura_sucesso(request):
    return render(request, "vagas/candidatura_sucesso.html")

def lista_candidatos(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    candidaturas = Candidatura.objects.filter(vaga=vaga)
    return render(request, "vagas/lista_candidatos.html", {"vaga": vaga, "candidaturas": candidaturas})
