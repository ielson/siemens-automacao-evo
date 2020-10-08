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
from string import Template
import json

class Relatorio:
    ''' Classe para armazenar os objetos dos relatórios'''

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
        # * to unpack the tuple
        #  self.psi = psi_padrao.format(*psi)
        self.psi1 = psi[0]
        self.psi2 = psi[1]
        self.psi3 = psi[2]
        self.psi4 = psi[3]
        self.psi5 = psi[4]

    def set_pecas(self, pecas):
        self.pecas = pecas

    def set_ferramentas(self, ferramentas):
        self.ferramentas = ferramentas

    def contar_espacos(self):
        pass

    def completar_espacos(self):
        pass

    def gerar_texto(self, followup):
        if not followup:
            with open("modeloEncerramento.txt", encoding='latin-1') as arquivo:
                modelo = Template(arquivo.read())
            dados = dict(descricao = self.descricao, procedimentos = self.procedimentos, infraestrutura = self.infraestrutura, conclusao=self.situacao, psi1=self.psi1, psi2=self.psi2, psi3=self.psi3, psi4=self.psi4, psi5=self.psi5, pecas=self.pecas, instrumentos=self.ferramentas)
            self.relatorio = modelo.substitute(dados)
            caracteres = self.contador_caracteres()
            with open("relatorio1.txt", "w", encoding="latin-1") as relatorioSalvo:
                json_str = json.dumps(dados, indent=4)
                print(json_str, file=relatorioSalvo)
        return(self.relatorio, caracteres)
        
    def contador_caracteres(self):
    # Tenho que arrumar aqui, se não vai ficar abrindo o arquivo toda vez que o contador for chamado, que vão ser muitas
        #if not followup:
        visivelCliente = self.relatorio.split('*')[0]
        print('visivel cliente: {}'.format(visivelCliente))
        print('tamanho: {}'.format(len(visivelCliente)))
        return visivelCliente

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
    print(relatorio)
    relatorio1.copy2clip(relatorio)


if __name__ == "__main__":
    import sys
    main(sys.argv)
            
