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
        MainWindow.resize(665, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
        self.horizontalLayout_3.addWidget(self.pesquisaLineEdit)
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
        self.horizontalLayout_3.addWidget(self.pesquisarButton)
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
        self.horizontalLayout_3.addWidget(self.projetarButton)
        self.atualizarButton = QtWidgets.QPushButton(self.centralwidget)
        self.atualizarButton.setStyleSheet("* {\n"
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
        self.atualizarButton.setObjectName("atualizarButton")
        self.horizontalLayout_3.addWidget(self.atualizarButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mainTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainTextEdit.sizePolicy().hasHeightForWidth())
        self.mainTextEdit.setSizePolicy(sizePolicy)
        self.mainTextEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.mainTextEdit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.mainTextEdit.setObjectName("mainTextEdit")
        self.gridLayout.addWidget(self.mainTextEdit, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.listView.setStyleSheet("*{\n"
"    width: 100px;\n"
"}")
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 1, 2, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
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
        self.atualizarButton.setText(_translate("MainWindow", "Atualizar"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
