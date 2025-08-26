'''
Pega o maior valor que existe e empurrar ele para a ponta de um array, e ir fazendo isto sussetivamente, de par em par.
'''

def bubbleSort(array):
    troca = 0
    limit = len(array)
    for i in range(limit): # passar por uma lista e
        for j in range(0, limit - i -1): # fazer um novo for
            if array[j] > array[j + 1]: # compara os elementos encontrados
                array[j], array[j + 1] = array[j + 1], array[j] 
                troca += 1
    return array, troca

def bubbleSortIvoVersion(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        for j in range(0, tamanho_lista - i - 1): # o -i é porque ele não pode ir até o último elemento, que é p maior do bubble sort
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    
    return lista



numbers = [5,20,19,15,37,3,72,81]

print(bubbleSort(numbers))