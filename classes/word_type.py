#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WordType:
    TYPES_HASH = {
        "ADV":     "adverbio",        # HSK1
        "ADJ":     "adjetivo",        # HSK1
        "CLA":     "clasificador",    # HSK1
        "CON":     "conjunción",      # HSK1
        "FH":      "frase hecha",     # HSK1
        "INT":     "interjección",    # HSK1
        "MOD":     "verbo modal",     # HSK1
        "NOM":     "nombre",          # HSK1
        "NP":      "nombre propio",   # HSK1
        "NUM/CLA": "num./clas.",      # HSK1
        "PRE":     "preposición",     # HSK1
        "PRO":     "pronombre",       # HSK1
        "PT":      "partícula",       # HSK1
        "VER":     "verbo"            # HSK1

        # "PREF": "prefijo",
        # "SUF":  "sufijo",
        # "V+O":  "verbo + objeto",
        # "V+C":  "verbo + complementos",
        # "VAUX": "verbo auxiliar",
        # "PTV":  "partícula verbal",
        # "PI":   "partícula interrogativa",
        # "PM":   "partícula modal",
        # "NUM":  "numeral",
        # "OTR":  "otro",
    }

    # TYPES_HASH_BOOK = {
    #     "ADV":  "Adv.",
    #     "ADJ":  "Adj.",
    #     "PRO":  "Pron.",
    #     "PRE":  "preposición",
    #     "PREF": "prefijo",
    #     "SUF":  "sufijo",

    #     "NOM":  "N",
    #     "NP":   "n.p.",

    #     "VER":  "V",
    #     "V+O":  "VO",
    #     "V+C":  "verbo + complementos",
    #     "VAUX": "V.Aux.",

    #     "PT":   "partícula",
    #     "PTV":  "partícula verbal",
    #     "PI":   "PrI",
    #     "PM":   "PtM",

    #     "CLA":  "Clas.",
    #     "CON":  "conjunción",
    #     "NUM":  "Num.",
    #     "INT":  "Int",
    #     "FH":   "F.h.",
    #     "OTR":  "otro",

    #     "NUM/CLA": "Num./Clas."  # HSK4
    # }

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
        # self.book_type = self.TYPES_HASH_BOOK[key]

    def short_word_type(self):
        return self.SHORT_WORD_TYPE.get(self.key) or self.key
