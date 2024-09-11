# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Draw_3.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1161, 502)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 651, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plotWidget = QWidget(self.verticalLayoutWidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.plotWidget)

        self.x_start_Label = QLabel(Form)
        self.x_start_Label.setObjectName(u"x_start_Label")
        self.x_start_Label.setGeometry(QRect(50, 380, 32, 20))
        self.x_end_Label = QLabel(Form)
        self.x_end_Label.setObjectName(u"x_end_Label")
        self.x_end_Label.setGeometry(QRect(160, 380, 32, 20))
        self.y_range_up_Label = QLabel(Form)
        self.y_range_up_Label.setObjectName(u"y_range_up_Label")
        self.y_range_up_Label.setGeometry(QRect(250, 380, 71, 20))
        self.x_end_edit = QLineEdit(Form)
        self.x_end_edit.setObjectName(u"x_end_edit")
        self.x_end_edit.setGeometry(QRect(130, 400, 91, 20))
        self.y_range_edit_down = QLineEdit(Form)
        self.y_range_edit_down.setObjectName(u"y_range_edit_down")
        self.y_range_edit_down.setGeometry(QRect(350, 400, 91, 20))
        self.y_range_edit_up = QLineEdit(Form)
        self.y_range_edit_up.setObjectName(u"y_range_edit_up")
        self.y_range_edit_up.setGeometry(QRect(240, 400, 91, 20))
        self.x_start_edit = QLineEdit(Form)
        self.x_start_edit.setObjectName(u"x_start_edit")
        self.x_start_edit.setGeometry(QRect(20, 400, 91, 20))
        self.y_range_down_Label = QLabel(Form)
        self.y_range_down_Label.setObjectName(u"y_range_down_Label")
        self.y_range_down_Label.setGeometry(QRect(360, 380, 71, 20))
        self.x_start_slider = QSlider(Form)
        self.x_start_slider.setObjectName(u"x_start_slider")
        self.x_start_slider.setGeometry(QRect(20, 430, 91, 16))
        self.x_start_slider.setMaximum(999)
        self.x_start_slider.setValue(0)
        self.x_start_slider.setOrientation(Qt.Orientation.Horizontal)
        self.x_end_slider = QSlider(Form)
        self.x_end_slider.setObjectName(u"x_end_slider")
        self.x_end_slider.setGeometry(QRect(130, 430, 91, 16))
        self.x_end_slider.setMinimum(1)
        self.x_end_slider.setMaximum(1000)
        self.x_end_slider.setOrientation(Qt.Orientation.Horizontal)
        self.y_range_up_slider = QSlider(Form)
        self.y_range_up_slider.setObjectName(u"y_range_up_slider")
        self.y_range_up_slider.setGeometry(QRect(240, 430, 91, 16))
        self.y_range_up_slider.setOrientation(Qt.Orientation.Horizontal)
        self.y_range_down_slider = QSlider(Form)
        self.y_range_down_slider.setObjectName(u"y_range_down_slider")
        self.y_range_down_slider.setGeometry(QRect(350, 430, 91, 16))
        self.y_range_down_slider.setOrientation(Qt.Orientation.Horizontal)
        self.signal_info = QLabel(Form)
        self.signal_info.setObjectName(u"signal_info")
        self.signal_info.setGeometry(QRect(580, 370, 71, 16))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(560, 390, 191, 101))
        self._main_debug = QPushButton(Form)
        self._main_debug.setObjectName(u"_main_debug")
        self._main_debug.setGeometry(QRect(760, 410, 75, 24))
        self.get_file_path_btn = QPushButton(Form)
        self.get_file_path_btn.setObjectName(u"get_file_path_btn")
        self.get_file_path_btn.setGeometry(QRect(760, 470, 75, 24))
        self.zoomOutYButton = QPushButton(Form)
        self.zoomOutYButton.setObjectName(u"zoomOutYButton")
        self.zoomOutYButton.setGeometry(QRect(1060, 420, 61, 24))
        self.zoomInYButton = QPushButton(Form)
        self.zoomInYButton.setObjectName(u"zoomInYButton")
        self.zoomInYButton.setGeometry(QRect(990, 420, 61, 24))
        self.zoomInXButton = QPushButton(Form)
        self.zoomInXButton.setObjectName(u"zoomInXButton")
        self.zoomInXButton.setGeometry(QRect(850, 420, 61, 24))
        self.zoomOutXButton = QPushButton(Form)
        self.zoomOutXButton.setObjectName(u"zoomOutXButton")
        self.zoomOutXButton.setGeometry(QRect(920, 420, 61, 24))
        self.x_move_right_btn = QPushButton(Form)
        self.x_move_right_btn.setObjectName(u"x_move_right_btn")
        self.x_move_right_btn.setGeometry(QRect(930, 460, 51, 24))
        self.x_move_left_btn = QPushButton(Form)
        self.x_move_left_btn.setObjectName(u"x_move_left_btn")
        self.x_move_left_btn.setGeometry(QRect(870, 460, 51, 24))
        self.y_move_down_btn = QPushButton(Form)
        self.y_move_down_btn.setObjectName(u"y_move_down_btn")
        self.y_move_down_btn.setGeometry(QRect(1050, 460, 51, 24))
        self.y_move_up_btn = QPushButton(Form)
        self.y_move_up_btn.setObjectName(u"y_move_up_btn")
        self.y_move_up_btn.setGeometry(QRect(990, 460, 51, 24))
        self.back_to_main_btn = QPushButton(Form)
        self.back_to_main_btn.setObjectName(u"back_to_main_btn")
        self.back_to_main_btn.setGeometry(QRect(760, 440, 71, 24))
        self.confirm_btn = QPushButton(Form)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(470, 410, 61, 24))
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(680, 10, 471, 341))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plotWidget_2 = QWidget(self.verticalLayoutWidget_2)
        self.plotWidget_2.setObjectName(u"plotWidget_2")
        self.plotWidget_2.setAutoFillBackground(True)

        self.verticalLayout_2.addWidget(self.plotWidget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.x_start_Label.setText(QCoreApplication.translate("Form", u"X\u8d77\u70b9", None))
        self.x_end_Label.setText(QCoreApplication.translate("Form", u"X\u7ec8\u70b9", None))
        self.y_range_up_Label.setText(QCoreApplication.translate("Form", u"Y\u8303\u56f4\uff08\u4e0a\uff09", None))
        self.y_range_down_Label.setText(QCoreApplication.translate("Form", u"Y\u8303\u56f4\uff08\u4e0b\uff09", None))
        self.signal_info.setText(QCoreApplication.translate("Form", u"\u4fe1\u53f7\u4fe1\u606f\uff1a", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self._main_debug.setText(QCoreApplication.translate("Form", u"DEBUG", None))
        self.get_file_path_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.zoomOutYButton.setText(QCoreApplication.translate("Form", u"Y\u8f74\u7f29\u5c0f", None))
        self.zoomInYButton.setText(QCoreApplication.translate("Form", u"Y\u8f74\u653e\u5927", None))
        self.zoomInXButton.setText(QCoreApplication.translate("Form", u"X\u8f74\u4f38\u957f", None))
        self.zoomOutXButton.setText(QCoreApplication.translate("Form", u"X\u8f74\u7f29\u77ed", None))
        self.x_move_right_btn.setText(QCoreApplication.translate("Form", u"\u53f3\u79fb", None))
        self.x_move_left_btn.setText(QCoreApplication.translate("Form", u"\u5de6\u79fb", None))
        self.y_move_down_btn.setText(QCoreApplication.translate("Form", u"\u4e0b\u79fb", None))
        self.y_move_up_btn.setText(QCoreApplication.translate("Form", u"\u4e0a\u79fb", None))
        self.back_to_main_btn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u4e3b\u754c\u9762", None))
        self.confirm_btn.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
    # retranslateUi

