class Nodo:

    def __init__(self, valor, nodo_izquierdo, nodo_derecho):
        self.valor = valor
        self.nodo_izquierdo = nodo_izquierdo
        self.nodo_derecho = nodo_derecho
        self.coste_ultima_busqueda = 0

    def __repr__(self):
        return f'[{self.valor}, {self.nodo_izquierdo}, {self.nodo_derecho}]'
    
    def buscar(self, numero):
        self.coste_ultima_busqueda = self.coste_ultima_busqueda + 1
        if self.valor == numero:
            resultado = self
            return resultado
        elif numero < self.valor:
            if isinstance(self.nodo_izquierdo,Nodo):
                self.coste_ultima_busqueda = self.coste_ultima_busqueda + 1
                resultado = self.nodo_izquierdo.buscar(numero)
                return resultado
        elif isinstance(self.nodo_derecho,Nodo):
                self.coste_ultima_busqueda = self.coste_ultima_busqueda + 1
                resultado = self.nodo_derecho.buscar(numero)
                return resultado
        else:
            return None

    def insertar(self,num_a_insertar):
        if num_a_insertar <= self.valor:
            if self.nodo_izquierdo == []:
                self.nodo_izquierdo = num_a_insertar
            elif isinstance(self.nodo_izquierdo,Nodo):
                self.nodo_izquierdo.insertar(num_a_insertar)
        else:
            if self.nodo_derecho == []:
                self.nodo_derecho = num_a_insertar
            elif isinstance(self.nodo_derecho,Nodo):
                self.nodo_derecho.insertar(num_a_insertar)
        return self        


if __name__ == '__main__':
    nodo1 = Nodo(5, Nodo(3,[],Nodo(4,[],[])), Nodo(7,[],[]))
    buscar = nodo1.buscar(4)
    print(buscar)
    print(nodo1.coste_ultima_busqueda)
    
    insertar1 = nodo1.insertar(7)
    print(insertar1)

        