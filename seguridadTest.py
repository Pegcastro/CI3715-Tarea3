import unittest
from seguridad import Seguridad

class SeguridadTest(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()

    def testSeguridad(self):
        self.seguridad = Seguridad()
        self.assertEqual(len(self.seguridad.dict), 0)

    def test_caso_frontera_email(self):
        self.assertFalse(self.seguridad.ingresarUsuario('a', 'aAa12345', 'aAa12345'))

if __name__ == '__main__':
    unittest.main()