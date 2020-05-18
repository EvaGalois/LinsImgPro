# -*- coding:utf-8 -*-
# Time : 2019/08/13 下午 3:16
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt19_QSlider.py
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SliderDemo(QWidget):
    def __init__(self, parent=None):
        super(SliderDemo, self).__init__(parent)
        self.setWindowTitle("QSlider 示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("Hello PyQt5")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # 水平方向
        self.s1 = QSlider(Qt.Horizontal)
        # 设置最小值
        self.s1.setMinimum(10)
        # 设置最大值
        self.s1.setMaximum(50)
        # 设置步长
        self.s1.setSingleStep(3)
        # 设置当前值
        self.s1.setValue(20)
        # 刻度位置在下方
        self.s1.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.s1.setTickInterval(5)
        layout.addWidget(self.s1)
        # 连接信号槽
        self.s1.valueChanged.connect(self.value_changed)

    def value_changed(self):
        print("current slider value=%s" % self.s1.value())
        size = self.s1.value()
        self.label.setFont(QFont("Arial", size))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SliderDemo()
    win.show()
    sys.exit(app.exec_())
