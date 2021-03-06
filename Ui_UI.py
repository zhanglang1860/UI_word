# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OneDrive - Microsoft 365\工作\联合动力（新）\1. 代码\UI_word\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from processing import openWindow, load, check, calculate, check_enable
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 893)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 70, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 561, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 140, 71, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 70, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 140, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 347, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(21, 31, 144, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 514, 149))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(41, 388, 64, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(111, 388, 151, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(373, 388, 64, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setGeometry(QtCore.QRect(443, 388, 151, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(111, 427, 151, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setGeometry(QtCore.QRect(443, 427, 151, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(111, 470, 151, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setGeometry(QtCore.QRect(443, 470, 151, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setEnabled(True)
        self.textEdit_5.setGeometry(QtCore.QRect(90, 300, 151, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 64, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        # self.pushButton.clicked.connect(self.textEdit.clear)
        self.pushButton.clicked.connect(
            partial(openWindow, self.centralwidget, self.textEdit)
        )
        self.pushButton_2.clicked.connect(partial(load, self.textEdit))
        self.pushButton_3.clicked.connect(
            partial(
                check,
                self.checkBox,
                self.textEdit_5,
                self.textEdit_2,
                self.textEdit_3,
                self.textEdit_4,
                self.textEdit_6,
                self.textEdit_7,
                self.textEdit_8,
                self.pushButton_4,
            )
        )
        self.pushButton_4.clicked.connect(
            partial(calculate, self.checkBox, self.textEdit_5)
        )

        self.checkBox.clicked.connect(
            partial(
                check_enable,
                self.checkBox,
                self.label_6,
                self.textEdit_5,
                self.textEdit_2,
                self.textEdit_3,
                self.textEdit_4,
                self.textEdit_6,
                self.textEdit_7,
                self.textEdit_8,
                self.label_4,
                self.label_5,
            )
        )
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "打开"))
        self.textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'微软雅黑'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p></body></html>",
            )
        )
        self.pushButton_3.setText(_translate("MainWindow", "检验"))
        self.pushButton_2.setText(_translate("MainWindow", "载入"))
        self.pushButton_4.setText(_translate("MainWindow", "计算"))
        self.checkBox.setText(_translate("MainWindow", "存在多种类型风机"))
        self.label.setText(_translate("MainWindow", "第一步：标准化输出"))
        self.label_2.setText(_translate("MainWindow", "第二步：计算湍流"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p>计算湍流分成两步：</p><p>1) 首先进行检测test_data文件夹内，是否有标准化输出的湍流文件</p><p>2) 若有标准化输出的湍流文件，那么进行湍流计算</p><p>    若风电场存在多种类型风机，需要指定风机类型及风机数量（需要排序）</p></body></html>",
            )
        )
        self.label_4.setText(
            _translate("MainWindow", "<html><head/><body><p>风机直径</p></body></html>")
        )
        self.label_5.setText(
            _translate("MainWindow", "<html><head/><body><p>风机数量</p></body></html>")
        )
        self.label_6.setText(
            _translate("MainWindow", "<html><head/><body><p>风机直径</p></body></html>")
        )
        self.menu.setTitle(_translate("MainWindow", "你好"))
