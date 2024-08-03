# Se va a utilizar el algoritmo kmp para resolver este problema

def compute_prefix(word):
    m = len(word)
    pi = [0] * m # Tabla de prefijos
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
    n = len(paragraph)
    m = len(word)
    pi = compute_prefix(word) # Calculo de tabla de prefijos
    q = 0 # Progreso de la coincidencia
    ocurrences = 0

    # Iterar sobre cada carácter del párrafo
    for i in range(n):
        while q > 0 and word[q] != paragraph[i]:
            q = pi[q - 1] # Actualizar q usando el valor previo de pi

        if word[q] == paragraph[i]:
            q += 1

        # Si q es igual a la longitud de la palabra, se ha encontrado una ocurrencia
        if q == m:
            ocurrences += 1 # Incrementar el contador de ocurrencias
            q = pi[q - 1]
    
    return ocurrences

