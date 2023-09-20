import unittest
import doctest
import locale

from funcoes import calculo_digita, calculo_arquivo

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

class TestCalculoFuncoes(unittest.TestCase):
    # Não funciona sem return
    def test_calculo_digita(self):
        resultado = calculo_digita("23 de Agosto de 2023 - 18 de Setembro de 2023")
        self.assertEqual(resultado, "O número de dias entre essas datas é:  25")

        resultado = calculo_digita("18 de Setembro de 2023 - 23 de Agosto de 2023")
        self.assertEqual(resultado, "O número de dias entre essas datas é:  25")


    # Funciona corretamente
    def test_calculo_arquivo(self):
        with open("input.txt", "w") as f:
            f.write("23 de Agosto de 2023 - 18 de Setembro de 2023\n")


        resultado = calculo_arquivo("input.txt")
        self.assertEqual(resultado, "Diferença de dias: 25")


if __name__ == "__main__":
    unittest.main()

