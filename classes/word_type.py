#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WordType:
    TYPES_HASH = {
        "NOM":   "Nombre",
        "ADV": "Adverbio",
        "ADJ": "Adjetivo",
        "PRO": "Pronombre",
        "PRE": "Preposición",
        "VER": "Verbo",
        "NP":  "Nombre Propio",
        "PI":  "Particula Interrogativa",
        "CLA": "Clasificador",
        "CON": "Conjunción",
        "NUM": "Numeral",
        "OTR": "Otro",
        "INT": "Interjección",
        "FH":  "Frase Hecha",
        "PT":  "Partícula"
    }

    def __init__(self, key):
        self.key = key
        self.type = self.TYPES_HASH[key]
