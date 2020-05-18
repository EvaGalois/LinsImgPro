#!./env/bin/python
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
# from PyQt5 import Qt
import numpy as np
from PIL import Image
import cv2
import math

class initUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(initUI, self).__init__(*args, **kwargs)
        self.setupUI()

    def setupUI(self):
        self.resize(800, 800)
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
        self.SliderEvent()
        self.UIsetting()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def widgets(self):
        # self.scaling = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.scaling = QtWidgets.QSlider(QtCore.Qt.Vertical)
        # self.rotation = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.rotation = QtWidgets.QSlider(QtCore.Qt.Vertical)

        self.scaling.setMinimum(10)
        self.scaling.setMaximum(200)
        self.scaling.setSingleStep(2)
        self.scaling.setTickInterval(2)
        self.scaling.setValue(100)
        self.scaling.setTickPosition(QtWidgets.QSlider.TicksLeft)
        # self.scaling.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.rotation.setMinimum(-180)
        self.rotation.setMaximum(180)
        self.rotation.setSingleStep(4)
        self.rotation.setTickInterval(4)
        self.rotation.setValue(0)
        self.rotation.setTickPosition(QtWidgets.QSlider.TicksRight)
        # self.rotation.setStyleSheet('background-color: rgba(0, 0, 0, 0)')

        self.label_pic = QtWidgets.QLabel(self)

    def layouts(self):
        # 实例化一个 QWidget 类
        widget = QtWidgets.QWidget()

        # 垂直布局盒子
        Hbox = QtWidgets.QHBoxLayout()
        Hbox.addWidget(self.scaling)
        Hbox.addWidget(self.label_pic)
        Hbox.addWidget(self.rotation)

        Hbox.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(Hbox)

        self.scaleSign = QtWidgets.QLabel('缩放', widget)
        self.scaleSign.move(60, 30)
        self.scaleSign.setFont(QtGui.QFont("Arial", 18))
        self.scaleSign.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.angelSign = QtWidgets.QLabel('旋转', widget)
        self.angelSign.move(60, 80)
        self.angelSign.setFont(QtGui.QFont("Arial", 18))
        self.angelSign.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.scaleLab = QtWidgets.QLabel('1', widget)
        self.scaleLab.move(110, 30)
        self.scaleLab.setFont(QtGui.QFont("Arial", 20))
        self.scaleLab.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.angelLab = QtWidgets.QLabel('0', widget)
        self.angelLab.move(110, 80)
        self.angelLab.setFont(QtGui.QFont("Arial", 20))
        self.angelLab.setStyleSheet('background-color: rgba(0, 0, 0, 0)')

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

    def SliderEvent(self):
        self.scaling.valueChanged.connect(self.ScalingValueChanged)
        self.rotation.valueChanged.connect(self.RotationValueChanged)

    def UIsetting(self):
        pass

    # ignore test of the triggered[QtWidgets.QAction]
    def processtrigger(self, Qaction):
        print(Qaction.text(), 'is triggered!')

    def OpenFile(self):
        global height, width, nframes, image, bytesPerLine, filename, imgGray, orimg, imgRGB
        try:
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

            self.scaling.setValue(100)
            self.rotation.setValue(0)

            self.label_pic.resize(width, height)
            self.label_pic.setAlignment(QtCore.Qt.AlignCenter)

        except:
            self.showMessageBox()

    def SaveFile(self):
        #获取文件路径
        try:
            file_name = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFile", "./outputImgs","Text Files(*.png);;All Files(*)")
            print(file_name[0])
            qimg = self.label_pic.pixmap().toImage()  # 获取Qlabel图片
            print(qimg)
            mat_img = self.qimage2mat(qimg)  # 将Qimage转换为mat类型
            print(mat_img)
            cv2.imwrite(file_name[0], mat_img)
            # self.btn_saveFile = QPushButton(self)
            # self.btn_saveFile.file(filename,file_name[0])
        except:
            self.showMessageBox()

    def qimage2mat(self, qimg):
        try:
            ptr = qimg.constBits()
            ptr.setsize(qimg.byteCount())
            mat = np.array(ptr).reshape(qimg.height(), qimg.width(), 4)
            return mat
        except:
            print('error qimage2mat')

    def QuitProgram(self):
        self.close()

    def ScalingValueChanged(self):
        try:
            zoomScale = self.scaling.value() * 0.01
            zoomScale = round(zoomScale, 2)
            self.scaleLab.setText(str(zoomScale))

            Ang = eval(self.angelLab.text())
            # print(Ang)
            image = Image.fromarray(orimg.astype('uint8')).convert('RGB')
            Iwidth, Iheight = image.size
            new_image_length = Iwidth if Iwidth > Iheight else Iheight
            new_image = Image.new(image.mode, (new_image_length, new_image_length), color='#000')
            if Iwidth > Iheight:  # 原图宽大于高，则填充图片的竖直维度
                new_image.paste(image, (0, int((new_image_length - Iheight) / 2)))
            else:
                new_image.paste(image, (int((new_image_length - Iwidth) / 2), 0))
            imgIm = np.array(new_image)
            RGBimgIm = cv2.cvtColor(imgIm, cv2.COLOR_BGR2RGB)
            newSide = max(RGBimgIm.shape[0], RGBimgIm.shape[1])

            if width < height:
                matRotate = cv2.getRotationMatrix2D((newSide * 0.5, newSide * 0.5), Ang, 1 / math.sqrt((width / height) ** 2 + 1 ** 2))
                changeimgcode = 1
            elif width > height:
                matRotate = cv2.getRotationMatrix2D((newSide * 0.5, newSide * 0.5), Ang, 1 / math.sqrt((height / width) ** 2 + 1 ** 2))
                changeimgcode = 2
            else:
                matRotate = cv2.getRotationMatrix2D((newSide * 0.5, newSide * 0.5), Ang, 1 / math.sqrt(2))
                changeimgcode = 3

            imgRotate = cv2.warpAffine(RGBimgIm, matRotate, (newSide, newSide), borderValue=(0, 0, 0))

            # cv2.imshow("imgRotate", imgRotate)
            # cv2.waitKey(0)

            totalBytes = imgRotate.nbytes
            bytesPerLine = int(totalBytes / newSide)
            image = QtGui.QImage(imgRotate, newSide, newSide, bytesPerLine, QtGui.QImage.Format_RGB888)

            print('缩放', zoomScale)

            if changeimgcode == 1:
                ReductionFactor = math.sqrt((width / height) ** 2 + 1 ** 2)
            elif changeimgcode == 2:
                ReductionFactor = math.sqrt((height / width) ** 2 + 1 ** 2)
            else:
                ReductionFactor = math.sqrt(2)

            self.pic = QtGui.QPixmap(image).scaled(int(newSide * zoomScale * ReductionFactor), int(newSide * zoomScale * ReductionFactor))
            self.label_pic.setPixmap(self.pic)

        except:
            self.showMessageBox()

    def RotationValueChanged(self):
        try:
            Ang = self.rotation.value()
            self.angelLab.setText(str(Ang))
            zoomScale = eval(self.scaleLab.text())
            # print(zoomScale)

            w = int(zoomScale * orimg.shape[0])
            h = int(zoomScale * orimg.shape[1])
            mat = cv2.resize(orimg, (h, w))

            image = Image.fromarray(mat.astype('uint8')).convert('RGB')
            Iwidth, Iheight = image.size
            new_image_length = Iwidth if Iwidth > Iheight else Iheight
            new_image = Image.new(image.mode, (new_image_length, new_image_length), color='#000')

            if Iwidth > Iheight:  # 原图宽大于高，则填充图片的竖直维度
                new_image.paste(image, (0, int((new_image_length - Iheight) / 2)))
            else:
                new_image.paste(image, (int((new_image_length - Iwidth) / 2), 0))
            imgIm = np.array(new_image)
            RGBimgIm = cv2.cvtColor(imgIm, cv2.COLOR_BGR2RGB)
            newSide = max(RGBimgIm.shape[0], RGBimgIm.shape[1])

            if width < height:
                matRotate = cv2.getRotationMatrix2D((newSide * 0.5, newSide * 0.5), Ang, 1 / math.sqrt((width / height) ** 2 + 1 ** 2))
                changeimgcode = 1
            elif width > height:
                matRotate = cv2.getRotationMatrix2D((newSide * 0.5, newSide * 0.5), Ang, 1 / math.sqrt((height / width) ** 2 + 1 ** 2))
                changeimgcode = 2
            else:
                matRotate = cv2.getRotationMatrix2D((newSide * 0.5, newSide * 0.5), Ang, 1 / math.sqrt(2))
                changeimgcode = 3

            # matRotate[0,2] += (new_image_length - Iwidth) / 2 # 重点在这步
            # matRotate[1,2] += (new_image_length - Iheight) / 2 # 重点在这步

            imgRotate = cv2.warpAffine(RGBimgIm, matRotate, (newSide, newSide), borderValue=(0, 0, 0))

            NtotalBytes = imgRotate.nbytes
            NbytesPerLine = int(NtotalBytes / newSide)
            imgRotate = QtGui.QImage(imgRotate, newSide, newSide, NbytesPerLine, QtGui.QImage.Format_RGB888)

            if changeimgcode == 1:
                ReductionFactor = math.sqrt((width / height) ** 2 + 1 ** 2)
            elif changeimgcode == 2:
                ReductionFactor = math.sqrt((height / width) ** 2 + 1 ** 2)
            else:
                ReductionFactor = math.sqrt(2)

            print('旋转', Ang)

            self.pixdst = QtGui.QPixmap(imgRotate).scaled(int(newSide * ReductionFactor), int(newSide * ReductionFactor))
            self.label_pic.setPixmap(self.pixdst)

        except:
            self.showMessageBox()

    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.RightButton:
            self.scaling.setValue(100)
            self.rotation.setValue(0)
            print('缩放 1', '旋转 0')

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
       print('错误')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())