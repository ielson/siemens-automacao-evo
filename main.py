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
import os

class Relatorio:
    ''' Classe para armazenar os objetos dos relatórios'''

    def __init__(self, area='imagem'):
        self.area = area

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_tipo(self, tipo):
        self.tipo = tipo

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
        
    def set_ferramentasEspeciais(self, ferramentasEspeciais):
        self.ferramentasEspeciais = ferramentasEspeciais
        print("ferramentas especiais setadas no main")

    def set_tipoProblema(self, tipoProblema):
        self.tipoProblema = tipoProblema

    def set_planoAcao(self, planoAcao):
        self.planoAcao = planoAcao

    def set_tempoPrevisto(self, tempoPrevisto):
        self.tempoPrevisto = tempoPrevisto

    def set_complexidade(self, complexidade):
        self.complexidade = complexidade
    
    def set_pecasTeste(self, pecasTeste):
        self.pecasTeste = pecasTeste

    def set_pecasProxAtend(self, pecasProxAtend):
        self.pecasProxAtend = pecasProxAtend

    def set_pecasIndispensaveis(self, pecasIndispensaveis):
        self.pecasIndispensaveis = pecasIndispensaveis

    def contar_espacos(self):
        pass

    def completar_espacos(self):
        pass

    def gerar_texto(self):
        if self.situacao == "Finalizado":
            with open("modeloEncerramento.txt", encoding='latin-1') as arquivo:
                modelo = Template(arquivo.read())
            self.dados = dict(descricao = self.descricao, procedimentos = self.procedimentos, infraestrutura = self.infraestrutura, conclusao=self.situacao, psi1=self.psi1, psi2=self.psi2, psi3=self.psi3, psi4=self.psi4, psi5=self.psi5, pecas=self.pecas, instrumentos=self.ferramentas, tipo=self.tipo)
        if self.situacao == "Não finalizado":
            print("followup")
            with open("modeloFollowup.txt", encoding='latin-1') as arquivo:
                modelo = Template(arquivo.read())
            self.dados = dict(descricao = self.descricao, procedimentos = self.procedimentos, infraestrutura = self.infraestrutura, conclusao=self.situacao, psi1=self.psi1, psi2=self.psi2, psi3=self.psi3, psi4=self.psi4, psi5=self.psi5, pecas=self.pecas, instrumentos=self.ferramentas, tipo=self.tipo, tipoProblema=self.tipoProblema, planoAcao=self.planoAcao, tempoPrevisto=self.tempoPrevisto, ferramentasEspeciais=self.ferramentasEspeciais, complexidadeAtendimento=self.complexidade, pecasTeste=self.pecasTeste, pecasProximoAtendimento=self.pecasProxAtend, pecasIndispensaveis=self.pecasIndispensaveis)
        self.relatorio = modelo.substitute(self.dados)
        caracteres = self.contador_caracteres()
        return(self.relatorio, caracteres)
        
    def salvar_texto(self):
        for relatorioNum in range(3, 1, -1):
            if not os.path.exists("relatorio{}.txt".format(relatorioNum-1)):
                with open("relatorio{}.txt".format(relatorioNum-1), "w"):
                    pass
            try:
                with open("relatorio{}.txt".format(relatorioNum - 1 ), "r", encoding="latin-1") as relatorioOriginal:
                    dados_antigos = json.loads(relatorioOriginal.read())
                    print("relatorio original copiado")
                with open("relatorio{}.txt".format(relatorioNum), "w", encoding="latin-1") as relatorioMovido:
                    json_str_movida = json.dumps(dados_antigos, indent=4)
                    print(json_str_movida, file=relatorioMovido)
                    print("relatorio movido")
            except json.decoder.JSONDecodeError:
                    print("Erro do json, relatorio: {}".format(relatorioNum-1))
        with open("relatorio1.txt", "w", encoding="latin-1") as relatorioNovo:
            json_str = json.dumps(self.dados, indent=4)
            print(json_str, file=relatorioNovo)
            print("relatório salvo")

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
            
