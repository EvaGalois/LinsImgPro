from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import main as m
import cv2

class FileAlgoriThms:
    def __init__(self, *args, **kwargs):
        super(FileAlgoriThms, self).__init__(*args, **kwargs)

    def OpenFile(self):
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
        mainui = m.initUI()
        mainui.label_pic.setPixmap(self.pic)

    def SaveFile(self):
        print('successfully')

    def QuitProgram(self):
        print('successfully')

class GrayThms:
    def MidGrayThm(self):
        print('successfully')

    def LightThm(self):
        print('successfully')

    def DarkThm(self):
        print('successfully')

    def BinarizationThm(self):
        print('successfully')

class FilterThms:
    def GaussFilterThm(self):
        print('successfully')

    def MedianFilterThm(self):
        print('successfully')

    def MeanFilterThm(self):
        print('successfully')

class CompressThms:
    def TwiceCompressThm(self):
        print('successfully')

    def QuintuplingThm(self):
        print('successfully')

    def TenfoldCompressionThm(self):
        print('successfully')

class SectionThms:
    def QuartileThm(self):
        print('successfully')

    def NineEqualPartsThm(self):
        print('successfully')

class CutOutThms:
    def AIcutoutThm(self):
        print('successfully')

    def BgMeanThm(self):
        print('successfully')

    def ImageSynthesisThm(self):
        print('successfully')