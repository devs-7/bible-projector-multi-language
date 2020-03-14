# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programming\GitHub\Bible-projector\python\ui\main\window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pesquisarButton = QtWidgets.QPushButton(self.centralwidget)
        self.pesquisarButton.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: gray;\n"
"    color: white;\n"
"}")
        self.pesquisarButton.setObjectName("pesquisarButton")
        self.gridLayout.addWidget(self.pesquisarButton, 0, 1, 1, 1)
        self.pesquisaLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pesquisaLineEdit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pesquisaLineEdit.setObjectName("pesquisaLineEdit")
        self.gridLayout.addWidget(self.pesquisaLineEdit, 0, 0, 1, 1)
        self.projetarButton = QtWidgets.QPushButton(self.centralwidget)
        self.projetarButton.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: gray;\n"
"    color: white;\n"
"}")
        self.projetarButton.setObjectName("projetarButton")
        self.gridLayout.addWidget(self.projetarButton, 0, 2, 1, 1)
        self.mainTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.mainTextEdit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.mainTextEdit.setObjectName("mainTextEdit")
        self.gridLayout.addWidget(self.mainTextEdit, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor bíblico"))
        self.pesquisarButton.setText(_translate("MainWindow", "Pesquisar"))
        self.projetarButton.setText(_translate("MainWindow", "Projetar"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
