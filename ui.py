from PyQt5 import QtWidgets
from PyQt5 import QtGui

class initUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(initUI, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(1000, 1000)

        self.setWindowTitle('图像处理')
        self.setWindowIcon(QtGui.QIcon('web.png'))



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())