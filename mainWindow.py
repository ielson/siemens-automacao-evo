import sys
import main
import json
import os

from PyQt5 import QtWidgets, uic
from evoWindow import Ui_Sigame
from chooseWindow import Ui_MainWindow
from adicionarFerramentaUI import Ui_Dialog


class FerramentaDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(FerramentaDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.criarFerramenta)
        self.buttonBox.rejected.connect(self.fecharDialog)
        self.parent = parent

    def criarFerramenta(self):
        print("ferramenta criada")
        ferramenta = (self.nomeFerramentaTE.toPlainText().strip('\n'), 
                    self.matriculaSAPTE.toPlainText(),
                    self.validadeCertificadoDE.date().toString("dd/MM/yyyy"))
        print(ferramenta)
        self.parent.ferramentasUtilizadas.append(ferramenta)
        self.parent.escolherFerramenta.addItem("{} - {}".format(ferramenta[1], ferramenta[0]))
        self.parent.escolherFerramenta.setCurrentIndex(self.parent.escolherFerramenta.count()-1)
        with open("ferramentas.json", "w+", encoding='utf-8') as ferramentasFile:
            # assim só vai salvar uma, lembrar de mudar depois 
            # pickle.dump(ferramenta, ferramentasFile)
            json.dump(self.parent.ferramentasUtilizadas, ferramentasFile)

    def fecharDialog(self):
        print("fechando dialog")



