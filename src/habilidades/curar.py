from .interfaces import Ihabilidade


class Curar(Ihabilidade):
    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Curar personagem!")

    def nivel_atributo(self):
        print('Nível de cura {}'.format(self.nivel))
