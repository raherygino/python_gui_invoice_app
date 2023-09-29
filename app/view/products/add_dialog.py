# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_product_dialogpVYtvV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qfluentwidgets import LineEdit


class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(687, 161)
        AddProductDialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(AddProductDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_content = QFrame(AddProductDialog)
        self.dialog_content.setObjectName(u"dialog_content")
        self.dialog_content.setStyleSheet(u"#dialog_content {background-color: #454545; border:solid 2px; border-radius: 10px} QLabel { color: #ffffff }")
        self.dialog_content.setFrameShape(QFrame.StyledPanel)
        self.dialog_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dialog_content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.dialog_content)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)

        self.verticalLayout_2.addWidget(self.title)

        self.row = QFrame(self.dialog_content)
        self.row.setObjectName(u"row")
        self.row.setMaximumSize(QSize(16777215, 60))
        self.row.setFrameShape(QFrame.StyledPanel)
        self.row.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.row)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.col = QFrame(self.row)
        self.col.setObjectName(u"col")
        self.col.setFrameShape(QFrame.StyledPanel)
        self.col.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.col)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.col)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.verticalLayout_4.addWidget(self.label)

        self.LineEdit = LineEdit(self.col)
        self.LineEdit.setObjectName(u"LineEdit")

        self.verticalLayout_4.addWidget(self.LineEdit)


        self.horizontalLayout.addWidget(self.col)

        self.col_2 = QFrame(self.row)
        self.col_2.setObjectName(u"col_2")
        self.col_2.setFrameShape(QFrame.StyledPanel)
        self.col_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.col_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.col_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.LineEdit_2 = LineEdit(self.col_2)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.verticalLayout_3.addWidget(self.LineEdit_2)


        self.horizontalLayout.addWidget(self.col_2)


        self.verticalLayout_2.addWidget(self.row)

        self.row_2 = QFrame(self.dialog_content)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.row_2)

        self.buttonBox = QDialogButtonBox(self.dialog_content)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addWidget(self.dialog_content)


        self.retranslateUi(AddProductDialog)
        self.buttonBox.accepted.connect(AddProductDialog.accept)
        self.buttonBox.rejected.connect(AddProductDialog.reject)

        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("AddProductDialog", u"Ajouter un produit", None))
        self.label.setText(QCoreApplication.translate("AddProductDialog", u"Code", None))
        self.label_2.setText(QCoreApplication.translate("AddProductDialog", u"Designation", None))
    # retranslateUi

