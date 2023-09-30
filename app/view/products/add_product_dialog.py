from PyQt5.QtWidgets import QFrame, QHBoxLayout
from qfluentwidgets import LineEdit
from ...components.dialog.dialog import MessageBox

class ProductDialog():

    def __init__(self, parent):
        self.rw = QFrame(parent=parent)
        self.lnEdit = LineEdit(self.rw)
        self.lnEdit_1 = LineEdit(self.rw)
        self.rwLayout = QHBoxLayout(self.rw)
        self.rwLayout.addWidget(self.lnEdit)
        self.rwLayout.addWidget(self.lnEdit_1)
        MessageBox("hello", self.rw, parent=parent).show()

