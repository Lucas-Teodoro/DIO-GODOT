vitorias = 5001
derrotas = 4999
saldoVitorias = vitorias - derrotas
nivel = ""

if (saldoVitorias >= 101):
  nivel = "Imortal"
if (saldoVitorias > 90):
  nivel = "Lendário"
if (saldoVitorias > 80):
  nivel = "Diamante"
if (saldoVitorias > 50):
  nivel = "Ouro"
if (saldoVitorias > 20):
  nivel = "Prata"
if (saldoVitorias > 10):
  nivel = "Bronze"
if (saldoVitorias <= 10):
  nivel = "Ferro"
  
print (f'O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}')
