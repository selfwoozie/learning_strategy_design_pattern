from .interfaces import Ihabilidade


class LutaEspada(Ihabilidade):
    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Lutar com espadas!")

    def nivel_atributo(self):
        print('Nível de uso Espada {}'.format(self.nivel))
