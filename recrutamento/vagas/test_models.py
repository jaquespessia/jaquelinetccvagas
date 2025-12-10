from django.test import TestCase
from vagas.models import Vaga, Candidato, Candidatura


class VagaModelTest(TestCase):

    def test_criacao_vaga(self):
        vaga = Vaga.objects.create(
            titulo='Dev Júnior',
            descricao='Desenvolvimento web',
            requisitos='Python, Django'
        )

        self.assertEqual(str(vaga), 'Dev Júnior')
        self.assertIsNotNone(vaga.criado_em)


class CandidatoModelTest(TestCase):

    def test_criacao_candidato(self):
        candidato = Candidato.objects.create(
            nome='Maria Silva',
            email='maria@example.com',
            telefone='11999999999',
            curriculo='curriculos/teste.pdf'
        )

        self.assertEqual(str(candidato), 'Maria Silva')
        self.assertEqual(candidato.email, 'maria@example.com')


class CandidaturaModelTest(TestCase):

    def test_criacao_candidatura(self):
        vaga = Vaga.objects.create(
            titulo='Dev Pleno',
            descricao='Manutenção de sistemas',
            requisitos='Python, REST'
        )

        candidato = Candidato.objects.create(
            nome='João Souza',
            email='joao@example.com',
            telefone='11988888888',
            curriculo='curriculos/joao.pdf'
        )

        candidatura = Candidatura.objects.create(
            vaga=vaga,
            candidato=candidato
        )

        self.assertEqual(str(candidatura), 'João Souza → Dev Pleno')
        self.assertIsNotNone(candidatura.data)
        self.assertEqual(candidatura.vaga.titulo, 'Dev Pleno')
        self.assertEqual(candidatura.candidato.nome, 'João Souza')
