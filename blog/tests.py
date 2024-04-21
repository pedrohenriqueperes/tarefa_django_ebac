from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(titulo='Teste', conteudo='Este é um post de teste.')

    def test_texto_titulo(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.titulo}'
        self.assertEqual(expected_object_name, 'Teste')

    def test_data_publicacao_recente(self):
        post = Post.objects.get(id=1)
        self.assertTrue(post.data_publicacao <= timezone.now())
