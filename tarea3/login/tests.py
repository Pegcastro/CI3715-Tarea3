from django.test import TestCase
from .func import *

# Create your tests here.
class SeguridadModelTests(TestCase):

    def test_caso_frontera_email_registro_1(self):
        self.assertIs(registrarUsuario('a', 'aAa12345', 'aAa12345'), False)