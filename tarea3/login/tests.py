from django.test import TestCase
from .func import *

# Create your tests here.
class SeguridadModelTests(TestCase):

    def test_caso_frontera_email_registro_1(self):
        self.assertIs(registrarUsuario('a', 'aAa12345', 'aAa12345')[0], False)

    def test_caso_frontera_email_registro_2(self):
        self.assertIs(registrarUsuario('pagoncastro@gmail.com', 'Pablito1', 'Pablito1')[0], True)

    def test_caso_frontera_pass_registro_2(self):
        self.assertIs(registrarUsuario('pagoncastro@gmail.com', 'a', 'a')[0], True)

    def test_caso_frontera_pass_registro_2(self):
        self.assertIs(registrarUsuario('pagoncastro@gmail.com', 'Pablito1', 'Pablito2')[0], False)

    def test_interno_ingreso_1(self):
        self.assertIs(ingresarUsuario('pagoncastro@gmail.com', 'Pablito1')[0], True)
    
    def test_interno_ingreso_2(self):
        self.assertIs(ingresarUsuario('pagoncastro@gmail.com', 'Pablito2')[0], False)

    def test_interno_ingreso_3(self):
        self.assertIs(ingresarUsuario('almiavicas@gmail.com', 'Pablito1')[0], False)

    
