# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addCityDialog.ui'
#
# Created by: PyQt5 windows code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AddKeyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddKeyDialog, self).__init__(parent)
        # 设置主界面的标题及初始大小
        self.setWindowTitle('添加行业词')
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
        self.key_text = QtWidgets.QLineEdit(Dialog)
        self.key_text.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.key_text.setObjectName("city_text")

        self.retranslateUi(Dialog)
        self.button_ny.accepted.connect(self.add_key)
        self.button_ny.rejected.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def add_key(self):
        """
        添加城市名窗口的确定按钮点击事件
        将输入框的城市名添加到列表中，并更新UI
        :return:
        """
        # 窗口关闭，允许再次打开添加该窗口
        self.parent.key_dialog_showed = False

        # 获取数据的城市名并添加到主窗口实例的城市名列表中
        self.parent.key_datalist.append(self.key_text.text())

        # 更新主窗口的城市名列表UI
        self.parent.update_key_list()
        self.close()

    def cancel(self):
        # 窗口关闭，允许再次打开添加该窗口
        self.parent.key_dialog_showed = False
        self.close()
