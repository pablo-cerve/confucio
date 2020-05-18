#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WordType:
    TYPES_HASH = {
        "ADV":  "adverbio",
        "ADJ":  "adjetivo",
        "PRO":  "pronombre",
        "PRE":  "preposición",

        "NOM":  "nombre",
        "NP":   "nombre propio",

        "VER":  "verbo",
        "VMO":  "verbo + objeto",
        "VMC":   "verbo + complementos",
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

    def __init__(self, key):
        self.key = key
        self.type = self.TYPES_HASH[key]
