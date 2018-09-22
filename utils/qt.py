from math import sqrt
import os.path as osp

import numpy as np

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

here = osp.dirname(osp.abspath(__file__))


def new_icon(icon):
    """
    创建icon实例
    :param icon: icon文件名（不含后缀）
    :return:
    """
    icons_dir = osp.join(here, '../icons')
    return QtGui.QIcon(osp.join(':/', icons_dir, '%s.png' % icon))


def new_action(parent, text, slot=None, shortcut=None, icon=None,
               tip=None, checkable=False, enabled=True):
    """
    创建响应事件实例框架
    :param parent:
    :param text:
    :param slot:
    :param shortcut:快捷键
    :param icon:
    :param tip:
    :param checkable:
    :param enabled:
    :return:
    """
    action = QtWidgets.QAction(text, parent)
    if icon is not None:
        action.setIconText(text)
        action.setIcon(new_icon(icon))
    if shortcut is not None:
        if isinstance(shortcut, (list, tuple)):
            action.setShortcuts(shortcut)
        else:
            action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if slot is not None:
        parent.triggered[action].connect(slot)
    if checkable:
        action.setCheckable(True)
    action.setEnabled(enabled)
    return action


def add_action(widget, actions):
    """
    向窗口部件中添加响应事件
    """
    for action in actions:
        if action is None:
            widget.addSeparator()
        elif isinstance(action, QtWidgets.QMenu):
            widget.addMenu(action)
        else:
            widget.addAction(action)
