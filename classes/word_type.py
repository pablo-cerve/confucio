#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WordType:
    TYPES_HASH = {
        "ADV":  "adverbio",
        "ADJ":  "adjetivo",
        "PRO":  "pronombre",
        "PRE":  "preposición",
        "PREF": "prefijo",
        "SUF":  "sufijo",

        "NOM":  "nombre",
        "NP":   "nombre propio",

        "VER":  "verbo",
        "V+O":  "verbo + objeto",
        "V+C":  "verbo + complementos",
        "VAUX": "verbo auxiliar",

        "PT":   "partícula",
        "PTV":  "partícula verbal",
        "PI":   "partícula interrogativa",
        "PM":   "partícula modal",

        "CLA":  "clasificador",
        "CON":  "conjunción",
        "NUM":  "numeral",
        "INT":  "interjección",
        "FH":   "frase hecha",
        "OTR":  "otro",

        "NUM/CLA": "Num./Clas."  # HSK4
    }

    TYPES_HASH_BOOK = {
        "ADV":  "Adv.",
        "ADJ":  "Adj.",
        "PRO":  "Pron.",
        "PRE":  "preposición",
        "PREF": "prefijo",
        "SUF":  "sufijo",

        "NOM":  "N",
        "NP":   "n.p.",

        "VER":  "V",
        "V+O":  "VO",
        "V+C":  "verbo + complementos",
        "VAUX": "V.Aux.",

        "PT":   "partícula",
        "PTV":  "partícula verbal",
        "PI":   "PrI",
        "PM":   "PtM",

        "CLA":  "Clas.",
        "CON":  "conjunción",
        "NUM":  "Num.",
        "INT":  "Int",
        "FH":   "F.h.",
        "OTR":  "otro",

        "NUM/CLA": "Num./Clas."  # HSK4
    }

    SHORT_WORD_TYPE = {
        "NOM": "N",
        "VER": "V",
        "PRO": "P",
        "ADV": "A",
        "ADJ": "a"
    }

    def __init__(self, key):
        self.key = key
        self.type = self.TYPES_HASH[key]
        self.book_type = self.TYPES_HASH_BOOK[key]

    def short_word_type(self):
        return self.SHORT_WORD_TYPE.get(self.key) or self.key
