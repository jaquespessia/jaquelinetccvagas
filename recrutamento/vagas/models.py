from django.db import models

class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    requisitos = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    curriculo = models.FileField(upload_to='curriculos/')

    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidato.nome} → {self.vaga.titulo}"
