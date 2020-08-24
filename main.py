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
import subprocess
import platform

class Relatorio:
    ''' Classe para armazenar os objetos dos relatórios'''

    trouble = '<<<<<<<<< TROUBLETEXT >>>>>>>>>'
    completar= '''*****************************************************
*****************************************************
*****************************************************
*****************************************************
*****************************************************'''

    def __init__(self, area='imagem', tipo='manutencao'):
        self.area = area
        self.tipo = tipo

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_procedimentos(self, procedimentos):
        self.procedimentos = procedimentos

    def set_infraestrutura(self, infraestrutura):
        self.infraestrutura = infraestrutura

    def set_situacao(self, situacao):
        self.situacao = situacao

    def set_psi(self, psi):
        psi_padrao = '''
O Equipamento causou ou contribuiu para a morte ou grave ferimento ao usuário, paciente ou qualquer outra pessoa? {} 
Poderia o mau funcionamento do Equipamento causar a morte ou grave ferimento ao usuário, paciente ou qualquer outra pessoa caso ocorra novamente? {} 
Existe algum outro Problema Potencial de Segurança (PSI) considerando os requerimentos do GD 39? {} 
Caso se trate de um PSI inserir neste campo o Escalonamento ICDxxxx ou PMxxxx. {} 
Caso haja um problema de segurança, o cliente foi informado sobre tal problema e todos os riscos atrelados ao uso do equipamento nas condições apresentadas, tendo ele decidido se o equipamento continuará ou não em operação? {} 
        '''
        # * to unpack the tuple
        self.psi = psi_padrao.format(*psi)

    def contar_espacos(self):
        pass

    def completar_espacos(self):
        pass

    def gerar_texto(self):
        texto = "Descricao: " + self.descricao + "\n" + "Procedimentos: " + self.procedimentos  + "\n" + "Infra. do site: " + self.infraestrutura + "\n" +"Conclusão: " + self.situacao + "\n" +self.completar + '\n' + self.trouble +  self.psi 
        return(texto)

def main(args=None):
    relatorio1 = Relatorio('imagem', 'manutenção')
    descricao = input('Digite a descrição do chamado: ')
    procedimentos = input('Digite a procedimentos do chamado: ')
    infraestrutura = input('Digite a infraestrutura do chamado: ')
    situacao = input('Digite a situação do chamado: ')
    psi = input('Digite a psi do chamado: ')
    relatorio1.set_descricao(descricao)
    relatorio1.set_procedimentos(procedimentos)
    relatorio1.set_infraestrutura(infraestrutura)
    relatorio1.set_situacao(situacao)
    relatorio1.set_psi(psi)
    relatorio = relatorio1.gerar_texto()
    relatorio1.copy2clip(relatorio)


if __name__ == "__main__":
    import sys
    main(sys.argv)
            
