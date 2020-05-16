from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from ui import initUI

class Window(QtWidgets.QMainWindow)
    def __init__(self):
        super(Window, self).__init__()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())