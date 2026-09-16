from uuid import uuid4
import requests

class OSINTSpore:

    def __init__(self, target):
        self.target = target
        self.dna = str(uuid4())

    def fetch_headers(self):
        resp = requests.get(self.target)
        return resp.headers['server']