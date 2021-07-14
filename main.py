import sys
from PyQt5 import QtWidgets
from view.gui import Ui_Form

import lexical_analyzer.lexer as lexi
import syntactic_analyzer.parser as syntactic


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
        file.close()

    def lexicalAnalysis(self):
        code = self.ui.textEdit.toPlainText()

        lexer = lexi.goLexer()
        lexer.input(code)

        tokens = ''
        errors = ''

        while True:
            token = lexer.token()
            if not token:
                break  # No more input

            tokens += str(token) + '\n'
            #errors += lexi.error_message
            #lexi.error_message = ""

        if not lexi.flag:
            self.ui.textEdit_2.setText(lexi.error_message)
            lexi.flag = True
            lexi.error_message = ""
        else:
            self.ui.textEdit_2.setText(tokens)


    def syntacticalAnalysis(self):
        code = self.ui.textEdit.toPlainText()
        parser = syntactic.parser


        syntactic.flag = True
        syntactic.aux = True
        syntactic.error_message = ''

        result = parser.parse(code)

        if not syntactic.flag:
            self.ui.textEdit_3.setText(syntactic.error_message)
        else:
            self.ui.textEdit_3.setText(str(result) + '\n\n' + str(parser.productions))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Form()
    mainWindow.show()
    sys.exit(app.exec_())
