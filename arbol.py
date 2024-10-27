class Nodo:

    def __init__(self, valor, nodo_izquierdo, nodo_derecho):
        self.valor = valor
        self.nodo_izquierdo = nodo_izquierdo
        self.nodo_derecho = nodo_derecho

    def __repr__(self):
        return f'[{self.valor}, {self.nodo_izquierdo}, {self.nodo_derecho}]'
    
    def buscar(self, numero):
        if self.valor == numero:
            resultado = self
            return resultado
        elif numero < self.valor:
            if isinstance(self.nodo_izquierdo,Nodo):
                resultado = self.nodo_izquierdo.buscar(numero)
                return resultado
        elif isinstance(self.nodo_derecho,Nodo):
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
    print(nodo1)
    buscar = nodo1.buscar(4)
    print(buscar)
    insertar1 = nodo1.insertar(7)
    print(insertar1)
    nodo2 = Nodo(5,[],[])
    insertar2 = nodo2.insertar(3)
    print(insertar2)

        