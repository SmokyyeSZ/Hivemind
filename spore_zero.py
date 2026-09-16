"""
========================= Índice =========================

[BLOCO: Importes]
[BLOCO: Classes ]

"""

#[------------------------ ------------------------]
#|                BLOCO: Imports                   |
#[------------------------ ------------------------]

import requests

#[------------------------ ------------------------]
#|                BLOCO: Classes                   |
#[------------------------ ------------------------]

class OSINTSpore:

    def __init__(self, target):
        self.target = target

    def fetch_headers(self):

        resp = requests.get(self.target)

        print(f"{resp.headers['Server']}")

esporo_zero = OSINTSpore('http://scanme.nmap.org')

esporo_zero.fetch_headers()

