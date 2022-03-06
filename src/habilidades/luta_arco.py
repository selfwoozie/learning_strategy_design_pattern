from .interfaces import Ihabilidade


class LutaFlexa(Ihabilidade):
    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Atirar flexas!")

    def nivel_atributo(self):
        print('Nível de uso Arco {}'.format(self.nivel))
