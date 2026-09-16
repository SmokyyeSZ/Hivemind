from Spores.osint_spore import OSINTSpore
from mother import MotherMind

spore_zero = OSINTSpore('http://scanme.nmap.org')

dado_bruto = spore_zero.fetch_headers()
Mother = MotherMind()

Mother.memoria[spore_zero.dna] = {'server': dado_bruto} 

print(Mother.memoria)