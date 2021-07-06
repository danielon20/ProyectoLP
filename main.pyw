import sys
from PyQt5 import QtWidgets
from view.gui import Ui_Form

import lexical_analyzer.lexi as lexi
import syntactic_analyzer.syntactic as syntactic


class Form(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.lexicalAnalysis)
        self.ui.pushButton_4.clicked.connect(self.syntacticalAnalysis)

        self.loadTestAlgorithm()

    def loadTestAlgorithm(self):
        file = open('test algorithm.txt','r')
        lines = file.readlines()
        content = "".join(lines)
        self.ui.textEdit.setText(content)

    def lexicalAnalysis(self):
        code = self.ui.textEdit.toPlainText()

        lexer = lexi.goLexer()
        lexer.input(code)

        tokens = ''

        while True:
            token = lexer.token()
            if not token:
                break  # No more input
            tokens += str(token) + '\n'

        self.ui.textEdit_2.setText(tokens)

    def syntacticalAnalysis(self):
        code = self.ui.textEdit.toPlainText()
        parser = syntactic.parser


        syntactic.flag = True

        result = parser.parse(code)

        if not syntactic.flag:
            self.ui.textEdit_3.setText('Syntax error in input!')
        else:
            self.ui.textEdit_3.setText(str(result) + '\n' + str(parser.productions))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Form()
    mainWindow.show()
    sys.exit(app.exec_())
