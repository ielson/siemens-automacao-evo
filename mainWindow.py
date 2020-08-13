import sys

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
        self.infraNotOk.toggled.connect(self.checkButtonInfra)
        self.PSI.toggled.connect(self.checkButtonPSI)
        self.ferramentaUtilizada.toggled.connect(self.checkButtonFerramenta)
        


    def checkButtonInfra(self):
        if self.infraNotOk.isChecked() == True:
            self.preencherInfraTE.setVisible(True)
            self.preencherInfraLA.setVisible(True)
        else:
            self.preencherInfraTE.setVisible(False)
            self.preencherInfraLA.setVisible(False)

    def checkButtonPSI(self):
        if self.PSI.isChecked() == True:
            self.preencherPSITE.setVisible(True)
            self.preencherPSILA.setVisible(True)
        else:
            self.preencherPSITE.setVisible(False)
            self.preencherPSILA.setVisible(False)

    def checkButtonFerramenta(self):
        if self.ferramentaUtilizada.isChecked() == True:
            self.escolherFerramenta.setVisible(True)
        else:
            self.escolherFerramenta.setVisible(False)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
