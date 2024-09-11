# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import pics_ui_rc
import pics_ui_rc

class Ui_startForm(object):
    def setupUi(self, startForm):
        if not startForm.objectName():
            startForm.setObjectName(u"startForm")
        startForm.resize(645, 251)
        self.centralwidget = QWidget(startForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.login_btn = QPushButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(50, 180, 91, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 10, 341, 191))
        self.label_2.setPixmap(QPixmap(u":/Pictures/Pictures/test_Figure.jpg"))
        self.label_2.setScaledContents(True)
        self.account_info = QLineEdit(self.centralwidget)
        self.account_info.setObjectName(u"account_info")
        self.account_info.setGeometry(QRect(100, 120, 141, 21))
        self.password_info = QLineEdit(self.centralwidget)
        self.password_info.setObjectName(u"password_info")
        self.password_info.setGeometry(QRect(100, 150, 141, 21))
        self.signup_btn = QPushButton(self.centralwidget)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setGeometry(QRect(150, 180, 91, 21))
        self.account_label = QLabel(self.centralwidget)
        self.account_label.setObjectName(u"account_label")
        self.account_label.setGeometry(QRect(50, 120, 31, 20))
        self.account_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.account_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(50, 150, 31, 20))
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.head_label = QLabel(self.centralwidget)
        self.head_label.setObjectName(u"head_label")
        self.head_label.setGeometry(QRect(10, 30, 271, 81))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(18)
        self.head_label.setFont(font)
        self.head_label.setCursor(QCursor(Qt.ArrowCursor))
        self.head_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        startForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(startForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 645, 22))
        startForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(startForm)
        self.statusbar.setObjectName(u"statusbar")
        startForm.setStatusBar(self.statusbar)

        self.retranslateUi(startForm)

        self.login_btn.setDefault(False)
        self.signup_btn.setDefault(False)


        QMetaObject.connectSlotsByName(startForm)
    # setupUi

    def retranslateUi(self, startForm):
        startForm.setWindowTitle(QCoreApplication.translate("startForm", u"\u767b\u5f55\u754c\u9762", None))
        self.login_btn.setText(QCoreApplication.translate("startForm", u"\u767b\u5f55", None))
        self.label_2.setText("")
        self.signup_btn.setText(QCoreApplication.translate("startForm", u"\u6ce8\u518c", None))
        self.account_label.setText(QCoreApplication.translate("startForm", u"\u8d26\u53f7", None))
        self.password_label.setText(QCoreApplication.translate("startForm", u"\u5bc6\u7801", None))
        self.head_label.setText(QCoreApplication.translate("startForm", u"\u6b22\u8fce\u4f7f\u7528\n"
"\u201c\u60a6\u5fc3\u667a\u6108\u201d\n"
"\u6291\u90c1\u75c7\u5e72\u9884\u8c03\u63a7\u7cfb\u7edf", None))
    # retranslateUi

