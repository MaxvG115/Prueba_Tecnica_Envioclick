# Prueba_Tecnica_Envioclick

Este repositorio contiene soluciones a una prueba técnica que aborda dos ejercicios prácticos. A continuación, se proporciona una descripción general de cada solución, los requisitos y cómo ejecutarlos.

## Contenido del Repositorio

### `ejercicio_1.py`

Este archivo contiene la implementación del algoritmo Knuth-Morris-Pratt (KMP) para la búsqueda de subcadenas. Incluye dos funciones principales:

- **`compute_prefix(word)`**: Calcula la tabla de prefijos para el algoritmo KMP.
- **`kmp_search(word, paragraph)`**: Busca todas las ocurrencias de una palabra en un párrafo usando el algoritmo KMP.

### `ejercicio_2.py`

Este archivo implementa una función de ordenamiento personalizado utilizando el algoritmo Merge Sort. La función principal es:

- **`sort_by_priority(entry, criteria)`**: Ordena una lista de elementos por prioridad, aplicando filtros basados en criterios específicos.

### `entry.py`

Contiene una lista de diccionarios que representa los datos de entrada para el segundo ejercicio.

## Requisitos

- Python 3

## Ejecución

Para ejecutar los archivos, sigue estos pasos:

1. **Clona el repositorio**:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. **Ejecuta los ejercicios**:

    - Para ejecutar el primer ejercicio:

        ```bash
        python ejercicio_1.py
        ```

    - Para ejecutar el segundo ejercicio:

        ```bash
        python ejercicio_2.py
        ```
