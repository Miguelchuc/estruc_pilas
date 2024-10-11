import matplotlib.pyplot as plt

class pilas:
    def __init__(self, capacidad=8):
        self.C = capacidad
        self.pila = []
        self.E = []

    def agregar(self, ELE_ag):
        if len(self.pila) < self.C:
            self.pila.append(ELE_ag)
            self.guardaado()

    def eliminar(self):
        if self.pila:
            self.pila.pop()
            self.guardaado()

    def guardaado(self):
        self.E.append(list(self.pila))

    def graficar(self):
        for i, estado in enumerate(self.E):
            plt.subplot(len(self.E), 1, i + 1)
            plt.bar(range(len(estado)), [1] * len(estado), tick_label=estado)
            plt.ylim(0, 1.5)
            plt.title(f'pila {i + 1}')
            plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

pila = pilas()
pila.agregar('X')
pila.agregar('Y')
pila.eliminar()  
pila.eliminar()
pila.eliminar()  
pila.agregar('V')
pila.agregar('W')
pila.eliminar() 
pila.agregar('R')
pila.graficar()