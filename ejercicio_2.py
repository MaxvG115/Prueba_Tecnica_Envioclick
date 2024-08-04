from input import entry

def sort_by_priority(entry, criteria):

    def merge_sort(arr, key, reverse=False):
        if len(arr) > 1:
            mid = len(arr) // 2 # Encontrar el punto medio para dividir el arreglo en dos mitades
            left_half = arr[:mid] # Subarreglo izquierdo
            right_half = arr[mid:] # Subarreglo derecho

            # Ordenar recursivamente ambas mitades
            merge_sort(left_half, key, reverse)
            merge_sort(right_half, key, reverse)

            # Índices para recorrer las mitades y el arreglo principal
            i = j = k = 0

            # Combinar las dos mitades en el arreglo principal
            while i < len(left_half) and j < len(right_half):
                # Comparar elementos de las mitades basados en el valor de `key`
                if (not reverse and left_half[i][key] < right_half[j][key]) or (reverse and left_half[i][key] > right_half[j][key]):
                    arr[k] = left_half[i] # Añadir el elemento de la mitad izquierda
                    i += 1
                else:
                    arr[k] = right_half[j] # Añadir el elemento de la mitad derecha
                    j += 1
                k += 1
            
            # Añadir los elementos restantes de la mitad izquierda, si los hay
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Añadir los elementos restantes de la mitad derecha, si los hay
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
                
        # Devolver el arreglo ordenado
        return arr
    
    
    
    