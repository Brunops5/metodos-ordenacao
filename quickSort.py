def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [elemento for elemento in lista[1:] if elemento <= pivo]
        maiores = [elemento for elemento in lista[1:] if elemento > pivo]

        return quick_sort(menores) + [pivo] + quick_sort(maiores)

if __name__ == '__main__':
   minha_lista = [64, 34, 25, 12, 22, 11, 90]
minha_lista_ordenada = quick_sort(minha_lista)
print("Lista ordenada:", minha_lista_ordenada) 