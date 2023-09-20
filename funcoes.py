# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:07:52 2023

@author: joaod
"""

import datetime, locale
import sys

def calcula_dif (duas_datas) :
    
    # Set the locale to Portuguese
    locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')

    # Define the date format for parsing
    formato = "%d de %B de %Y"

    try: 
        # Split the dates based on the " - " separator
        datas = duas_datas.split(" - ")
    except AttributeError: 
        print("Você provavelmente digitou errado.")
        sys.exit()
        

    # Parse each date string into a datetime object
    parsed_dates = []
    for date_str in datas:
        parsed_date = datetime.datetime.strptime(date_str, formato)
        parsed_dates.append(parsed_date)

    dif_days = (parsed_dates[1] - parsed_dates[0]).days
    
    return dif_days

def retorna_arquivo(filename):
    try:
        with open(f"{filename}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Arquivo '{filename}.txt' não encontrado. Por favor, forneça um arquivo válido.")
        return None
