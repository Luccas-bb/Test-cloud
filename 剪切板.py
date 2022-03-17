# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:52:47 2021

@author: 56482
"""

import win32clipboard as w
import win32con


def get_text():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('GBK')


def set_text(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString.encode(encoding='gbk'))
    w.CloseClipboard()


# 读取剪切板内容
ss = get_text()
temp = ss.replace("\r\n","")
temp = temp.replace(" ","")
set_text(temp)
print(get_text())



