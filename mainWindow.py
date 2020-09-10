import sys
import main

from PyQt5 import QtWidgets, uic
from evoWindow import Ui_Form
from chooseWindow import Ui_MainWindow


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
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
        self.avisoFerramenta.setVisible(False)
        self.infraNotOk.toggled.connect(self.checkButtonInfra)
        self.PSI.toggled.connect(self.checkButtonPSI)
        self.ferramentaUtilizada.toggled.connect(self.checkButtonFerramenta)
        self.copiarRelatorio.clicked.connect(self.buttonCopiar)
        self.infra = "Ok"
        self.psi = "Ok"
        self.situacao = "Finalizado"
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.tipoCB.activated[str].connect(self.tipoEscolhido)
       

    def checkButtonInfra(self):
        if self.infraNotOk.isChecked() == True:
            self.preencherInfraTE.setVisible(True)
            self.preencherInfraLA.setVisible(True)
            self.infra = "Not Ok"
        else:
            self.preencherInfraTE.setVisible(False)
            self.preencherInfraLA.setVisible(False)
            self.infra = "Ok"

    def checkButtonPSI(self):
        if self.PSI.isChecked() == True:
            self.preencherPSILA.setVisible(True)
            self.psi = "Not Ok"
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
            self.resize(880, 1024)
        else:
            self.preencherPSILA.setVisible(False)
            self.psi = "Ok"
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

    def checkButtonFerramenta(self):
        if self.ferramentaUtilizada.isChecked() == True:
            self.escolherFerramenta.setVisible(True)
            self.avisoFerramenta.setVisible(True)
        else:
            self.escolherFerramenta.setVisible(False)
            self.avisoFerramenta.setVisible(False)

    def checkButtonFollowUp(self):
        if self.necessarioFollowUp.isChecked():
            self.situacao = "Não finalizado"
        else:
            self.situacao = "Finalizado"
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
        texto = novoRelatorio.gerar_texto()

        self.clipboard.setText(texto)
        print(texto)

    def getInfra(self):
        if self.infra == "Not Ok":
            self.infra = self.preencherInfraTE.toPlainText()
        return self.infra

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
            psi5 = 'Não'
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
