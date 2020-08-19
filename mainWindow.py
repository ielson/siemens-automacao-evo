import sys
import main

from PyQt5 import QtWidgets, uic
from evoWindow import Ui_Form


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.escolherFerramenta.setVisible(False)
        self.preencherInfraLA.setVisible(False)
        self.preencherInfraTE.setVisible(False)
        self.preencherPSILA.setVisible(False)
        self.preencherPSITE.setVisible(False)
        self.avisoFerramenta.setVisible(False)
        self.infraNotOk.toggled.connect(self.checkButtonInfra)
        self.PSI.toggled.connect(self.checkButtonPSI)
        self.ferramentaUtilizada.toggled.connect(self.checkButtonFerramenta)
        self.copiarRelatorio.clicked.connect(self.buttonCopiar)
        self.infra = "Ok"
        self.psi = "Ok"
        self.situacao = "Finalizado"

       

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
            self.preencherPSITE.setVisible(True)
            self.preencherPSILA.setVisible(True)
            self.psi = "Not Ok"
        else:
            self.preencherPSITE.setVisible(False)
            self.preencherPSILA.setVisible(False)
            self.psi = "Ok"

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
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(texto)
        print(texto)

    def getInfra(self):
        if self.infra == "Not Ok":
            self.infra = self.preencherInfraTE.toPlainText()
        return self.infra

    def getPsi(self):
        if self.psi == "Not Ok":
            self.psi = self.preencherPSITE.toPlainText()
        return self.psi





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
