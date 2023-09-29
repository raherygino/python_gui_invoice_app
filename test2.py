# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import (CaptionLabel, BodyLabel, SubtitleLabel, TitleLabel,
                            LargeTitleLabel,DisplayLabel, StrongBodyLabel, setTheme, Theme)

from oc_fluent_widgets import MessageBox

#from .qfluentwidgets import MessageDialog
#from .lib.test import HelloWordl


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.vBoxLayout = QVBoxLayout(self)
        setTheme(Theme.DARK)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.setSpacing(20)

        self.vBoxLayout.addWidget(CaptionLabel('Caption'))
        self.vBoxLayout.addWidget(BodyLabel('Body'))
        self.vBoxLayout.addWidget(StrongBodyLabel('Body Strong'))
        self.vBoxLayout.addWidget(SubtitleLabel('Subtitle'))
        self.vBoxLayout.addWidget(TitleLabel('Title'))
        self.vBoxLayout.addWidget(LargeTitleLabel('Title Large'))
        self.vBoxLayout.addWidget(DisplayLabel('Display'))
        MessageBox("hello", "test", self)
        #MessageBox("hello", "content", self.vBoxLayout).show()

        # customize text color
        # self.vBoxLayout.itemAt(0).widget().setTextColor('#009faa', '#009faa')

        # setTheme(Theme.DARK)
        # self.setStyleSheet("QWidget{background: rgb(32, 32, 32)}")


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()