from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from qfluentwidgets import SubtitleLabel
from ...components.dialog.dialog import MessageBox
from ...components.layout.Frame import Frame
from ...components.input.InputText import InputText

class ProductDialog():

    def __init__(self, parent):
        
        self.content = Frame('vertical', 'content_dial', parent=parent)

        self.layoutTitle = Frame('horizontal', 'row', parent=parent)
        self.title = SubtitleLabel('Nouveau produit')

        self.row = Frame('horizontal', 'row', parent=parent)
        self.inputCode = InputText("Code", self.row)
        self.inputDesignation = InputText("Designation", self.row)

        self.row_2 = Frame('horizontal', 'row_2', parent=parent)
        self.inputCategory = InputText("Categorie", self.row_2)
        self.inputSubCategory = InputText("Sous categorie", self.row_2)

        self.layoutTitle.setMargins(8,4,0,0)
        self.row.setMargins(0,0,0,0)
        self.row_2.setMargins(0,0,0,0)

        #self.content.setStyleSheet("#content_dial{ background: #ff7788 } #row_2 { background: #142170 } #row{ background: #cccfee }")

        self.layoutTitle.addWidget(self.title)
        self.content.addWidget(self.layoutTitle)
        self.content.addWidget(self.row)
        self.content.addWidget(self.row_2)

        self.dialog = MessageBox(self.content, parent=parent)
        self.dialog.show()        
        self.dialog.yesButton.clicked.connect(self.yesBtnEvent)


    def yesBtnEvent(self):
        self.dialog.accept()
        self.dialog.yesSignal
        print("hello world")

