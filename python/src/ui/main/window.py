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
        MainWindow.resize(709, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.versoesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.versoesComboBox.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    width: 30px\n"
"}")
        self.versoesComboBox.setObjectName("versoesComboBox")
        self.horizontalLayout_3.addWidget(self.versoesComboBox)
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
        self.pesquisarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.projetarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.atualizarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.configuracoesButton = QtWidgets.QPushButton(self.centralwidget)
        self.configuracoesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configuracoesButton.setStyleSheet("* {\n"
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
        self.configuracoesButton.setObjectName("configuracoesButton")
        self.horizontalLayout_3.addWidget(self.configuracoesButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 3, 0, 1, 1)
        self.ocorrenciasListView = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ocorrenciasListView.sizePolicy().hasHeightForWidth())
        self.ocorrenciasListView.setSizePolicy(sizePolicy)
        self.ocorrenciasListView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.ocorrenciasListView.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"*:item {\n"
"    margin-bottom: 10px;\n"
"}")
        self.ocorrenciasListView.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.ocorrenciasListView.setWordWrap(True)
        self.ocorrenciasListView.setObjectName("ocorrenciasListView")
        self.gridLayout.addWidget(self.ocorrenciasListView, 1, 3, 3, 1)
        self.ocorrenciasLabel = QtWidgets.QLabel(self.centralwidget)
        self.ocorrenciasLabel.setStyleSheet("")
        self.ocorrenciasLabel.setObjectName("ocorrenciasLabel")
        self.gridLayout.addWidget(self.ocorrenciasLabel, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
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
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.mainTextEdit.setObjectName("mainTextEdit")
        self.gridLayout.addWidget(self.mainTextEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
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
        self.configuracoesButton.setText(_translate("MainWindow", "Configurações"))
        self.ocorrenciasLabel.setText(_translate("MainWindow", "Ocorrências"))
        self.label_3.setText(_translate("MainWindow", "Capítulo"))
        self.label_2.setText(_translate("MainWindow", "Pré-visualização"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
