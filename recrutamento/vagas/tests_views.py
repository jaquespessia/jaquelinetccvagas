from django.test import TestCase
from django.urls import reverse

from .models import Vaga, Candidato, Candidatura


class RecrutamentoViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.vaga1 = Vaga.objects.create(
            titulo="Desenvolvedor Backend",
            descricao="Experiência com Python e Django",
            requisitos="Django, PostgreSQL"
        )

        
        cls.candidato1 = Candidato.objects.create(
            nome="Maria Ferreira",
            email="maria@example.com",
            telefone="11999999999"
        )

       
        cls.candidatura1 = Candidatura.objects.create(
            vaga=cls.vaga1,
            candidato=cls.candidato1,
            mensagem="Tenho experiência em Django."
        )

    def test_criar_vaga(self):
        url = reverse('criar_vaga')
        dados = {
            'titulo': 'Analista de Dados',
            'descricao': 'Análise de grandes volumes de dados',
            'requisitos': 'Python, SQL, PowerBI'
        }

        self.client.post(url, data=dados)

        self.assertTrue(
            Vaga.objects.filter(titulo='Analista de Dados').exists()
        )

    
    def test_listar_vagas(self):
        url = reverse('listar_vagas')
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Desenvolvedor Backend")

   
    def test_criar_candidatura(self):
        url = reverse('criar_candidatura')
        dados = {
            'vaga': self.vaga1.id,
            'candidato': self.candidato1.id,
            'mensagem': 'Tenho interesse na vaga!'
        }

        self.client.post(url, data=dados)

        self.assertTrue(
            Candidatura.objects.filter(mensagem='Tenho interesse na vaga!').exists()
        )

    def test_listar_candidatos_por_vaga(self):
        url = reverse('listar_candidatos_vaga', kwargs={'vaga_id': self.vaga1.id})
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Maria Ferreira")
