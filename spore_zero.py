"""
========================= Índice =========================

[BLOCO: Importes]
[BLOCO: Classes ]

"""

#[------------------------ ------------------------]
#|                BLOCO: Imports                   |
#[------------------------ ------------------------]

import requests
from uuid import uuid4

#[------------------------ ------------------------]
#|                BLOCO: Classes                   |
#[------------------------ ------------------------]

class OSINTSpore:

    def __init__(self, target):
        self.target = target
        self.dna = str(uuid4())

    def fetch_headers(self):
        resp = requests.get(self.target)
        return resp.headers['server']

class MotherMind:
    def __init__(self):
        self.memoria = {}


spore_zero = OSINTSpore('http://scanme.nmap.org')

dado_bruto = spore_zero.fetch_headers()
Mother = MotherMind()

Mother.memoria[spore_zero.dna] = {'server': dado_bruto} 

print(Mother.memoria)