from PyQt5 import QtWidgets
from PyQt5 import QtGui

class initUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())