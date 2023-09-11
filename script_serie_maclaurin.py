# Importação da biblioteca math e da função "funcao_cosseno_maclaurin":
import math
from decimal import Decimal
from funcao_cosseno_maclaurin import maclaurin_cosseno


# RA: 082220003
ultimo = 3

penultimo = 0

if penultimo == 0:
    precisao_desejada = 1e-9

# Definição do valor de x:
x = (ultimo+1)/10

resultado, termos = maclaurin_cosseno(x, precisao_desejada)

# Impressão dos resultados em tela:
print("Numero de termos: ", termos)

print("Valor da função (maclaurin): ", resultado)
print("valor da função cos: ", math.cos(x))
print("Diferença (em módulo): ", abs(Decimal(math.cos(x)) - resultado))
