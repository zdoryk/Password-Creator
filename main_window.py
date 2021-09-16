# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Password_creator_v1_0.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from custom_widgets.my_checkbox import MyCheckbox
from custom_widgets.py_slider import PySlider


class Ui_MainWindow(object):

    # Setup UI

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 800))
        MainWindow.setMaximumSize(QSize(500, 800))
        MainWindow.setStyleSheet(u"QLabel, QTextEdit, QPushButton, QCheckBox{\n"
                                 "	color: #F2F0F9;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget{\n"
                                 "	background-color: #1A1C20;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 501, 48))
        font = QFont()
        font.setFamily(u"Futura Hv BT")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(25, 130, 450, 65))
        self.widget.setStyleSheet(u"background-color: #2A2B33;\n"
                                  "border-radius: 16px;")
        self.password_text_edit = QTextEdit(self.widget)
        self.password_text_edit.setObjectName(u"password_text_edit")
        self.password_text_edit.setGeometry(QRect(10, 12, 431, 41))
        sizePolicy.setHeightForWidth(self.password_text_edit.sizePolicy().hasHeightForWidth())
        self.password_text_edit.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Futura Hv BT")
        font1.setPointSize(16)
        self.password_text_edit.setFont(font1)
        self.generate_btn = QPushButton(self.centralwidget)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setGeometry(QRect(160, 210, 190, 50))
        font2 = QFont()
        font2.setFamily(u"Futura Hv BT")
        font2.setPointSize(14)
        self.generate_btn.setFont(font2)
        self.generate_btn.setStyleSheet(u"background-color: #5834EA;\n"
                                        "border-radius: 22px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(25, 300, 450, 461))
        self.frame.setStyleSheet(u"background-color: #2A2B33;\n"
                                 "border-radius: 16px;\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalSlider = PySlider(Qt.Horizontal, self.frame)
        # self.horizontalSlider = QSlider(self.frame)
        self.horizontalSlider.setGeometry(QRect(50, 380, 351, 18))
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setMaximum(22)
        self.horizontalSlider.setValue(15)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.char_amount = QLabel(self.frame)
        self.char_amount.setObjectName(u"char_amount")
        self.char_amount.setGeometry(QRect(100, 400, 251, 31))
        self.char_amount.setFont(font1)
        self.char_amount_label = QLabel(self.frame)
        self.char_amount_label.setObjectName(u"label_7")
        self.char_amount_label.setGeometry(QRect(200, 330, 51, 41))
        self.char_amount_label.setFont(font1)
        self.char_amount_label.setStyleSheet(u"border-color: #B9B1D9;\n"
                                             "border-width: 2px;\n"
                                             "border-style: solid;\n"
                                             "border-radius: 10px;")
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 40, 371, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.number_checkbox = MyCheckbox(self.verticalLayoutWidget, 'Numbers')
        self.number_checkbox.setObjectName(u"lwr_str_checkbox")
        self.number_checkbox.setStyleSheet(u"\n""border-radius: 0px;")

        self.verticalLayout.addWidget(self.number_checkbox)

        self.uppr_str_checkbox = MyCheckbox(self.verticalLayoutWidget, 'Upper string')
        self.uppr_str_checkbox.setObjectName(u"lwr_str_checkbox")
        self.uppr_str_checkbox.setStyleSheet(u"\n""border-radius: 0px;")

        self.verticalLayout.addWidget(self.uppr_str_checkbox)

        self.lwr_str_checkbox = MyCheckbox(self.verticalLayoutWidget, 'Lower string')
        self.lwr_str_checkbox.setObjectName(u"lwr_str_checkbox")
        self.lwr_str_checkbox.setStyleSheet(u"\n""border-radius: 0px;")

        self.verticalLayout.addWidget(self.lwr_str_checkbox)

        self.spec_symb_checkbox = MyCheckbox(self.verticalLayoutWidget, 'Special symbols')
        self.spec_symb_checkbox.setObjectName(u"spec_symb_checkbox")
        self.spec_symb_checkbox.setStyleSheet(u"\n""border-radius: 0px;")

        self.verticalLayout.addWidget(self.spec_symb_checkbox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # retranslateUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password Creator", None))
        self.password_text_edit.setHtml(QCoreApplication.translate("MainWindow",
                                                                   u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:'Futura Hv BT'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                                                   '<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click "Generate"</p></body></html>',
                                                                   None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.char_amount.setText(QCoreApplication.translate("MainWindow", f"Characters amount", None))
        self.char_amount_label.setText(QCoreApplication.translate("MainWindow", u"15", None))

        self.horizontalSlider.valueChanged.connect(self.char_amount_label_change)

    def char_amount_label_change(self, value):
        self.char_amount_label.setText(str(value))
