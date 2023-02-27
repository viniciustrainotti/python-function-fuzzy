import matplotlib.pyplot as plt

def fuzzy(d):
    tam = 2*d+1
    # print(f"tamanho do vetor {tam}")
    # inicializa o vetor com zeros
    graus = [0]*tam
    # máximo do grau de pertinência
    maximo = d
    for i in range(tam):
        # print(graus)
        # se o índice for menor ou igual a d, o grau de pertinência é o próprio índice
        if i <= d:
            graus[i] = i
        # se o índice for maior do que d, o grau de pertinência é o valor máximo diminuído pela diferença entre o índice e d
        else:
            graus[i] = maximo - (i - d)
    return graus

# exemplo
d = 30
graus = fuzzy(d)

indices = list(range(-d, d+1))

# gráfico
plt.plot(indices, graus)
plt.xlabel('Posição na vizinhança')
plt.ylabel('Grau de pertinência')
plt.title('Função triangular para vizinhança de tamanho d = {}'.format(d))
plt.show()
