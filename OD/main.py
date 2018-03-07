# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from cadastrar_produto import Ui_Form_produto
from cadastrar_fornecedor import Ui_Form_fornecedor
from cadastrar_usuario import Ui_Form_usuario
from consulta_produto import Ui_Form_consultaProduto
from consulta_fornecedor import Ui_Form_consultaProduto
class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1250, 800)
        Main.setMinimumSize(QtCore.QSize(1250, 800))
        Main.setMaximumSize(QtCore.QSize(1250, 800))
        self.centralWidget = QtWidgets.QWidget(Main)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1171, 591))
        self.label.setStyleSheet("image: url(:/img/img/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        Main.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1250, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuEstoque = QtWidgets.QMenu(self.menuBar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuRelat_rio = QtWidgets.QMenu(self.menuBar)
        self.menuRelat_rio.setObjectName("menuRelat_rio")
        self.menuUsuarios = QtWidgets.QMenu(self.menuBar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        self.menuForncedor = QtWidgets.QMenu(self.menuBar)
        self.menuForncedor.setObjectName("menuForncedor")
        Main.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)
        self.cadastrar_produto = QtWidgets.QAction(Main)
        self.cadastrar_produto.setObjectName("cadastrar_produto")
        self.consultar_produto = QtWidgets.QAction(Main)
        self.consultar_produto.setObjectName("consultar_produto")
        self.relatorio = QtWidgets.QAction(Main)
        self.relatorio.setObjectName("relatorio")
        self.gerenciar_usuario = QtWidgets.QAction(Main)
        self.gerenciar_usuario.setObjectName("gerenciar_usuario")
        self.actionConsultar_2 = QtWidgets.QAction(Main)
        self.actionConsultar_2.setObjectName("actionConsultar_2")
        self.bancodados = QtWidgets.QAction(Main)
        self.bancodados.setObjectName("bancodados")
        self.backup = QtWidgets.QAction(Main)
        self.backup.setObjectName("backup")
        self.actionFornecedor_CTRL_F = QtWidgets.QAction(Main)
        self.actionFornecedor_CTRL_F.setObjectName("actionFornecedor_CTRL_F")
        self.cadastrar_fornecedor = QtWidgets.QAction(Main)
        self.cadastrar_fornecedor.setObjectName("cadastrar_fornecedor")
        self.consultar_fornecedor = QtWidgets.QAction(Main)
        self.consultar_fornecedor.setObjectName("consultar_fornecedor")
        self.menuEstoque.addAction(self.cadastrar_produto)
        self.menuEstoque.addAction(self.consultar_produto)
        self.menuRelat_rio.addAction(self.relatorio)
        self.menuUsuarios.addAction(self.gerenciar_usuario)
        self.menuConfigura_es.addAction(self.bancodados)
        self.menuConfigura_es.addAction(self.backup)
        self.menuForncedor.addAction(self.cadastrar_fornecedor)
        self.menuForncedor.addAction(self.consultar_fornecedor)
        self.menuBar.addAction(self.menuEstoque.menuAction())
        self.menuBar.addAction(self.menuForncedor.menuAction())
        self.menuBar.addAction(self.menuRelat_rio.menuAction())
        self.menuBar.addAction(self.menuUsuarios.menuAction())
        self.menuBar.addAction(self.menuConfigura_es.menuAction())

        self.eventos()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)
    
    def eventos(self):
        self.cadastrar_produto.triggered.connect(self.cadastrar_p)
        self.consultar_produto.triggered.connect(self.consulta_p)
        self.cadastrar_fornecedor.triggered.connect(self.cadastrar_f)
        self.consultar_fornecedor.triggered.connect(self.consultar_f)
        self.relatorio.triggered.connect(self.relat)
        self.gerenciar_usuario.triggered.connect(self.gerenciar_u)
        self.bancodados.triggered.connect(self.bancod)
        self.backup.triggered.connect(self.backupp)

    def cadastrar_p(self):
        print("cadastrar produto")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_produto()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def consulta_p(self):
        print("consulta produto")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_consultaProduto()
        self.ui.setupUi(self.janela)
        self.janela.show()


    def cadastrar_f(self):
        print("cdastrar fornecedor")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_fornecedor()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def consultar_f(self):
        print("consulta fornecedor")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_consultaProduto()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def relat(self):
        print("relatorio")

    def gerenciar_u(self):
        print("gerenciar usuario")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_usuario()
        self.ui.setupUi(self.janela)
        self.janela.show()
        
    def bancod(self):
        print("banco de dados")
    def backupp(self):
        print("backup")

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "SISTEMA ESTOQUE-ARPROTECT"))
        self.menuEstoque.setTitle(_translate("Main", "Esto&que"))
        self.menuRelat_rio.setTitle(_translate("Main", "Re&latório"))
        self.menuUsuarios.setTitle(_translate("Main", "&Usuarios"))
        self.menuConfigura_es.setTitle(_translate("Main", "&Configurações"))
        self.menuForncedor.setTitle(_translate("Main", "Fornecedor"))
        self.cadastrar_produto.setText(_translate("Main", "Cadastrar(CTRL+C)"))
        self.consultar_produto.setText(_translate("Main", "Consultar(CTRL+&L)"))
        self.relatorio.setText(_translate("Main", "&Consulta(CTRL+I)"))
        self.gerenciar_usuario.setText(_translate("Main", "Gerenciar(CTRL+U)"))
        self.actionConsultar_2.setText(_translate("Main", "Consultar"))
        self.bancodados.setText(_translate("Main", "&Banco de Dados"))
        self.backup.setText(_translate("Main", "Ba&ckup"))
        self.actionFornecedor_CTRL_F.setText(_translate("Main", "&Fornecedor(CTRL+F)"))
        self.cadastrar_fornecedor.setText(_translate("Main", "Cadastrar(CTRL+F)"))
        self.consultar_fornecedor.setText(_translate("Main", "Consultar"))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

#pyinstaller --onedir --windowed