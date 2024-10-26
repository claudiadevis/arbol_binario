
def arbol_binario(arbol):
    """
    Devuelve el mayor valor almacenado en el árbol binario del ejercicio 8

    """
    mayor = arbol[0]
    for nodonivel_1 in arbol:
        if type(nodonivel_1) == int:
            if nodonivel_1 >= mayor:
                mayor = nodonivel_1
        else:
            for nodonivel_2 in nodonivel_1:
                if type(nodonivel_2) == int:
                    if nodonivel_2 >= mayor:
                        mayor = nodonivel_2
                else:
                    for nodonivel_3 in nodonivel_2:
                        if type(nodonivel_3) == int:
                            if nodonivel_3 >= mayor:
                                mayor = nodonivel_3
                        else:
                            for nodonivel_4 in nodonivel_3:
                                if type(nodonivel_4) == int:
                                    if nodonivel_4 >= mayor:
                                        mayor = nodonivel_4


    return mayor


arbol = [1,
                 [7,
                  [2,
                   [],
                   []], 
                  [6,
                   [5,[],[]],
                   [11,[],[]]
                   ]],
                  [9,[],
                    [9,
                     [5,[],[]],
                     []]
                  ]]

print(arbol_binario(arbol))