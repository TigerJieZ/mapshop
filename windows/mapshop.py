# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapshop.ui'
#
# Created by: PyQt5 windows code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import functools

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import qt
from windows.addCityDialog import AddCityDialog


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.city = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 330, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 330, 221, 16))
        self.label.setObjectName("label")
        self.result_tableview = QtWidgets.QTableView(self.centralwidget)
        self.result_tableview.setGeometry(QtCore.QRect(10, 40, 771, 281))
        self.result_tableview.setMinimumSize(QtCore.QSize(0, 281))
        self.result_tableview.setObjectName("result_listview")
        self.url_text = QtWidgets.QTextEdit(self.centralwidget)
        self.url_text.setGeometry(QtCore.QRect(20, 350, 651, 31))
        self.url_text.setObjectName("url_text")
        self.copyurl_listview = QtWidgets.QPushButton(self.centralwidget)
        self.copyurl_listview.setGeometry(QtCore.QRect(690, 350, 81, 31))
        self.copyurl_listview.setObjectName("copyurl_listview")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 380, 761, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 400, 194, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.key_listview = QtWidgets.QListView(self.layoutWidget)
        self.key_listview.setMaximumSize(QtCore.QSize(256, 100))
        self.key_listview.setObjectName("key_listview")
        self.verticalLayout_2.addWidget(self.key_listview)
        self.addkey_button = QtWidgets.QPushButton(self.layoutWidget)
        self.addkey_button.setObjectName("addkey_button")
        self.verticalLayout_2.addWidget(self.addkey_button)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 400, 71, 16))
        self.label_4.setObjectName("label_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(500, 400, 271, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(430, 420, 75, 23))
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(510, 420, 75, 23))
        self.stop_button.setObjectName("stop_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(600, 420, 75, 23))
        self.clear_button.setObjectName("clear_button")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(680, 420, 101, 16))
        self.radioButton.setObjectName("radioButton")
        self.toexcel_button = QtWidgets.QPushButton(self.centralwidget)
        self.toexcel_button.setGeometry(QtCore.QRect(430, 450, 75, 23))
        self.toexcel_button.setObjectName("toexcel_button")
        self.totxt_button = QtWidgets.QPushButton(self.centralwidget)
        self.totxt_button.setGeometry(QtCore.QRect(510, 450, 75, 23))
        self.totxt_button.setObjectName("totxt_button")
        self.tovcf_button = QtWidgets.QPushButton(self.centralwidget)
        self.tovcf_button.setGeometry(QtCore.QRect(600, 450, 75, 23))
        self.tovcf_button.setObjectName("tovcf_button")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(680, 450, 101, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 400, 194, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.city_listview = QtWidgets.QListView(self.layoutWidget1)
        self.city_listview.setMaximumSize(QtCore.QSize(256, 100))
        self.city_listview.setObjectName("city_listview")
        self.verticalLayout.addWidget(self.city_listview)
        self.addcity_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.addcity_button.setObjectName("addcity_button")
        self.verticalLayout.addWidget(self.addcity_button)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 490, 54, 12))
        self.label_5.setObjectName("label_5")
        self.search_num_text = QtWidgets.QLabel(self.centralwidget)
        self.search_num_text.setGeometry(QtCore.QRect(500, 490, 54, 12))
        self.search_num_text.setObjectName("search_num_text")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 490, 31, 16))
        self.label_6.setObjectName("label_6")
        self.status_text = QtWidgets.QLabel(self.centralwidget)
        self.status_text.setGeometry(QtCore.QRect(600, 490, 161, 16))
        self.status_text.setObjectName("status_text")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 520, 54, 12))
        self.label_7.setObjectName("label_7")
        self.now_city_text = QtWidgets.QLabel(self.centralwidget)
        self.now_city_text.setGeometry(QtCore.QRect(500, 520, 54, 12))
        self.now_city_text.setObjectName("now_city_text")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 520, 71, 16))
        self.label_8.setObjectName("label_8")
        self.now_key_text = QtWidgets.QLabel(self.centralwidget)
        self.now_key_text.setGeometry(QtCore.QRect(630, 520, 61, 16))
        self.now_key_text.setObjectName("now_key_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # 初始化view
        self.init_view()
        # 初始化view的响应事件
        self.init_event()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "单击上面的某条信息，获取其来源网址"))
        self.copyurl_listview.setText(_translate("MainWindow", "复制网址"))
        self.label_3.setText(_translate("MainWindow", "[2]关键词-点击“快速添加行业词”"))
        self.addkey_button.setText(_translate("MainWindow", "快速添加行业词>>"))
        self.label_4.setText(_translate("MainWindow", "[3]查询操作"))
        self.start_button.setText(_translate("MainWindow", "开始查询"))
        self.stop_button.setText(_translate("MainWindow", "停止查询"))
        self.clear_button.setText(_translate("MainWindow", "清空"))
        self.radioButton.setText(_translate("MainWindow", "过滤重复号码"))
        self.toexcel_button.setText(_translate("MainWindow", "导出Excel"))
        self.totxt_button.setText(_translate("MainWindow", "导出Txt"))
        self.tovcf_button.setText(_translate("MainWindow", "导出VCF"))
        self.radioButton_2.setText(_translate("MainWindow", "显示座机号码"))
        self.label_2.setText(_translate("MainWindow", "[1]城市-点击“快速添加城市名称”"))
        self.addcity_button.setText(_translate("MainWindow", "快速添加城市名称>>"))
        self.label_5.setText(_translate("MainWindow", "成功查询："))
        self.search_num_text.setText(_translate("MainWindow", "。。。"))
        self.label_6.setText(_translate("MainWindow", "状态："))
        self.status_text.setText(_translate("MainWindow", "。。。"))
        self.label_7.setText(_translate("MainWindow", "当前城市："))
        self.now_city_text.setText(_translate("MainWindow", "。。。"))
        self.label_8.setText(_translate("MainWindow", "当前关键词："))
        self.now_key_text.setText(_translate("MainWindow", "。。。"))

    def init_event(self):
        """
        为控件设置点击事件
        :return:
        """

        # 添加城市按钮事件
        self.addcity_button.clicked.connect(self.add_city)

    def init_view(self):
        self.init_result_table()
        self.init_city_list()

    def init_result_table(self):
        """
        初始化查询结果表格
        :return:
        """
        self.result_tableview_model = QtGui.QStandardItemModel(10, 7)
        # 设置水平方向四个头标签文本内容
        self.result_tableview_model.setHorizontalHeaderLabels(['店铺名', '联系电话', '地图坐标', '地址', '区域', '行业', '来源网址'])
        self.result_tableview.setModel(self.result_tableview_model)
        # 优化1 表格填满窗口
        # 水平方向标签拓展剩下的窗口部分，填满表格
        self.result_tableview.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
        self.result_tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def init_city_list(self):
        """
        初始化城市列表
        :return:
        """

        # 初始化城市名称列表
        self.city_listview_model = QtCore.QStringListModel()
        self.city_datalist = []
        self.city_listview_model.setStringList(self.city_datalist)
        self.city_listview.setModel(self.city_listview_model)

        # 添加城市的弹窗状态
        self.city_dialog_showed = False

    def add_city(self):
        """
        “快速添加城市”的点击事件
        :return:
        """

        if not self.city_dialog_showed:
            # 窗口打开，不允许再次打开添加该窗口
            self.city_dialog_showed = True
            print('---', self.city_datalist)
            dialog = AddCityDialog(self)
            dialog.setupUi(dialog)
            dialog.show()

            print('+++', self.city_datalist)

        # AddCityDialog.

        self.city_listview_model.setStringList(self.city_datalist)

    def update_city_list(self):
        """
        更新城市名列表的显示
        :return:
        """
        self.city_listview_model.setStringList(self.city_datalist)
        self.city_listview.setModel(self.city_listview_model)
