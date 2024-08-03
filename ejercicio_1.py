def compute_prefix(word):
    """
    Calcula la función de prefijos (tabla de pi) para el algoritmo KMP.
    
    Args:
        word (str): La cadena para la que se calcula la función de prefijos.
    
    Returns:
        List[int]: La tabla de prefijos para la cadena dada.
    """
    m = len(word)
    pi = [0] * m  # Tabla de prefijos
    k = 0  # Longitud del prefijo más largo

    for i in range(1, m):
        while k > 0 and word[k] != word[i]:
            k = pi[k - 1]  # Actualizar k usando el valor previo de pi
        if word[k] == word[i]:
            k += 1
        pi[i] = k  # Almacenar el valor de k en pi[i]

    return pi


def kmp_search(word, paragraph):
    """
    Busca todas las ocurrencias de una palabra en un párrafo usando el algoritmo KMP.
    
    Args:
        word (str): La palabra a buscar.
        paragraph (str): El párrafo en el que se busca la palabra.
    
    Returns:
        int: El número de ocurrencias encontradas.
    """
    n = len(paragraph)
    m = len(word)
    pi = compute_prefix(word)  # Calculo de tabla de prefijos
    q = 0  # Progreso de la coincidencia
    occurrences = 0

    for i in range(n):
        while q > 0 and word[q] != paragraph[i]:
            q = pi[q - 1]  # Actualizar q usando el valor previo de pi

        if word[q] == paragraph[i]:
            q += 1

        if q == m:
            occurrences += 1  # Incrementar el contador de ocurrencias
            q = pi[q - 1]
    
    return occurrences

# Casos de prueba

# Parrafo con 4 ocurrencias de la palabra logística
paragraph1 = (
    """La logística Digital es un concepto que surge de la integración entre la logística
    tradicional y la era digital. Con el auge del correo electrónico y las descargas digitales
    reemplazando productos físicos, podríamos estar hablando de un golpe devastador para la
    industria de la logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la
    logística ha introducido las innovaciones digitales."""
)

# Parrafo con 10 ocurrencias de la palabra logística
paragraph2 = (
    """La logística es un aspecto crucial en cualquier operación de logística moderna. En el mundo
    actual, la logística se ha convertido en un factor determinante para el éxito de las empresas.
    La gestión de la logística implica coordinar y optimizar todos los aspectos de la cadena de
    suministro. Para mejorar la eficiencia, las empresas invierten en tecnología avanzada para su
    logística. La logística internacional también juega un papel importante en el comercio global.
    La planificación estratégica de la logística ayuda a minimizar costos y maximizar beneficios.
    Además, la logística de última milla es fundamental para la satisfacción del cliente. En resumen,
    la logística adecuada puede marcar la diferencia en el rendimiento de cualquier organización.
    La eficiencia en logística es clave para mantener la competitividad en el mercado actual."""
)

word1 = "logística"

# Parrafo con 5 ocurrencias de la palabra alimento
paragraph3 = (
    """El alimento es esencial para la salud y el bienestar de cualquier ser vivo. Elegir un alimento
    nutritivo puede tener un impacto significativo en nuestra energía diaria. Los estudios han demostrado
    que una dieta equilibrada, rica en alimentos frescos, puede mejorar la calidad de vida. Además, es
    importante asegurarse de que el alimento que consumimos sea seguro y libre de contaminantes. Un buen
    plan de nutrición debe incluir una variedad de alimentos para satisfacer todas las necesidades del cuerpo."""
)

word2 = "alimento"

# Parrafo con 2 ocurrencias de la palabra alimento
paragraph4 = (
    """En el antiguo castillo, el guerrero empuñaba su espada con destreza, preparando su siguiente movimiento.
    La espada relucía bajo la luz del sol, mostrando su filo afilado y su historia de batallas pasadas. Cada
    golpe y cada parry eran precisos, demostrando años de entrenamiento y habilidad."""
)

word3 = "espada"

# El caso de prueba proporcionado por el documento se consigue con word1 y paragraph1
ocurrencias = kmp_search(word1, paragraph1)
print(f"{ocurrencias} ocurrencias encontradas.")