# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addCityDialog.ui'
#
# Created by: PyQt5 windows code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AddCityDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddCityDialog, self).__init__(parent)
        # 设置主界面的标题及初始大小
        self.setWindowTitle('Dialog例子')
        self.resize(250, 100)
        self.parent = parent

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 80)
        self.button_ny = QtWidgets.QDialogButtonBox(Dialog)
        self.button_ny.setGeometry(QtCore.QRect(30, 50, 201, 32))
        self.button_ny.setOrientation(QtCore.Qt.Horizontal)
        self.button_ny.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.button_ny.setObjectName("button_ny")
        self.city_text = QtWidgets.QLineEdit(Dialog)
        self.city_text.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.city_text.setObjectName("city_text")

        self.retranslateUi(Dialog)
        self.button_ny.accepted.connect(self.add_city)
        self.button_ny.rejected.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def add_city(self):
        """
        添加城市名窗口的确定按钮点击事件
        将输入框的城市名添加到列表中，并更新UI
        :return:
        """
        # 窗口关闭，允许再次打开添加该窗口
        self.parent.city_dialog_showed = False

        # 获取数据的城市名并添加到主窗口实例的城市名列表中
        self.parent.city_datalist.append(self.city_text.text())

        # 更新主窗口的城市名列表UI
        self.parent.update_city_list()
        self.close()

    def cancel(self):
        # 窗口关闭，允许再次打开添加该窗口
        self.parent.city_dialog_showed = False
        self.close()