class MainWindow(QtWidgets.QWidget, Ui_Sigame):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.resize(615, 930)
        self.escolherFerramenta.setVisible(False)
        self.preencherInfraLA.setVisible(False)
        self.preencherInfraTE.setVisible(False)
        self.preencherPSILA.setVisible(False)
        self.psi1LA.setVisible(False)
        self.psi1CB.setVisible(False)
        self.psi2LA.setVisible(False)
        self.psi2CB.setVisible(False)
        self.psi3LA.setVisible(False)
        self.psi3CB.setVisible(False)
        self.psi4LA.setVisible(False)
        self.psi4TE.setVisible(False)
        self.psi5LA.setVisible(False)
        self.psi5CB.setVisible(False)
        self.pecasTE.setVisible(False)
        self.pecasLA.setVisible(False)
        self.tipoProblemaLA.setVisible(False)
        self.tipoProblemaRB1.setVisible(False)
        self.tipoProblemaRB2.setVisible(False)
        self.tipoProblemaRB3.setVisible(False)
        self.planoAcaoLA.setVisible(False)
        self.planoAcaoTE.setVisible(False)
        self.tempoLA.setVisible(False)
        self.tempoTE.setVisible(False)
        self.ferramentasEspeciaisLA.setVisible(False)
        self.ferramentasEspeciaisTE.setVisible(False)
        self.complexidadeCB.setVisible(False)
        self.complexidadeLA.setVisible(False)
        self.pecasTesteLA.setVisible(False)
        self.pecasTesteTE.setVisible(False)
        self.pecasSolicitadasLA.setVisible(False)
        self.pecasSolicitadasTE.setVisible(False)
        self.indisponibilidadeLA.setVisible(False)
        self.indisponibilidadeTE.setVisible(False)
        self.avisoFerramenta.setVisible(False)
        self.infraNotOk.toggled.connect(self.checkButtonInfra)
        self.PSI.toggled.connect(self.checkButtonPSI)
        self.ferramentaUtilizada.toggled.connect(self.checkButtonFerramenta)
        self.necessarioFollowUp.toggled.connect(self.checkButtonFollowUp)
        self.copiarRelatorio.clicked.connect(self.buttonCopiar)
        self.pecasCB.toggled.connect(self.checkButtonPecas)
        self.escolherFerramenta.activated[str].connect(self.checkEscolherFerramentas)
        self.psi = "Ok"
        self.situacao = "Finalizado"
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.tipoCB.activated[str].connect(self.tipoEscolhido)
        self.ferramentasUtilizadas = []
        if os.path.isfile('ferramentas.json'):
            with open('ferramentas.json', 'r') as ferramentasFile:
                ferramentas = json.load(ferramentasFile)
                for ferramentaSalva in ferramentas:
                    # self.adicionarFerramenta()
                    print("uma ferramenta: {}".format(ferramentaSalva))
                    self.ferramentasUtilizadas.append(ferramentaSalva)
                    self.escolherFerramenta.addItem("{} - {}".format(ferramentaSalva[1], ferramentaSalva[0]))

    def checkButtonInfra(self):
        if self.infraNotOk.isChecked() == True:
            self.preencherInfraTE.setVisible(True)
            self.preencherInfraLA.setVisible(True)
            print('infra not ok')
        else:
            self.preencherInfraTE.setVisible(False)
            self.preencherInfraLA.setVisible(False)

    def checkEscolherFerramentas(self, ferramenta):
        if ferramenta == "Adicionar nova ferramenta":
            print("Nova ferramenta a ser adicionada")
            addFerramentaDiag = FerramentaDialog(self)
            addFerramentaDiag.exec_()
        else:
            print(ferramenta)

           
            
    
    def checkButtonPecas(self):
        if self.pecasCB.isChecked():
            self.pecasTE.setVisible(True)
            self.pecasLA.setVisible(True)
        else:
            self.pecasTE.setVisible(False)
            self.pecasLA.setVisible(False)

    def checkButtonPSI(self):
        if self.PSI.isChecked() == True:
            self.preencherPSILA.setVisible(True)
            self.psi1LA.setVisible(True)
            self.psi1CB.setVisible(True)
            self.psi2LA.setVisible(True)
            self.psi2CB.setVisible(True)
            self.psi3LA.setVisible(True)
            self.psi3CB.setVisible(True)
            self.psi4LA.setVisible(True)
            self.psi4TE.setVisible(True)
            self.psi5LA.setVisible(True)
            self.psi5CB.setVisible(True)
            self.resize(615, 930)
            self.pecasCB.setStyleSheet("margin-left:400%")
        else:
            self.preencherPSILA.setVisible(False)
            self.psi1LA.setVisible(False)
            self.psi1CB.setVisible(False)
            self.psi2LA.setVisible(False)
            self.psi2CB.setVisible(False)
            self.psi3LA.setVisible(False)
            self.psi3CB.setVisible(False)
            self.psi4LA.setVisible(False)
            self.psi4TE.setVisible(False)
            self.psi5LA.setVisible(False)
            self.psi5CB.setVisible(False)
            self.resize(480, 826)
            self.pecasCB.setStyleSheet("margin-left:200%")

    def checkButtonFerramenta(self):
        if self.ferramentaUtilizada.isChecked() == True:
            self.escolherFerramenta.setVisible(True)
            self.avisoFerramenta.setVisible(True)
        else:
            self.escolherFerramenta.setVisible(False)
            self.avisoFerramenta.setVisible(False)

    def checkButtonFollowUp(self):
        if self.necessarioFollowUp.isChecked() == False:
            self.pecasTE.setVisible(False)
            self.pecasLA.setVisible(False)
            self.tipoProblemaLA.setVisible(False)
            self.tipoProblemaRB1.setVisible(False)
            self.tipoProblemaRB2.setVisible(False)
            self.tipoProblemaRB3.setVisible(False)
            self.planoAcaoLA.setVisible(False)
            self.planoAcaoTE.setVisible(False)
            self.tempoLA.setVisible(False)
            self.tempoTE.setVisible(False)
            self.ferramentasEspeciaisLA.setVisible(False)
            self.ferramentasEspeciaisTE.setVisible(False)
            self.complexidadeCB.setVisible(False)
            self.complexidadeLA.setVisible(False)
            self.pecasTesteLA.setVisible(False)
            self.pecasTesteTE.setVisible(False)
            self.pecasSolicitadasLA.setVisible(False)
            self.pecasSolicitadasTE.setVisible(False)
            self.indisponibilidadeLA.setVisible(False)
            self.indisponibilidadeTE.setVisible(False)
        else:
            self.pecasTE.setVisible(True)
            self.pecasLA.setVisible(True)
            self.tipoProblemaLA.setVisible(True)
            self.tipoProblemaRB1.setVisible(True)
            self.tipoProblemaRB2.setVisible(True)
            self.tipoProblemaRB3.setVisible(True)
            self.planoAcaoLA.setVisible(True)
            self.planoAcaoTE.setVisible(True)
            self.tempoLA.setVisible(True)
            self.tempoTE.setVisible(True)
            self.ferramentasEspeciaisLA.setVisible(True)
            self.ferramentasEspeciaisTE.setVisible(True)
            self.complexidadeCB.setVisible(True)
            self.complexidadeLA.setVisible(True)
            self.pecasTesteLA.setVisible(True)
            self.pecasTesteTE.setVisible(True)
            self.pecasSolicitadasLA.setVisible(True)
            self.pecasSolicitadasTE.setVisible(True)
            self.indisponibilidadeLA.setVisible(True)
            self.indisponibilidadeTE.setVisible(True)
        self.situacao = 'finalizado'
        return self.situacao

    def buttonCopiar(self):
        area =  "imagem"
        tipo = self.tipoCB.currentText()
        novoRelatorio = main.Relatorio(area, tipo)
        novoRelatorio.set_descricao(self.descricaoTE.toPlainText())
        novoRelatorio.set_procedimentos(self.procedimentosTE.toPlainText())
        novoRelatorio.set_infraestrutura(self.getInfra())
        novoRelatorio.set_situacao(self.checkButtonFollowUp())
        novoRelatorio.set_psi(self.getPsi())
        novoRelatorio.set_pecas(self.getPecas())
        novoRelatorio.set_ferramentas(self.getFerramentas())
        texto = novoRelatorio.gerar_texto(False)

        self.clipboard.setText(texto)
        print(texto)

    def getInfra(self):
        # if self.infra == "Not Ok":
        if self.preencherInfraTE.toPlainText() == '':
            print('sem problemas de infra relatados')
            self.infra = "Ok"
        else:
            print('mudando infra')
            print(self.preencherInfraTE.toPlainText())
            self.infra = self.preencherInfraTE.toPlainText()
        return self.infra
        
    def getFerramentas(self):
        if self.escolherFerramenta.currentText() == "Adicionar nova ferramenta":
           print ('não Aplicável')
           return "Não Aplicável"
        else:
            print(self.escolherFerramenta.currentText())
            return(self.escolherFerramenta.currentText())
            


    def getPecas(self):
        if self.pecasTE.toPlainText() == '':
            return('Nenhuma')
        else:
            return self.pecasTE.toPlainText()

    def getPsi(self):
        if self.psi1CB.isChecked() == True:
            psi1 = "Sim"
        else:
            psi1 = 'Não'
        if self.psi2CB.isChecked() == True:
            psi2 = "Sim"
        else:
            psi2 = 'Não'
        if self.psi3CB.isChecked() == True:
            psi3 = "Sim"
        else:
            psi3 = 'Não'
        psi4 = self.psi4TE.toPlainText()
        if psi4=="":
            psi4='Não Aplicável'
        if self.psi5CB.isChecked() == True:
            psi5 = "Sim"
        else:
            psi5 = 'Não Aplicável'
        self.psi = (psi1, psi2, psi3, psi4, psi5)
        return self.psi

    def tipoEscolhido(self, tipo):
        if tipo == "Preventiva":
            texto_preventiva = '''Houve a troca de algum kit?
Qual o nível atual de hélio da máquina?
Houve algum ERDU Short nos últimos 2 meses? '''
            self.procedimentosTE.setPlainText(texto_preventiva)

class ChooserWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(ChooserWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.scriptPB.clicked.connect(self.mostrarScript)
        
    def mostrarScript(self):
        self.novaJanela = MainWindow()
        self.novaJanela.show()
        print("mostrarJanela") 

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
