import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QGridLayout,
                             QMainWindow, QPushButton, QTextEdit, QWidget)

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../turbulence02")))
import pro_data

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../turbulence02/source")))
import read_file

file_dir = os.path.abspath(os.path.join(os.getcwd(), "../turbulence02/"))
pro_folder = "pro"
test_folder = "test_data"
result_folder = "result"
data_folder = "zhenghe"


# step1 ： 标准化载入
def openWindow(centralwidget, textEdit):
    fname = QFileDialog.getOpenFileName(centralwidget, "Open file", ".")
    if fname[0]:

        textEdit.setText(fname[0])


def load(textEdit):
    print("开始载入")
    path = textEdit.toPlainText()
    print("载入文件路径为" + path)
    res = read_file.read_single_file_excel(path)
    print("读取完毕")
    res_concat = pro_data.pro_data(res)
    print("修改完毕")
    res_concat.to_csv(
        os.path.join(file_dir, test_folder, "tuanliu_import_data.csv"),
        encoding="utf-8",
        index=False,
    )
    # return res_concat


# step2 ： 计算湍流
def check_enable(
    checkBox,
    label_6,
    textEdit_5,
    textEdit_2,
    textEdit_3,
    textEdit_4,
    textEdit_6,
    textEdit_7,
    textEdit_8,
    label_4,
    label_5,
):
    if checkBox.isChecked():

        textEdit_2.setEnabled(True),
        textEdit_3.setEnabled(True),
        textEdit_4.setEnabled(True),
        textEdit_6.setEnabled(True),
        textEdit_7.setEnabled(True),
        textEdit_8.setEnabled(True),
        label_4.setEnabled(True),
        label_5.setEnabled(True),

        label_6.setEnabled(False),
        textEdit_5.setEnabled(False),
    else:
        label_6.setEnabled(True),
        textEdit_5.setEnabled(True),
        textEdit_2.setEnabled(False),
        textEdit_3.setEnabled(False),
        textEdit_4.setEnabled(False),
        textEdit_6.setEnabled(False),
        textEdit_7.setEnabled(False),
        textEdit_8.setEnabled(False),
        label_4.setEnabled(False),
        label_5.setEnabled(False),


def check(
    checkBox,
    textEdit_5,
    textEdit_2,
    textEdit_3,
    textEdit_4,
    textEdit_6,
    textEdit_7,
    textEdit_8,
    pushButton_4,
):
    print("开始检测")
    if textEdit_5.toPlainText(): 
        D5 = eval(textEdit_5.toPlainText())
    else:
        D5=0
    if textEdit_2.toPlainText(): 
        D2 = eval(textEdit_2.toPlainText())
    else:
        D2=0
    if textEdit_3.toPlainText(): 
        D3 = eval(textEdit_3.toPlainText())
    else:
        D3=0
    if textEdit_4.toPlainText(): 
        D4 = eval(textEdit_4.toPlainText())
    else:
        D4=0
    if textEdit_6.toPlainText(): 
        N2 = eval(textEdit_6.toPlainText())
    else:
        N2=0
    if textEdit_7.toPlainText(): 
        N3 = eval(textEdit_7.toPlainText())
    else:
        N3=0
    if textEdit_8.toPlainText(): 
        N4 = eval(textEdit_8.toPlainText())
    else:
        N4=0 

    print(D5)
    check_file = os.path.join(file_dir, test_folder, "tuanliu_import_data.csv")
    if os.path.exists(check_file):

        if checkBox.isChecked():
            if (D2 != 0 and N2 != 0) or (D3 != 0 and N3 != 0) or (D4 != 0 and N4 != 0):
                pushButton_4.setEnabled(True)
                print("可以计算湍流")
            else:
                print("请输入各风机类型直径D及风机数量") 
        else:
            if D5 != 0:
                pushButton_4.setEnabled(True)
                print("可以计算湍流")
            else:
                print("请输入风机直径D")
    else:
        
        pushButton_4.setEnabled(False)
        print("不可以计算湍流")

def calculate(checkBox,
    textEdit_5,
    textEdit_2,
    textEdit_3,
    textEdit_4,
    textEdit_6,
    textEdit_7,
    textEdit_8,):
    print("开始计算")
    check_file = os.path.join(file_dir, test_folder, "tuanliu_import_data.csv")

    if checkBox.isEnabled():


        # pushButton.setEnabled(True)
        print("可以计算湍流")
    else:
        D = eval(textEdit.toPlainText())
        print(D)


# from functools import partial
# from processing import openWindow,load,check,calculate
# self.pushButton.clicked.connect(partial(openWindow,self.centralwidget,self.textEdit))
# self.pushButton_2.clicked.connect(partial(load,self.textEdit))
# self.pushButton_3.clicked.connect(partial(check,self.pushButton_4))
# self.pushButton_4.clicked.connect(partial(calculate)
