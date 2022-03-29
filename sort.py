import random

# Implementação do MergeSort "na raça", seguindo apenas a explicação da aula 19
def MergeSort(array):
    n = len(array)
    # Caso mínimo da recursão
    if (n == 1):
        return(array)
    else:
        # 1) Dividir o array em duas metades
        primeira_metade = array[0 : n//2]
        segunda_metade = array[n//2 : n]

        # 2) Ordenar cada metade recursivamente
        primeira_metade = MergeSort(primeira_metade)
        segunda_metade = MergeSort(segunda_metade)

        # 3) Merjar as metades ordenadas em tempo linear
        array_ordenado = []
        n = len(primeira_metade)
        m = len(segunda_metade)
        i = 0 # Indicador 'smallest' da primeira metade
        j = 0 # Indicador 'smallest' da segunda metade
        while (i < n) or (j < m):
            if (i < n) and (j < m): # Caso básico
                if (primeira_metade[i] < segunda_metade[j]):
                    array_ordenado.append(primeira_metade[i])
                    i += 1
                else:
                    array_ordenado.append(segunda_metade[j])
                    j += 1
            elif (i >= n) and (j < m): # Indicador da primeira metade estourado
                array_ordenado.append(segunda_metade[j])
                j += 1
            else: # Indicador da segunda metade estourado
                array_ordenado.append(primeira_metade[i])
                i += 1
        return(array_ordenado)


# Implementação do BubbleSort, seguindo a definição
def BubbleSort(array):
    n = len(array)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(n-1):
            if array[i] > array[i+1]:
                ordenado = False
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array