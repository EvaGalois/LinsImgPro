from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class initUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(initUI, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.resize(1000, 1000)
        self.setWindowTitle('图像处理')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setFixedSize(self.width(), self.height())
        self.center()
        # self.layouts()
        self.widgets()
        self.menubar()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def widgets(self):
        # trainsformation = # 嵌入图像旋转缩放画布
        self.scaling = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.rotation = QtWidgets.QSlider(QtCore.Qt.Horizontal)

    def menubar(self):
        # self.file.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.menubar = self.menuBar() # 获取窗体菜单栏

        self.file = self.menubar.addMenu('文件') # 菜单栏添加菜单项
        self.gray = self.menubar.addMenu('灰度')
        self.clearupnoise = self.menubar.addMenu('去燥')
        self.compress = self.menubar.addMenu('压缩')
        self.section = self.menubar.addMenu('切图')
        self.cutout = self.menubar.addMenu('抠图')

        self.open = QtWidgets.QAction('打开图像文件', self)
        self.open.setShortcut('Ctrl+O') # 设置快捷键
        self.save = QtWidgets.QAction('保存图像文件', self)
        self.save.setShortcut('Ctrl+S')
        self.quit = QtWidgets.QAction('退出程序' ,self)
        self.quit.setShortcut('Ctrl+Alt+Q')

        self.file.addAction(self.open)
        self.file.addAction(self.save)
        self.file.addAction(self.quit)
        self.gray.addAction('图像转中灰')
        self.gray.addAction('图像转浅灰')
        self.gray.addAction('图像转深灰')
        self.gray.addAction('图像二值化')
        self.clearupnoise.addAction('高斯滤波')
        self.clearupnoise.addAction('中值滤波')
        self.clearupnoise.addAction('均值滤波')
        self.compress.addAction('图像二倍压缩')
        self.compress.addAction('图像五倍压缩')
        self.compress.addAction('图像十倍压缩')
        self.section.addAction('图像四等分')
        self.section.addAction('图像九等分')
        self.cutout.addAction('智能边缘抠图')

        self.cutmore = self.cutout.addMenu('提取背景')
        self.cutmore.addAction('背景颜色均值')
        self.cutmore.addAction('图像合成')




    def processtrigger(self, qaction):
        print(qaction.text(), 'is triggered!')






if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())