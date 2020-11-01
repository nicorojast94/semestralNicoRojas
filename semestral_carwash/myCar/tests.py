from django.test import TestCase
import unittest

# Create your tests here.


class TestBDD(unittest.TestCase):

    def test_grabar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre="elpepe",
                descripcion="jabonoso",
                precio=4000,
                stock=45
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

if __name__=="__main__":
    unittest.main()


class TestBDD(unittest.TestCase):

    def test_modificar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre="eetesech",
                descripcion="espumoso",
                precio=3000,
                stock=20
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

if __name__=="__main__":
    unittest.main()
