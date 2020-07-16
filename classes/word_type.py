#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WordType:
    TYPES_HASH_BOOK_2 = {
        "Adv.":  "adverbio",
        "A":     "adjetivo",


        "N":     "nombre",
        "NP":    "nombre propio",

        "V":     "verbo",
        "VO":    "verbo + objeto",

        "Clas.": "clasificador",
        "Conj.": "conjunción",


        "EF":    "expresión fija"
    }

    TYPES_HASH = {
        "ADV":  "adverbio",
        "ADJ":  "adjetivo",
        "PRO":  "pronombre",
        "PRE":  "preposición",

        "NOM":  "nombre",
        "NP":   "nombre propio",

        "VER":  "verbo",
        "VMO":  "verbo + objeto",
        "VMC":  "verbo + complementos",
        "VAUX": "verbo auxiliar",

        "PT":   "partícula",
        "PI":   "partícula interrogativa",
        "PM":   "partícula modal",

        "CLA":  "clasificador",
        "CON":  "conjunción",
        "NUM":  "numeral",
        "INT":  "interjección",
        "FH":   "frase hecha",
        "OTR":  "otro"
    }

    TYPES_HASH_BOOK = {
        "ADV":  "Adv.",
        "ADJ":  "Adj.",
        "PRO":  "Pron.",
        "PRE":  "preposición",

        "NOM":  "N",
        "NP":   "n.p.",

        "VER":  "V",
        "VMO":  "VO",
        "VMC":  "verbo + complementos",
        "VAUX": "V.Aux.",

        "PT":   "partícula",
        "PI":   "PrI",
        "PM":   "PtM",

        "CLA":  "Clas.",
        "CON":  "conjunción",
        "NUM":  "Num.",
        "INT":  "Int",
        "FH":   "F.h.",
        "OTR":  "otro"
    }

    def __init__(self, key, book_number=None):
        if book_number == 2:
            self.key = key
            self.type = self.TYPES_HASH_BOOK_2[key]
            self.book_type = key
        else:
            self.key = key
            self.type = self.TYPES_HASH[key]
            self.book_type = self.TYPES_HASH_BOOK[key]
