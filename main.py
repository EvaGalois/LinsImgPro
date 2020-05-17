#!./env/bin/python
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import algorithm as alg

class initUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(initUI, self).__init__(*args, **kwargs)
        self.setupUI()

    def setupUI(self):
        self.resize(1000, 1000)
        self.setWindowTitle('图像处理')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setFixedSize(self.width(), self.height())
        self.center()
        self.widgets()
        self.layouts()
        self.menubar()
        self.menuEvent()
        self.UIsetting()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def widgets(self):
        self.scaling = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.rotation = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.label_pic = QtWidgets.QLabel(self)
        self.label_pic.setGeometry(100,100,400,400)
        # self.label_pic.setPixmap(QtGui.QPixmap('./inputImgs/test.jpg'))

    def layouts(self):
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        Vbox = QtWidgets.QVBoxLayout()

    def menubar(self):
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
        file_algorithms = alg.FileAlgoriThms()
        self.open.triggered.connect(lambda:file_algorithms.OpenFile())
        self.save.triggered.connect(lambda:file_algorithms.SaveFile())
        self.quit.triggered.connect(lambda:file_algorithms.QuitProgram())

        gray_thms = alg.GrayThms()
        self.midgray.triggered.connect(lambda:gray_thms.MidGrayThm())
        self.light.triggered.connect(lambda:gray_thms.LightThm())
        self.dark.triggered.connect(lambda:gray_thms.DarkThm())
        self.binarization.triggered.connect(lambda:gray_thms.BinarizationThm())

        fliter_thms = alg.FilterThms()
        self.gaussfilter.triggered.connect(lambda:fliter_thms.GaussFilterThm())
        self.medianfilter.triggered.connect(lambda:fliter_thms.MedianFilterThm())
        self.meanfilter.triggered.connect(lambda:fliter_thms.MeanFilterThm())

        compress_thms = alg.CompressThms()
        self.twicecompress.triggered.connect(lambda:compress_thms.TwiceCompressThm())
        self.quintupling.triggered.connect(lambda:compress_thms.QuintuplingThm())
        self.tenfoldcompression.triggered.connect(lambda:compress_thms.TenfoldCompressionThm())

        section_thms = alg.SectionThms()
        self.quartile.triggered.connect(lambda:section_thms.QuartileThm())
        self.NineEqualparts.triggered.connect(lambda:section_thms.NineEqualPartsThm())

        cutout_thms = alg.CutOutThms()
        self.AIcutout.triggered.connect(lambda:cutout_thms.AIcutoutThm())
        self.bgmean.triggered.connect(lambda:cutout_thms.BgMeanThm())
        self.imageSynthesis.triggered.connect(lambda:cutout_thms.ImageSynthesisThm())

    def UIsetting(self):
        pass



    # ignore test of the triggered[QtWidgets.QAction]
    def processtrigger(self, Qaction):
        print(Qaction.text(), 'is triggered!')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())