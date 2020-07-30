#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Interface gráfica do programa de automatização do evo
"""

__version__ = "0.0.1"
__author__ = "Daniel Mascarenhas"
__email__ = "daniel.mascarenhas@siemens-healthineers.com"
__maintainer__ = "Daniel Mascarenhas"                         # should be the person who will fix bugs and make improvements
__copyright__ = "Copyright 2020, Siemens Healthineers"
__license__ = "GPL"
__status__ = "Prototype"                               # Prototype, Development or Production
__credits__ = ["Daniel Mascarenhas", "Gersiano Santana"]                      # also include contributors that wrote no code

# --------------------------------------------------------------------------------

# Import built-in modules first
# followed by third-party modules
# followed by any changes to the path
# your own modules.

class relatorio:
    ''' Classe para armazenar os objetos dos relatórios'''

    trouble = '<<<<<<<<< TROUBLETEXT >>>>>>>>>'
    def __init__(self, area='imagem', tipo='manutencao'):
        self.area = area
        self.tipo = tipo

    def set_descricao(descricao):
        self.descricao = descricao

    def set_procedimentos(procedimentos):
        self.procedimentos = procedimentos

    def set_infraestrutura(infraestrutura):
        self.infraestrutura = infraestrutura

    def set_situacao(situacao):
        self.situacao = situacao

    def set_psi(psi):
        self.psi = psi

    def contar_espacos():
        pass

    def completar_espacos():
        pass

def main(args=None):
    pass



if __name__ == "__main__":
    import sys
    main(sys.argv)
            
