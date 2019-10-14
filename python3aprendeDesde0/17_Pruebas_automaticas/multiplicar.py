# Unittest - Sirve para crear pruebas dentrod el propio código
def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(2,4)
print(resultado)

import unittest
class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(4,2), 8)
        # self.assertEqual(multiplicar(4,2), 9) # test que falla

if __name__ == "__main__":
    unittest.main()