# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Draw_2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(773, 545)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 731, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plotWidget = QWidget(self.verticalLayoutWidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.plotWidget)

        self.x_start = QLabel(Form)
        self.x_start.setObjectName(u"x_start")
        self.x_start.setGeometry(QRect(50, 410, 32, 20))
        self.x_end = QLabel(Form)
        self.x_end.setObjectName(u"x_end")
        self.x_end.setGeometry(QRect(160, 410, 32, 20))
        self.y_middle_3 = QLabel(Form)
        self.y_middle_3.setObjectName(u"y_middle_3")
        self.y_middle_3.setGeometry(QRect(270, 410, 32, 20))
        self.y_range_left = QLabel(Form)
        self.y_range_left.setObjectName(u"y_range_left")
        self.y_range_left.setGeometry(QRect(360, 410, 71, 20))
        self.x_end_edit = QLineEdit(Form)
        self.x_end_edit.setObjectName(u"x_end_edit")
        self.x_end_edit.setGeometry(QRect(130, 430, 91, 20))
        self.y_range_edit_right = QLineEdit(Form)
        self.y_range_edit_right.setObjectName(u"y_range_edit_right")
        self.y_range_edit_right.setGeometry(QRect(460, 430, 91, 20))
        self.y_range_edit_left = QLineEdit(Form)
        self.y_range_edit_left.setObjectName(u"y_range_edit_left")
        self.y_range_edit_left.setGeometry(QRect(350, 430, 91, 20))
        self.x_start_edit = QLineEdit(Form)
        self.x_start_edit.setObjectName(u"x_start_edit")
        self.x_start_edit.setGeometry(QRect(20, 430, 91, 20))
        self.y_middle_edit = QLineEdit(Form)
        self.y_middle_edit.setObjectName(u"y_middle_edit")
        self.y_middle_edit.setGeometry(QRect(240, 430, 91, 20))
        self.y_range_righ = QLabel(Form)
        self.y_range_righ.setObjectName(u"y_range_righ")
        self.y_range_righ.setGeometry(QRect(470, 410, 71, 20))
        self.x_start_slider = QSlider(Form)
        self.x_start_slider.setObjectName(u"x_start_slider")
        self.x_start_slider.setGeometry(QRect(20, 460, 91, 16))
        self.x_start_slider.setOrientation(Qt.Orientation.Horizontal)
        self.x_end_slider = QSlider(Form)
        self.x_end_slider.setObjectName(u"x_end_slider")
        self.x_end_slider.setGeometry(QRect(130, 460, 91, 16))
        self.x_end_slider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_3 = QSlider(Form)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(240, 460, 91, 16))
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_4 = QSlider(Form)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setGeometry(QRect(350, 460, 91, 16))
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_5 = QSlider(Form)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setGeometry(QRect(460, 460, 91, 16))
        self.horizontalSlider_5.setOrientation(Qt.Orientation.Horizontal)
        self.signal_info = QLabel(Form)
        self.signal_info.setObjectName(u"signal_info")
        self.signal_info.setGeometry(QRect(580, 400, 71, 16))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(570, 420, 191, 111))
        self._main_debug = QPushButton(Form)
        self._main_debug.setObjectName(u"_main_debug")
        self._main_debug.setGeometry(QRect(20, 500, 75, 24))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 370, 731, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.zoomInXButton = QPushButton(self.widget)
        self.zoomInXButton.setObjectName(u"zoomInXButton")

        self.horizontalLayout.addWidget(self.zoomInXButton)

        self.zoomOutXButton = QPushButton(self.widget)
        self.zoomOutXButton.setObjectName(u"zoomOutXButton")

        self.horizontalLayout.addWidget(self.zoomOutXButton)

        self.zoomInYButton = QPushButton(self.widget)
        self.zoomInYButton.setObjectName(u"zoomInYButton")

        self.horizontalLayout.addWidget(self.zoomInYButton)

        self.zoomOutYButton = QPushButton(self.widget)
        self.zoomOutYButton.setObjectName(u"zoomOutYButton")

        self.horizontalLayout.addWidget(self.zoomOutYButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.x_start.setText(QCoreApplication.translate("Form", u"X\u8d77\u70b9", None))
        self.x_end.setText(QCoreApplication.translate("Form", u"X\u7ec8\u70b9", None))
        self.y_middle_3.setText(QCoreApplication.translate("Form", u"Y\u4e2d\u70b9", None))
        self.y_range_left.setText(QCoreApplication.translate("Form", u"Y\u8303\u56f4\uff08\u5de6\uff09", None))
        self.y_range_righ.setText(QCoreApplication.translate("Form", u"Y\u8303\u56f4\uff08\u53f3\uff09", None))
        self.signal_info.setText(QCoreApplication.translate("Form", u"\u4fe1\u53f7\u4fe1\u606f\uff1a", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4fe1\u53f7\u7c7b\u578b\uff1aECG</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4fe1\u53f7\u91c7\u6837\u7387\uff1a256Hz</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u91c7\u96c6\u65e5\u671f\uff1a24-7-8</p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u91c7\u96c6\u65f6\u95f4\uff1a21:00:23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6301\u7eed\u65f6\u957f\uff1a100s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u603b\u70b9\u6570\uff1a25600</p></body></html>", None))
        self._main_debug.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.zoomInXButton.setText(QCoreApplication.translate("Form", u"X\u8f74", None))
        self.zoomOutXButton.setText(QCoreApplication.translate("Form", u"X\u8f74", None))
        self.zoomInYButton.setText(QCoreApplication.translate("Form", u"Y\u8f74", None))
        self.zoomOutYButton.setText(QCoreApplication.translate("Form", u"Y\u8f74", None))
    # retranslateUi

