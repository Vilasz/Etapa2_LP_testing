# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 07:47:06 2023

@author: joaod
"""

from funcao import calcula_dif
from retorna_arquivo import retorna_arquivo

def main():
    """
    Função que calcula a diferença de dias entre duas datas.
    
    Essa função recebe duas datas em um input ou lê a partir de um arquivo, calcula os dias entre as duas datas, e printa o resultado.
    
    Example:
    >>> # Simula o input de duas datas
    >>> # Forneça o nome do arquivo ou a data desejada: 22 de Agosto de 2023 - 23 de Agosto de 2023
    >>> # Número de dias entre as duas datas: 1
    >>> main()

    >>> # Simula o input de um arquivo
    >>> # Forneça o nome do arquivo ou a data desejada: texto_datas
    >>> # Número de dias entre as duas datas: 287
    >>> main()

    """
    datas = input("Forneça o nome do arquivo ou a data desejada:")

    if "-" in datas: 
        datas = datas
    else: 
        datas = retorna_arquivo(datas)

    dif_datas = calcula_dif(datas)

    # Print days:
    # print("Número de dias entre as duas datas:", dif_datas)
    return dif_dias

if __name__ == "__main__":
    main()
