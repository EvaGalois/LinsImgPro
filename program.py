#!./env/bin/python
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
# from PyQt5 import Qt
import cv2

class initUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(initUI, self).__init__(*args, **kwargs)
        self.setupUI()

    def setupUI(self):
        self.resize(1000, 1000)
        self.setWindowTitle('图像处理')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setMinimumSize(400, 400)
        # self.setFixedSize(self.width(), self.height())
        self.setStyleSheet('background-color: #000')
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

    def layouts(self):
        # 实例化一个 QWidget 类
        widget = QtWidgets.QWidget()

        # 垂直布局盒子
        Vbox = QtWidgets.QVBoxLayout()
        Vbox.addWidget(self.scaling)
        Vbox.addWidget(self.rotation)
        Vbox.addWidget(self.label_pic)

        widget.setLayout(Vbox)

        # 实例化后的 QWidget 给 QMainWindow 设置 setCentralWidget
        self.setCentralWidget(widget)

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
        self.open.triggered.connect(self.OpenFile)
        self.save.triggered.connect(self.SaveFile)
        self.quit.triggered.connect(self.QuitProgram)

        self.midgray.triggered.connect(self.MidGrayThm)
        self.light.triggered.connect(self.LightThm)
        self.dark.triggered.connect(self.DarkThm)
        self.binarization.triggered.connect(self.BinarizationThm)

        self.gaussfilter.triggered.connect(self.GaussFilterThm)
        self.medianfilter.triggered.connect(self.MedianFilterThm)
        self.meanfilter.triggered.connect(self.MeanFilterThm)

        self.twicecompress.triggered.connect(self.TwiceCompressThm)
        self.quintupling.triggered.connect(self.QuintuplingThm)
        self.tenfoldcompression.triggered.connect(self.TenfoldCompressionThm)

        self.quartile.triggered.connect(self.QuartileThm)
        self.NineEqualparts.triggered.connect(self.NineEqualPartsThm)

        self.AIcutout.triggered.connect(self.AIcutoutThm)
        self.bgmean.triggered.connect(self.BgMeanThm)
        self.imageSynthesis.triggered.connect(self.ImageSynthesisThm)

    def UIsetting(self):
        pass

    # ignore test of the triggered[QtWidgets.QAction]
    def processtrigger(self, Qaction):
        print(Qaction.text(), 'is triggered!')

    def OpenFile(self, use):
        global height, width, nframes, image, bytesPerLine, filename, imgGray, orimg, imgRGB

        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(None, "OpenFile", "./inputImgs", "All Files(*);;Text Files(*.png);;Text Files(*.jpg)")
        orimg = cv2.imread(filename)
        imgGray = cv2.cvtColor(orimg, cv2.COLOR_BGR2GRAY)
        imgRGB = cv2.cvtColor(orimg, cv2.COLOR_BGR2RGB)
        height, width, nframes, = imgRGB.shape
        totalBytes = imgRGB.nbytes
        bytesPerLine = int(totalBytes / height)
        img_Lab = QtGui.QImage(imgRGB, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.pic = QtGui.QPixmap(img_Lab).scaled(width, height)
        self.label_pic.setPixmap(self.pic)
        print(width, height)

        if width < 1000 & height < 1000:
            self.setFixedSize(width * 1.2, height * 1.2)
        elif width > 1000 & height > 1000:
            self.setFixedSize(width, height)

        self.label_pic.resize(width, height)
        self.label_pic.setAlignment(QtCore.Qt.AlignCenter)

    def SaveFile(self):
        #获取文件路径
        try:
            file_name = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFile", "./outputImgs","Text Files(*.png);;All Files(*)")
            print(file_name[0])
            qimg = self.label_pic.pixmap().toImage()  # 获取Qlabel图片
            mat_img = self.qimage2mat(qimg)  # 将Qimage转换为mat类型
            cv2.imwrite(file_name[0], mat_img)
            # self.btn_saveFile = QPushButton(self)
            # self.btn_saveFile.file(filename,file_name[0])
        except:
            self.showMessageBox()

    def qimage2mat(self, qimg):
        try:
            ptr = qimg.constBits()
            ptr.setsize(qimg.byteCount())
            mat = np.array(ptr).reshape(qimg.height(), qimg.width(), 4)  # 注意这地方通道数一定要填4，否则出错
            return mat
        except:
            pass

    def QuitProgram(self):
        print('successfully')

    def MidGrayThm(self):
        print('successfully')

    def LightThm(self):
        print('successfully')

    def DarkThm(self):
        print('successfully')

    def BinarizationThm(self):
        print('successfully')

    def GaussFilterThm(self):
        print('successfully')

    def MedianFilterThm(self):
        print('successfully')

    def MeanFilterThm(self):
        print('successfully')

    def TwiceCompressThm(self):
        print('successfully')

    def QuintuplingThm(self):
        print('successfully')

    def TenfoldCompressionThm(self):
        print('successfully')

    def QuartileThm(self):
        print('successfully')

    def NineEqualPartsThm(self):
        print('successfully')

    def AIcutoutThm(self):
        print('successfully')

    def BgMeanThm(self):
        print('successfully')

    def ImageSynthesisThm(self):
        print('successfully')

    def showMessageBox(self):
       print('保存错误')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())