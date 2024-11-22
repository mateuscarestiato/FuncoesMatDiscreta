#Grupo: Mateus, Breno, William e Maria Giulia

#Sequência de Fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#Exemplo
n = 5
print(fibonacci(n))  #Saída: 8 (sequência: 1, 1, 2, 3, 5, 8)

#Somatório
def somatorio(arr, n):
    if n == 0:
        return 0
    return somatorio(arr, n - 1) + (arr[n - 1])

#Exemplo
arr = [2, 3, 4]
n = len(arr)
print(somatorio(arr, n))  #Saída: 9 (soma de 2 + 3 + 4)

#Produtório
def produtorio(arr, n):
    if n == 0:
        return 1
    return produtorio(arr, n - 1) * (arr[n - 1])

#Exemplo
arr = [2, 3, 4]
n = len(arr)
print(produtorio(arr, n))  #Saída: 24 (produto de 2 * 3 * 4)

#União
def uniao(conjuntos, n):
    if n == 0:
        return set()
    return uniao(conjuntos, n - 1).union(conjuntos[n - 1])

#Exemplo
conjuntos = [{1, 2}, {2, 3}, {4}]
n = len(conjuntos)
print(uniao(conjuntos, n))  #Saída: {1, 2, 3, 4}

#Interseção
def intersecao(conjuntos, n=None):
    if n is None:
        n = len(conjuntos) 
    if n == 1:
        return conjuntos[0]
    return intersecao(conjuntos, n - 1).intersection(conjuntos[n - 1])

#Exemplo
conjuntos = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
print(intersecao(conjuntos))  #Saída: {3}