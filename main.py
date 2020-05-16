from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import algorithm as alg

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
        self.widgets()
        self.menubar()
        self.menuEvent()
        self.layouts()
        self.UIsetting()

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
        self.midgray = QtWidgets.QAction('图像转中灰')
        self.light = QtWidgets.QAction('图像转浅灰')
        self.dark = QtWidgets.QAction('图像转深灰')
        self.binarization = QtWidgets.QAction('图像二值化')
        self.gaussfilter = QtWidgets.QAction('高斯滤波')
        self.medianfilter = QtWidgets.QAction('中值滤波')
        self.meanfilter = QtWidgets.QAction('均值滤波')
        self.twicecompress = QtWidgets.QAction('图像二倍压缩')
        self.quintupling = QtWidgets.QAction('图像五倍压缩')
        self.tenfoldcompression = QtWidgets.QAction('图像十倍压缩')
        self.quartile = QtWidgets.QAction('图像四等分')
        self.NineEqualparts = QtWidgets.QAction('图像九等分')
        self.AIcutout = QtWidgets.QAction('智能边缘抠图')
        self.bgmean = QtWidgets.QAction('背景颜色均值')
        self.imageSynthesis = QtWidgets.QAction('图像合成')

        self.file.addAction(self.open)
        self.file.addAction(self.save)
        self.file.addAction(self.quit)
        self.gray.addAction(self.midgray)
        self.gray.addAction(self.light)
        self.gray.addAction(self.dark)
        self.gray.addAction(self.binarization)
        self.clearupnoise.addAction(self.gaussfilter)
        self.clearupnoise.addAction(self.medianfilter)
        self.clearupnoise.addAction(self.meanfilter)
        self.compress.addAction(self.twicecompress)
        self.compress.addAction(self.quintupling)
        self.compress.addAction(self.tenfoldcompression)
        self.section.addAction(self.quartile)
        self.section.addAction(self.NineEqualparts)
        self.cutout.addAction(self.AIcutout)

        self.cutmore = self.cutout.addMenu('提取背景')
        self.cutmore.addAction(self.bgmean)
        self.cutmore.addAction(self.imageSynthesis)

    def menuEvent(self):
        self.open.triggered.connect(alg.fileAlgorithm.openfile)
        self.save.triggered.connect(alg.fileAlgorithm.savefile)
        self.quit.triggered.connect(alg.fileAlgorithm.quitprogram)

        self.midgray.triggered.connect(alg.fileAlgorithm.midgrayThm)
        self.light.triggered.connect(alg.fileAlgorithm.lightThm)
        self.dark.triggered.connect(alg.fileAlgorithm.darkThm)
        self.binarization.triggered.connect(alg.fileAlgorithm.binarizationThm)

        self.gaussfilter.triggered.connect(alg.fileAlgorithm.gaussfilterThm)
        self.medianfilter.triggered.connect(alg.fileAlgorithm.medianfilterThm)
        self.meanfilter.triggered.connect(alg.fileAlgorithm.meanfilterThm)

        self.twicecompress.triggered.connect(alg.fileAlgorithm.twicecompressThm)
        self.quintupling.triggered.connect(alg.fileAlgorithm.quintuplingThm)
        self.tenfoldcompression.triggered.connect(alg.fileAlgorithm.tenfoldcompressionThm)

        self.quartile.triggered.connect(alg.fileAlgorithm.quartileThm)
        self.NineEqualparts.triggered.connect(alg.fileAlgorithm.NineEqualpartsThm)

        self.AIcutout.triggered.connect(alg.fileAlgorithm.AIcutoutThm)
        self.bgmean.triggered.connect(alg.fileAlgorithm.bgmeanThm)
        self.imageSynthesis.triggered.connect(alg.fileAlgorithm.imageSynthesisThm)



    def layouts(self):
        pass




    def UIsetting(self):
        pass





    def processtrigger(self, Qaction):
        print(Qaction.text(), 'is triggered!')
        # 测试 triggered[QtWidgets.QAction] 点击函数







if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())