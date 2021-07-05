import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form

import lexi 
import syntactic 


class form(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.lexicalAnalysis)
        self.ui.pushButton_4.clicked.connect(self.syntacticalAnalysis)

    def lexicalAnalysis(self):
        code = self.ui.textEdit.toPlainText()

        lexer = lexi.goLexer()
        lexer.input(code)

        tokens = ''

        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            tokens += str(tok) + '\n'


        self.ui.textEdit_2.setText(tokens)

    def syntacticalAnalysis(self):
        code = self.ui.textEdit.toPlainText()
        parser = syntactic.parser

        syntactic.flag = True
        
        result = parser.parse(code)
        
        if syntactic.flag == False:
            self.ui.textEdit_3.setText('Syntax error in input!')
        else:
            self.ui.textEdit_3.setText(str(result))


app=QtWidgets.QApplication(sys.argv)
mainWindow=form()
mainWindow.show()
sys.exit(app.exec_())