
def arbol_binario(arbol):
    """
    Devuelve el mayor valor almacenado en el árbol binario del ejercicio 8

    """
    mayor = arbol[0]

    for nodo in arbol:
        if type(nodo) == int:
            if nodo >= mayor:
                mayor = nodo
        elif type(nodo) == list and nodo != []:
            mayor_nodo = arbol_binario(nodo)
            if mayor_nodo >= mayor:
                mayor = mayor_nodo
            
    
    return mayor


arbol =  [1,
  [7,
    [2,
      [],
      []],
    [6, 
      [5,
        [],
        []],
      [11,
        [],
        []]]],
    [9,
      [],
      [9, 
        [5,
          [],
          []],
        []]]]


print(arbol_binario(arbol))