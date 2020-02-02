import unittest
from seguridad import Seguridad

class SeguridadTest(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()

    def testSeguridad(self):
        self.seguridad = Seguridad()
        self.assertEqual(len(self.seguridad.dict), 0)

    def test_caso_frontera_email_registro(self):
        self.assertEqual(self.seguridad.registrarUsuario('a', 'aAa12345', 'aAa12345'), False)
    
    def test_caso_frontera_pass_regitro(self):
        self.assertEqual(self.seguridad.registrarUsuario('pagoncastro@gmail.com', 'Pablito1', 'Pablito1'), True)


if __name__ == '__main__':
    unittest.main()