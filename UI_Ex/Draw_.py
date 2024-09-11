# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Draw_.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(771, 503)
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

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 410, 731, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.x_start = QLabel(self.widget)
        self.x_start.setObjectName(u"x_start")

        self.horizontalLayout_2.addWidget(self.x_start)

        self.x_start_edit = QLineEdit(self.widget)
        self.x_start_edit.setObjectName(u"x_start_edit")

        self.horizontalLayout_2.addWidget(self.x_start_edit)

        self.x_end = QLabel(self.widget)
        self.x_end.setObjectName(u"x_end")

        self.horizontalLayout_2.addWidget(self.x_end)

        self.x_end_edit = QLineEdit(self.widget)
        self.x_end_edit.setObjectName(u"x_end_edit")

        self.horizontalLayout_2.addWidget(self.x_end_edit)

        self.y_range = QLabel(self.widget)
        self.y_range.setObjectName(u"y_range")

        self.horizontalLayout_2.addWidget(self.y_range)

        self.y_middle_edit = QLineEdit(self.widget)
        self.y_middle_edit.setObjectName(u"y_middle_edit")

        self.horizontalLayout_2.addWidget(self.y_middle_edit)

        self.y_middle = QLabel(self.widget)
        self.y_middle.setObjectName(u"y_middle")

        self.horizontalLayout_2.addWidget(self.y_middle)

        self.y_range_edit_left = QLineEdit(self.widget)
        self.y_range_edit_left.setObjectName(u"y_range_edit_left")

        self.horizontalLayout_2.addWidget(self.y_range_edit_left)

        self.y_range_edit_right = QLineEdit(self.widget)
        self.y_range_edit_right.setObjectName(u"y_range_edit_right")

        self.horizontalLayout_2.addWidget(self.y_range_edit_right)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 370, 731, 26))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.zoomInXButton = QPushButton(self.widget1)
        self.zoomInXButton.setObjectName(u"zoomInXButton")

        self.horizontalLayout.addWidget(self.zoomInXButton)

        self.zoomOutXButton = QPushButton(self.widget1)
        self.zoomOutXButton.setObjectName(u"zoomOutXButton")

        self.horizontalLayout.addWidget(self.zoomOutXButton)

        self.zoomInYButton = QPushButton(self.widget1)
        self.zoomInYButton.setObjectName(u"zoomInYButton")

        self.horizontalLayout.addWidget(self.zoomInYButton)

        self.zoomOutYButton = QPushButton(self.widget1)
        self.zoomOutYButton.setObjectName(u"zoomOutYButton")

        self.horizontalLayout.addWidget(self.zoomOutYButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.x_start.setText(QCoreApplication.translate("Form", u"X\u8d77\u70b9", None))
        self.x_end.setText(QCoreApplication.translate("Form", u"X\u7ec8\u70b9", None))
        self.y_range.setText(QCoreApplication.translate("Form", u"Y\u4e2d\u70b9", None))
        self.y_middle.setText(QCoreApplication.translate("Form", u"Y\u8303\u56f4", None))
        self.zoomInXButton.setText(QCoreApplication.translate("Form", u"X\u8f74", None))
        self.zoomOutXButton.setText(QCoreApplication.translate("Form", u"X\u8f74", None))
        self.zoomInYButton.setText(QCoreApplication.translate("Form", u"Y\u8f74", None))
        self.zoomOutYButton.setText(QCoreApplication.translate("Form", u"Y\u8f74", None))
    # retranslateUi

