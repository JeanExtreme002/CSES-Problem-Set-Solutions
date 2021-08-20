def find_number(x, y):
    base = max([x, y]) # Obtém o maior número para formar um quadrado (base²).

    # Se a base for par, significa que o maior valor dentro do quadrado está
    # localizado à direita na última linha do quadrado. Exemplo (4²):
    #
    # 01 02 09 10
    # 04 03 08 11
    # 05 06 07 12
    # 16 15 14 13     <- O maior valor é 16 e está na última linha, à direita.
    #
    # Para obtermos o valor na posição (X, Y), basta se mover para trás. Primeiro,
    # devemos nos mover com base na posição Y (coluna). Exemplo (Y = 4):
    #
    # 01 02 09 10
    # 04 03 08 11
    # 05 06 07 12
    # 16 15 14 13
    #  >  >  >  Y     <- Estamos na coluna do número, saindo da coluna 1 e indo para 4 [movemos (+3) colunas (4 - 1)].
    #
    # Depois disso, nos movemos com base na posição X (linha). Exemplo (X = 2):
    #
    # 01 02 09 10
    # 04 03 08 11 X   <- Estamos na linha do número, saindo da linha 4 e indo para 2 [movemos (-2) linhas (base - 2)].
    # 05 06 07 12 ^
    # 16 15 14 13 ^
    #  >  >  >  Y
    #
    # No final das contas, temos a fórmula: BASE² - (Y - 1) - (BASE - X).
    # Exemplo: N(2, 4) = 4² - (4 - 1) - (4 - 2) = 16 - 3 - 2 = [11]
    if base % 2 == 0: return base ** 2 - (y - 1) - (base - x)

    # Se a base for ímpar, significa que o maior valor dentro do quadrado está
    # localizado à esquerda, na primeira linha do quadrado. Exemplo (3²):
    #
    # 01 02 09        <- O maior valor é 09 e está na primeira linha, à esquerda.
    # 04 03 08
    # 05 06 07
    #
    # Nesse caso, o processo é o mesmo, no entanto, trocamos na fórmula a variável X por Y e Y por X. Isso porque,
    # diferentemente do quadrado de base par, onde nos movemos para cima (base - x) no eixo X, aqui, nos movemos
    # para baixo (x - 1). Exemplo (X = 3):
    #
    # 01 02 09 v
    # 04 03 08 v
    # 05 06 07 X      <- Estamos na linha do número, saindo da linha 1 e indo para 3 [movemos (+2) linhas (3 - 1)].
    #
    # E diferentemente do quadrado de base par, onde nos movemos para esquerda (y - 1) no eixo Y, aqui, nos movemos
    # para direita (base - y). Exemplo (Y = 1):
    #
    # 01 02 09 v
    # 04 03 08 v
    # 05 06 07 X
    #  Y  <  <        <- Estamos na coluna do número, saindo da coluna 3 e indo para 1 [movemos (-2) colunas (base - 1)].
    #
    # Sendo assim, temos a fórmula: BASE² - (X - 1) - (BASE - Y).
    # Exemplo: N(3, 1) = 3² - (3 - 1) - (3 - 1) = 9 - 2 - 2 = [05]
    return base ** 2 - (x - 1) - (base - y)

t = int(input())

# Obtém os dados de entrada (X, Y) e imprime o valor encontrado.
for i in range(t):
    x, y = [int(i) for i in input().split()]
    print(find_number(x, y))
