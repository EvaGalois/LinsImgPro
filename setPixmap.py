import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)    # 创建布局
        lb1 = QLabel(self)  # 实例化 QLabel 类
        lb1.setPixmap(QPixmap('./inputImgs/test2.jpg')) # 给 QLabel 的实例嵌入图片
        hbox.addWidget(lb1)     # 布局中加入 这个 QLabel 的实例
        self.setLayout(hbox)    # 给 self 设置这个布局

        self.move(300, 300)
        self.setWindowTitle('像素图控件')
        self.show()

    # def showDate(self, date):

    #     self.lb1.setText(date.toString())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())