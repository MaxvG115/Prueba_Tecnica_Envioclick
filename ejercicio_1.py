# Se va a utilizar el algoritmo kmp para resolver este problema

def compute_prefix(word):
    m = len(word)
    pi = [0] * m # Funcion de prefijos
    k = 0 # Variable para almacenar la longitud del prefijo más largo

    # Iterar sobre cada carácter de la palabra, excepto el primero
    for i in range(1, m):
        while k > 0 and word[k] != word[i]:
            k = pi[k - 1] # Actualizar k usando el valor previo de pi
        if word[k] == word[i]:
            k += 1
        pi[i] = k # Almacenar el valor de k en pi[i]

    return pi


def kmp_search(word, paragraph):