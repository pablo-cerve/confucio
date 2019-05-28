#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WordType:
    TYPES_HASH = {
        "NOM": "Nom.",
        "ADV": "Adv.",
        "ADJ": "Adj.",
        "PRO": "Pron.",
        "PRE": "Prep.",
        "VER": "Verbo",
        "VMO": "Verbo+Obj",
        "NP":  "Nom.Prop.",
        "PI":  "P.I.",
        "CLA": "Clas.",
        "CON": "Conj.",
        "NUM": "Num.",
        "OTR": "Otro",
        "INT": "Interj.",
        "FH":  "Frase Hecha",
        "PT":  "Part.",
        "VAUX": "Verbo Aux."
    }

    def __init__(self, key):
        self.key = key
        self.type = self.TYPES_HASH[key]
