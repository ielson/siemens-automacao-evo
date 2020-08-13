import sys

from PyQt5 import QtWidgets, uic
from evoWindow import Ui_Form

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.escolherFerramenta.setVisible(False)
        self.preencherInfra.setVisible(False)
        self.preencherPSI.setVisible(False)
        self.infraNotOk.toggled.connect(self.checkButton)


    def checkButton(self):
        print("button pressed")
        if self.infraNotOk.isChecked() == True:
            self.preencherInfra.setVisible(True)
        else:
            self.preencherInfra.setVisible(False)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
