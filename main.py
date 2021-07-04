import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form

class form(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)


app=QtWidgets.QApplication(sys.argv)
mainWindow=form()
mainWindow.show()
sys.exit(app.exec_())