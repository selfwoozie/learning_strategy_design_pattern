from ..habilidades import Ihabilidade
from typing import Type

class Guerreiro:
    def __init__(self, habilidade: Type[Ihabilidade]):
        self.habilidade = habilidade
    
    def acao(self):
        self.habilidade.comportamento()
    
    def attributos(self):
        self.habilidade.nivel_atributo()
