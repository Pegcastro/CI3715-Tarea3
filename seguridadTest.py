import unittest
from seguridad import Seguridad

class SeguridadTest(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()

    def testSeguridad(self):
        self.seguridad = Seguridad()
        self.assertEqual(len(self.seguridad.dict), 0)

    def test_caso_frontera_email_registro_1(self):
        self.assertEqual(self.seguridad.registrarUsuario('a', 'aAa12345', 'aAa12345'), False)
    
    def test_caso_frontera_email_regitro_2(self):
        self.assertEqual(self.seguridad.registrarUsuario('pagoncastro@gmail.com', 'Pablito1', 'Pablito1'), True)
    
    def test_caso_frontera_pass_registro_1(self):
        self.assertEqual(self.seguridad.registrarUsuario('pagoncastro@gmail.com', 'a', 'a'), False)

if __name__ == '__main__':
    unittest.main()