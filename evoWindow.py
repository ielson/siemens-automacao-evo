# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 640)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStatusTip("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_3.addWidget(self.plainTextEdit_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_4.addWidget(self.radioButton)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_6.addWidget(self.radioButton_3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_5.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_7.addWidget(self.radioButton_4)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.escolherFerramenta = QtWidgets.QComboBox(Form)
        self.escolherFerramenta.setObjectName("escolherFerramenta")
        self.escolherFerramenta.addItem("")
        self.verticalLayout_10.addWidget(self.escolherFerramenta)
        self.preencherPSI = QtWidgets.QPlainTextEdit(Form)
        self.preencherPSI.setObjectName("preencherPSI")
        self.verticalLayout_10.addWidget(self.preencherPSI)
        self.preencherInfra = QtWidgets.QPlainTextEdit(Form)
        self.preencherInfra.setObjectName("preencherInfra")
        self.verticalLayout_10.addWidget(self.preencherInfra)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Tipo"))
        self.comboBox.setToolTip(_translate("Form", "Selecione o tipo de serviço realizado"))
        self.comboBox.setCurrentText(_translate("Form", "Corretiva"))
        self.comboBox.setItemText(0, _translate("Form", "Corretiva"))
        self.comboBox.setItemText(1, _translate("Form", "Preventiva"))
        self.comboBox.setItemText(2, _translate("Form", "Update"))
        self.comboBox.setItemText(3, _translate("Form", "Viagem"))
        self.comboBox.setItemText(4, _translate("Form", "Instalação/Desinstalação"))
        self.label_2.setText(_translate("Form", "Descrição do Problema"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "Descreva o problema encontrado na máquina"))
        self.label_3.setText(_translate("Form", "Procedimentos Realizados"))
        self.label_6.setText(_translate("Form", "Ferramenta Utilizada?"))
        self.radioButton.setText(_translate("Form", "SIM"))
        self.label_5.setText(_translate("Form", "Necessário Follow-up?"))
        self.radioButton_3.setText(_translate("Form", "SIM"))
        self.label_7.setText(_translate("Form", "Problema de Segurança"))
        self.radioButton_2.setText(_translate("Form", "E&xistente"))
        self.label_4.setText(_translate("Form", "Infraestrutura"))
        self.radioButton_4.setText(_translate("Form", "Não O&k"))
        self.escolherFerramenta.setItemText(0, _translate("Form", "Adicionar ferramenta"))
