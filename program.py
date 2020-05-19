#!./env/bin/python
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
# from PyQt5 import Qt
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as mpl
import cv2
import math

import traceback

class SomeCustomException(Exception):
    pass

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
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
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
        try:
            # self.scaling = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            self.scaling = QtWidgets.QSlider(QtCore.Qt.Vertical)
            # self.rotation = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            self.rotation = QtWidgets.QSlider(QtCore.Qt.Vertical)

            self.scaling.setMinimum(2)
            self.scaling.setMaximum(200)
            self.scaling.setSingleStep(2)
            self.scaling.setTickInterval(2)
            self.scaling.setValue(100)
            self.scaling.setTickPosition(QtWidgets.QSlider.TicksLeft)
            # self.scaling.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
            # self.scaling.setEnabled(False)
            self.rotation.setMinimum(-180)
            self.rotation.setMaximum(180)
            self.rotation.setSingleStep(4)
            self.rotation.setTickInterval(4)
            self.rotation.setValue(0)
            self.rotation.setTickPosition(QtWidgets.QSlider.TicksRight)
            # self.rotation.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
            # self.rotation.setEnabled(False)

            self.label_pic = QtWidgets.QLabel(self)

        except Exception:
            pass

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
        self.midgray = QtWidgets.QAction('图像转中灰' ,self)
        self.light = QtWidgets.QAction('图像转浅灰' ,self)
        self.dark = QtWidgets.QAction('图像转深灰' ,self)
        self.binarization = QtWidgets.QAction('图像二值化' ,self)
        self.gaussfilter = QtWidgets.QAction('高斯滤波' ,self)
        self.medianfilter = QtWidgets.QAction('中值滤波' ,self)
        self.meanfilter = QtWidgets.QAction('均值滤波' ,self)
        self.twicecompress = QtWidgets.QAction('图像二倍压缩' ,self)
        self.quintupling = QtWidgets.QAction('图像五倍压缩' ,self)
        self.tenfoldcompression = QtWidgets.QAction('图像十倍压缩' ,self)
        self.customizedCompr = QtWidgets.QAction('自定义压缩' ,self)
        self.quartile = QtWidgets.QAction('图像四切' ,self)
        self.NineEqualparts = QtWidgets.QAction('图像九切' ,self)
        self.customizedSec = QtWidgets.QAction('自定义切图' ,self)
        self.AIcutout = QtWidgets.QAction('智能边缘抠图' ,self)
        self.Chinese = QtWidgets.QAction('中文模式' ,self)
        self.English = QtWidgets.QAction('英文模式' ,self)

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
        self.compress.addAction(self.customizedCompr)
        self.section.addAction(self.quartile)
        self.section.addAction(self.NineEqualparts)
        self.section.addAction(self.customizedSec)
        self.cutout.addAction(self.AIcutout)

        self.cutmore = self.cutout.addMenu('语言设置')
        self.cutmore.addAction(self.Chinese)
        self.cutmore.addAction(self.English)

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

        self.twicecompress.triggered.connect(lambda:self.Compressing(2))
        self.quintupling.triggered.connect(lambda:self.Compressing(5))
        self.tenfoldcompression.triggered.connect(lambda:self.Compressing(10))
        self.customizedCompr.triggered.connect(self.customizedComprfunc)

        self.quartile.triggered.connect(lambda:self.Sec(2))
        self.NineEqualparts.triggered.connect(lambda:self.Sec(3))
        self.customizedSec.triggered.connect(self.customizedSecfunc)

        self.AIcutout.triggered.connect(self.AIcutoutThm)

    def SliderEvent(self):
        self.scaling.valueChanged.connect(self.ScalingValueChanged)
        self.rotation.valueChanged.connect(self.RotationValueChanged)

    def UIsetting(self):
        self.Chinese.triggered.connect(self.ChineseLang)
        self.English.triggered.connect(self.EnglishLang)

    # ignore test of the triggered[QtWidgets.QAction]
    def processtrigger(self, Qaction):
        print(Qaction.text(), 'is triggered!')

    def OpenFile(self):
        global height, width, nframes, image, bytesPerLine, filename, imgGray, orimg, imgRGB
        try:
            filename, filetype = QtWidgets.QFileDialog.getOpenFileName(None, "OpenFile", "./inputImgs", "All Files(*);;Text Files(*.png);;Text Files(*.jpg)")
            orimg = cv2.imread(filename)
            imgGray = cv2.cvtColor(orimg, cv2.COLOR_BGR2GRAY)
            print(orimg.shape)
            print(orimg)
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
            self.scaling.setEnabled(True)
            self.rotation.setEnabled(True)

        except Exception as e:
            print(e)
            traceback.print_exc()

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
        except Exception as e:
            print(e)
            traceback.print_exc()

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

        except Exception as e:
            # print(e)
            # traceback.print_exc()
            pass

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

        except Exception as e:
            # print(e)
            # traceback.print_exc()
            pass

    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.RightButton:
            self.scaling.setValue(100)
            self.rotation.setValue(0)
            print('缩放 1', '旋转 0')

    def MidGrayThm(self):
        try:
            print(filename,"图像转中灰")
            cv2.namedWindow("MidGRAY")
            cv2.resizeWindow("MidGRAY", int(width * 1), int(height * 1))
            MidGray = imgGray
            cv2.imshow("MidGRAY", MidGray)
            cv2.moveWindow("MidGRAY", 1000, 500)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像中性灰完成')

    def LightThm(self):
        try:
            print(filename, "图像转浅灰")
            cv2.namedWindow("LightGRAY")
            cv2.resizeWindow("LightGRAY", int(width * 1), int(height * 1))
            LightGray = imgGray
            lightGray = np.ravel(LightGray)
            for index in range(0, len(lightGray)):
                if lightGray[index] < 192:
                    lightGray[index] += 64
                else:
                    lightGray[index] = 255
            lightGrayImg = lightGray.reshape((height, width))
            cv2.imshow("LightGRAY", lightGrayImg)
            cv2.moveWindow("LightGRAY", 1000, 500)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像浅灰完成')

    def DarkThm(self):
        try:
            print(filename, "图像转深灰")
            cv2.namedWindow("DarkGRAY")
            cv2.resizeWindow("DarkGRAY", int(width * 1), int(height * 1))
            DarkGray = imgGray
            darkGray = np.ravel(DarkGray)
            for index in range(0, len(darkGray)):
                if darkGray[index] > 64:
                    darkGray[index] -= 64
                else:
                    darkGray[index] = 0
            darkGrayImg = darkGray.reshape((height, width))
            cv2.imshow("DarkGRAY", darkGrayImg)
            cv2.moveWindow("DarkGRAY", 1000, 500)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像深灰完成')

    def BinarizationThm(self):
        try:
            print(filename, "自适应阈值二值化")
            ret, adaptionDo_img = cv2.threshold(imgGray, 0, 255, cv2.THRESH_OTSU)
            cv2.namedWindow("THRESH_OTSU", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("THRESH_OTSU", int(width * 1), int(height * 1))
            cv2.imshow("THRESH_OTSU", adaptionDo_img)
            cv2.moveWindow("DarkGRAY", 1000, 500)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像二值化完成')

    def GaussFilterThm(self):
        try:
            print(filename, "高斯滤波处理")
            img_GaussianBlur = cv2.GaussianBlur(orimg, (11, 11), 0)
            cv2.namedWindow("GaussianBlur", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("GaussianBlur", int(width * 1), int(height * 1))
            cv2.imshow("GaussianBlur", img_GaussianBlur)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像滤波完成')

    def MedianFilterThm(self):
        try:
            print(filename, "中值滤波处理")
            img_medianBlur = cv2.medianBlur(orimg, 9)
            cv2.namedWindow("MedianBlur", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("MedianBlur", int(width * 1), int(height * 1))
            cv2.imshow("MedianBlur", img_medianBlur)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像滤波完成')

    def MeanFilterThm(self):
        try:
            print(filename, "均值滤波处理")
            img_Blur = cv2.blur(orimg, (10, 10))
            cv2.namedWindow("MeanBlur", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("MeanBlur", int(width * 1), int(height * 1))
            cv2.imshow("MeanBlur", img_Blur)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像滤波完成')

    def Compressing(self, compreN=2):
        try:
            compreNum = 1 / compreN
            decreaseimg = cv2.resize(orimg, (int(compreNum * width), int(compreNum * height)))
            RGBdecimg = cv2.cvtColor(decreaseimg, cv2.COLOR_BGR2RGB)
            decheight, decwidth, decnframes, = RGBdecimg.shape
            totalBytes = RGBdecimg.nbytes
            decbytesPerLine = int(totalBytes / decheight)
            decimage = QtGui.QImage(RGBdecimg, decwidth, decheight, decbytesPerLine, QtGui.QImage.Format_RGB888)
            self.decpix = QtGui.QPixmap(decimage).scaled(decwidth, decheight)
            self.label_pic.setPixmap(self.decpix)

            cv2.namedWindow("original", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("original", width, height)
            cv2.imshow("original", orimg)
            cv2.namedWindow("compression", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("compression", int(width * compreN), int(height * compreN))
            cv2.imshow("compression", decreaseimg)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像压缩完成')

    def customizedComprfunc(self):
        try:
            self.ComprfuncWindow = Comprfunc()
            self.ComprfuncWindow.show()

        except Exception as e:
            print(e)
            traceback.print_exc()

    def Sec(self, n=2):
        try:
            pilimage = Image.open(filename)
            item_width = int(width / n)
            item_height = int(height / n)
            box_list = []
            # (left, upper, right, lower)
            for i in range(0, n):  # 两重循环，生成 n^2 张图片基于原图的位置
                for j in range(0, n):
                    # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
                    box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)
                    box_list.append(box)
            image_list = [pilimage.crop(box) for box in box_list]
            mpl.use('Qt5Agg')
            plt.rcParams['toolbar'] = 'None'
            plt.style.use('dark_background')
            fig = plt.figure()
            for i in range(n**2):
                plt.subplot(n, n, i + 1), plt.imshow(image_list[i], 'gray')
                plt.title(str(i + 1))
                plt.axis('off')

            fig.subplots_adjust(wspace=0, hspace=0)
            fig.tight_layout()
            plt.tight_layout()
            fig.canvas.set_window_title('图像%s等分'%(str(n**2),))
            plt.show()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('图像切割完成')

    def customizedSecfunc(self):
        try:
            self.SecfuncWindow = Secfunc()
            self.SecfuncWindow.show()

        except Exception as e:
            print(e)
            traceback.print_exc()

    def AIcutoutThm(self):
        try:
            import paddlehub as hub
            import matplotlib.image as mpimg
            from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
            from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
            from matplotlib.figure import Figure

            humanseg = hub.Module(name="deeplabv3p_xception65_humanseg")
            results = humanseg.segmentation(data={"image": [filename]}, output_dir='outputImgs')

            result_img = mpimg.imread(results[0]['processed'])
            print(result_img.shape)
            mpl.use('Qt5Agg')
            plt.rcParams['toolbar'] = 'None'
            plt.style.use('dark_background')
            fig, ax = plt.subplots(1, 1, figsize=(int(result_img.shape[1]/100),int(result_img.shape[0]/100)), dpi=100)
            print(fig)
            print(ax)
            fig.subplots_adjust(wspace=0, hspace=0)
            fig.tight_layout()
            plt.tight_layout()
            plt.subplot(1,1,1)
            plt.imshow(result_img)
            plt.title(results[0]['processed'])
            plt.axis('off')
            fig.canvas.set_window_title(results[0]['processed'])
            # fig.canvas.manager.window.overrideredirect(1)
            print(type(fig.canvas))
            plt.show()

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('边缘检测成功')

    def ChineseLang(self):
        try:
            self.file.setTitle('File')
            self.gray.setTitle('Gray')
            self.clearupnoise.setTitle('ClearupNoise')
            self.compress.setTitle('Compress')
            self.section.setTitle('Section')
            self.cutout.setTitle('Cutout')
            self.open.setText('open')
            self.save.setText('save')
            self.quit.setText('quit')
            self.midgray.setText('midgray')
            self.light.setText('light')
            self.dark.setText('dark')
            self.binarization.setText('binarization')
            self.gaussfilter.setText('gaussfilter')
            self.medianfilter.setText('medianfilter')
            self.meanfilter.setText('meanfilter')
            self.twicecompress.setText('twicecompress')
            self.quintupling.setText('quintupling')
            self.tenfoldcompression.setText('tenfoldcompression')
            self.quartile.setText('quartile')
            self.NineEqualparts.setText('NineEqualparts')
            self.AIcutout.setText('AIcutout')
            self.cutmore.setTitle('SettingLang')
            self.Chinese.setText('Chinese')
            self.English.setText('English')
            self.scaleSign.setText('scale')
            self.angelSign.setText('angel')
            self.setWindowTitle('ImageProcessing')
            self.customizedCompr.setText('customizedCompr')
            self.customizedSec.setText('customizedSec')

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('异常清理')

    def EnglishLang(self):
        try:
            self.file.setTitle('File')
            self.gray.setTitle('Gray')
            self.clearupnoise.setTitle('ClearupNoise')
            self.compress.setTitle('Compress')
            self.section.setTitle('Section')
            self.cutout.setTitle('Cutout')
            self.open.setText('open')
            self.save.setText('save')
            self.quit.setText('quit')
            self.midgray.setText('midgray')
            self.light.setText('light')
            self.dark.setText('dark')
            self.binarization.setText('binarization')
            self.gaussfilter.setText('gaussfilter')
            self.medianfilter.setText('medianfilter')
            self.meanfilter.setText('meanfilter')
            self.twicecompress.setText('twicecompress')
            self.quintupling.setText('quintupling')
            self.tenfoldcompression.setText('tenfoldcompression')
            self.quartile.setText('quartile')
            self.NineEqualparts.setText('NineEqualparts')
            self.AIcutout.setText('AIcutout')
            self.cutmore.setTitle('SettingLang')
            self.Chinese.setText('Chinese')
            self.English.setText('English')
            self.scaleSign.setText('scale')
            self.angelSign.setText('angel')
            self.setWindowTitle('ImageProcessing')
            self.customizedCompr.setText('customizedCompr')
            self.customizedSec.setText('customizedSec')

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('异常清理')

    def showMessageBox(self):
       print('Successfully!')

class Comprfunc(QtWidgets.QWidget):
    def __init__(self):
        super(Comprfunc, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 100)
        self.setFixedSize(self.width(), self.height())
        self.setStyleSheet('background-color: #000')
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.setWindowTitle('压缩图像')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.center()
        self.widget()
        self.action()
        self.layout()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def widget(self):
        self.comlab = QtWidgets.QLabel('切割参数：', self)
        self.comlab.setFont(QtGui.QFont("Arial", 18))
        self.comlab.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.comnum = QtWidgets.QLineEdit('5', self)
        self.comnum.setFont(QtGui.QFont("Arial", 30))
        self.comnum.setPlaceholderText('Normal')
        self.comnum.setEchoMode(QtWidgets.QLineEdit.Normal)

        # 实例化整形验证器
        IntValidator = QtGui.QIntValidator(self)
        IntValidator.setRange(1, 99)
        self.comnum.setValidator(IntValidator)

        self.comnum.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.comnum.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.comnum.setStyleSheet('border: none;')
        # self.comnum.setStyleSheet('background-color: #fff')
        self.commit = QtWidgets.QPushButton('切图', self)
        self.commit.setFont(QtGui.QFont("Arial", 20))
        self.commit.setStyleSheet('padding: 8 8 8 8; background-color: ##4477ff; border-radius: 20; color: black')

        self.commit.clicked.connect(self.action)

    def action(self):
        try:
            log = initUI()
            value = int(self.comnum.text())
            log.Compressing(value)

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('切图完成!')

    def layout(self):
        self.Hbox = QtWidgets.QHBoxLayout(self)
        self.Hbox.addWidget(self.comlab)
        self.Hbox.addWidget(self.comnum)
        self.Hbox.addWidget(self.commit)
        self.Hbox.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.Hbox)

class Secfunc(QtWidgets.QWidget):
    def __init__(self):
        super(Secfunc, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 100)
        self.setFixedSize(self.width(), self.height())
        self.setStyleSheet('background-color: #000')
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.setWindowTitle('切割图像')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.center()
        self.widget()
        self.action()
        self.layout()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def widget(self):
        self.seclab = QtWidgets.QLabel('切割参数：', self)
        self.seclab.setFont(QtGui.QFont("Arial", 18))
        self.seclab.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.secnum = QtWidgets.QLineEdit('5', self)
        self.secnum.setFont(QtGui.QFont("Arial", 30))
        self.secnum.setPlaceholderText('Normal')
        self.secnum.setEchoMode(QtWidgets.QLineEdit.Normal)

        # 实例化整形验证器
        IntValidator = QtGui.QIntValidator(self)
        IntValidator.setRange(1, 99)
        self.secnum.setValidator(IntValidator)

        self.secnum.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.secnum.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.secnum.setStyleSheet('border: none;')
        # self.secnum.setStyleSheet('background-color: #fff')
        self.secmit = QtWidgets.QPushButton('切图', self)
        self.secmit.setFont(QtGui.QFont("Arial", 20))
        self.secmit.setStyleSheet('padding: 8 8 8 8; background-color: #4477ff; border-radius: 20; color: black')

        self.secmit.clicked.connect(self.action)

    def layout(self):
        self.Hbox = QtWidgets.QHBoxLayout(self)
        self.Hbox.addWidget(self.seclab)
        self.Hbox.addWidget(self.secnum)
        self.Hbox.addWidget(self.secmit)
        self.Hbox.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.Hbox)

    def action(self):
        try:
            log = initUI()
            value = int(self.secnum.text())
            log.Sec(value)

        except Exception as e:
            print(e)
            traceback.print_exc()

        finally:
            print('切图完成!')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = initUI()
    ui.show()
    sys.exit(app.exec_())