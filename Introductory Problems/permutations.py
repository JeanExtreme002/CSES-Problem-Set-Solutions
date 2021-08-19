n = int(input())

# Não há solução se N for 2 ou 3.
if 2 <= n <= 3: print("NO SOLUTION")

# Coloca todos os números pares à esquerda e ímpares à direita. Dessa forma,
# eu garanto que haverá uma distância de pelo menos 2 entre os números.
# Exemplo (n = 10): 2 4 6 8 10 1 3 5 7 9
else:
    for i in range(2, n + 1, 2):
        print(i, end = " ")

    for i in range(1, n + 1, 2):
        print(i, end = " ")
