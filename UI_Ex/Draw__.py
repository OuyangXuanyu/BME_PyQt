# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Draw_.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(768, 512)
        self.zoomInXButton = QPushButton(Form)
        self.zoomInXButton.setObjectName(u"pushButton")
        self.zoomInXButton.setGeometry(QRect(40, 340, 75, 24))
        self.zoomOutXButton = QPushButton(Form)
        self.zoomOutXButton.setObjectName(u"pushButton_2")
        self.zoomOutXButton.setGeometry(QRect(150, 350, 75, 24))
        self.zoomInYButton = QPushButton(Form)
        self.zoomInYButton.setObjectName(u"pushButton_3")
        self.zoomInYButton.setGeometry(QRect(260, 350, 75, 24))
        self.zoomOutYButton = QPushButton(Form)
        self.zoomOutYButton.setObjectName(u"pushButton_4")
        self.zoomOutYButton.setGeometry(QRect(370, 350, 75, 24))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 581, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plotWidget = QWidget(self.verticalLayoutWidget)
        self.plotWidget.setObjectName(u"widget")
        self.plotWidget.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.plotWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.zoomInXButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.zoomOutXButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.zoomInYButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.zoomOutYButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

