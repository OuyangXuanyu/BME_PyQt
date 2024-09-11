import csv
import json
import os
import sys
import zipfile
import webbrowser

import numpy as np
import pandas as pd
# import pics_ui_rc
import requests
from PySide6.QtCore import (QDateTime, QTimer)
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import (QLabel, QMessageBox, QLineEdit)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from UI_Ex.Draw_3 import Ui_Form  # 导入由pyuic6生成的UI类
from UI_main.main_ import Ui_mainMenu
from UI_main.start_ import Ui_startForm

from preprocess import FFT

# global vars
_username = ""
_password = ""
_data_location = ""
CONFIG_PATH = 'config.json'
textEdit_template = ""


# my_draw_signal = 0
#
#
# def init_Draw_window():
#     global my_draw_signal
#     my_draw_signal = MyDrawForm()


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
        self._renew_canvas = False

    def plot(self, x_data, y_data):
        self.axes.clear()
        self.axes.plot(x_data, y_data)
        self.draw()
        print(self.axes.get_ylim())

    def zoom_in_x(self):
        xlim = self.axes.get_xlim()
        self.axes.set_xlim([xlim[0] + (xlim[1] - xlim[0]) * 0.1, xlim[1] - (xlim[1] - xlim[0]) * 0.1])
        self.draw()
        return self.axes.get_xlim()

    def zoom_out_x(self):
        xlim = self.axes.get_xlim()
        self.axes.set_xlim([xlim[0] - (xlim[1] - xlim[0]) * 0.1, xlim[1] + (xlim[1] - xlim[0]) * 0.1])
        self.draw()
        return self.axes.get_xlim()

    def zoom_in_y(self):
        ylim = self.axes.get_ylim()
        print(ylim)
        self.axes.set_ylim([(ylim[0] + (ylim[1] - ylim[0]) * 0.1), (ylim[1] - (ylim[1] - ylim[0]) * 0.1)])
        self.draw()
        return self.axes.get_ylim()

    def zoom_out_y(self):
        ylim = self.axes.get_ylim()
        self.axes.set_ylim([(ylim[0] - (ylim[1] - ylim[0]) * 0.1), (ylim[1] + (ylim[1] - ylim[0]) * 0.1)])
        self.draw()
        return self.axes.get_ylim()

    def x_y_lim_range(self):
        return [self.axes.get_xlim(), self.axes.get_ylim()]

    def set_x_lim(self, x_left, x_right):
        self.axes.set_xlim([x_left, x_right])
        self.draw()

    def renew_canvas(self, x_y_range: list):
        if not self._renew_canvas:
            self._renew_canvas = True
            return
        try:
            self.axes.set_xlim([x_y_range[0], x_y_range[1]])
            self.axes.set_ylim([x_y_range[3], x_y_range[2]])
        except Exception as ex:
            print(ex)
        self.draw()

    def x_move_left(self):
        xlim = self.axes.get_xlim()
        _range_x_temp = max(xlim) - min(xlim)

        _temp_x_left_ = min(xlim) - 0.1 * _range_x_temp
        _temp_x_right_ = max(xlim) - 0.1 * _range_x_temp

        self.axes.set_xlim([_temp_x_left_, _temp_x_right_])
        self.draw()

    def x_move_right(self):
        xlim = self.axes.get_xlim()
        _range_x_temp = max(xlim) - min(xlim)

        _temp_x_left_ = min(xlim) + 0.1 * _range_x_temp
        _temp_x_right_ = max(xlim) + 0.1 * _range_x_temp

        self.axes.set_xlim([_temp_x_left_, _temp_x_right_])
        self.draw()

    def y_move_up(self):
        ylim = self.axes.get_ylim()
        print(ylim)
        _range_y_temp = max(ylim) - min(ylim)

        _temp_y_left_ = min(ylim) - 0.1 * _range_y_temp
        _temp_y_right_ = max(ylim) - 0.1 * _range_y_temp

        self.axes.set_ylim([_temp_y_left_, _temp_y_right_])
        self.draw()

    def y_move_down(self):
        ylim = self.axes.get_ylim()
        print(ylim)
        _range_y_temp = max(ylim) - min(ylim)

        _temp_y_left_ = min(ylim) + 0.1 * _range_y_temp
        _temp_y_right_ = max(ylim) + 0.1 * _range_y_temp

        self.axes.set_ylim([_temp_y_left_, _temp_y_right_])
        self.draw()


class MyStartForm(QMainWindow, Ui_startForm):
    def __init__(self, parent=None):
        super(MyStartForm, self).__init__(parent)
        self.setupUi(self)
        self.my_main = None

        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.signup_btn.clicked.connect(self.signup_btn_clicked)
        self.password_info.setEchoMode(QLineEdit.Password)

    def login_btn_clicked(self):
        # self.login_btn.setEnabled(0)
        global _username, _password
        _username = self.account_info.text()
        print(_username)
        _password = self.password_info.text()
        print(_password)

        login_info = {"username": _username, "password": _password}
        # https://www.leftthetop.asia/SC/doctor_login
        try:
            login_response = requests.post("https://www.leftthetop.asia/BME/doctor_login", json=login_info)
            print(login_response.json())
        except Exception as ex:
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText('服务器繁忙请稍后重试')
            msgbox.exec()
            return

        '''
            逻辑：
            1、检查有没有account信息，没有返回未注册 return 2
            2、检查account和password(加密后)是否对应，不对应返回密码错误 return 3
            3、成功返回登陆成功，结束当前页面进入下一页面，代入账户信息 return 1
        '''
        login_response_code = int(login_response.json()['code'])  # .咩野

        if login_response_code == 1:
            pass
        elif login_response_code == 2:
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText('用户未注册，请先进行注册操作')
            msgbox.exec()
            self.login_btn.setEnabled(1)
            return

        elif login_response_code == 3:
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText('密码输入错误，请重试！')
            msgbox.exec()
            self.login_btn.setEnabled(1)
            return

        else:
            print("Error back!")
            self.login_btn.setEnabled(1)
            return
        # my_main.pushButton.setText(_username)

        if not self.my_main:
            self.my_main = MyMainForm()
        self.my_main.title_label.setText("欢迎：" + _username + "\n使用“悦心智愈”\n抑郁症干预调控系统医用客户端")
        self.my_main.show()
        self.hide()
        # subprocess.Popen(['python', 'usetest02.py'] + ['1, 2, 3, 4, 5'])
        # sys.exit()
        # 写一个上传的request(POST)并返回成功or失败

    def signup_btn_clicked(self):
        # 写一个上传的request(POST)并返回成功or失败
        global _username, _password
        _username = self.account_info.text()
        _password = self.password_info.text()
        signup_info = {"username": str(_username), "password": str(_password)}
        signup_response = requests.post("https://www.leftthetop.asia/BME/doctor_signup", json=signup_info)

        if signup_response.status_code != 200:
            print("Wrong Server")
            return
        signup_response_info = signup_response.json()

        msgbox = QMessageBox(self)
        msgbox.setWindowTitle('提示')

        if signup_response_info['code'] == '1':
            msgbox.setText("恭喜你创建成功！")
        elif signup_response_info['code'] == '2':
            msgbox.setText("该账户已存在！")
        msgbox.exec()
        return

    '''
        逻辑：
        1、检查有没有account信息，有则返回已注册
        2、将account和password(加密后)存入数据库/csv后，返回注册成功
        （用户绑定信息）
    '''


class MyMainForm(QMainWindow, Ui_mainMenu):
    def __init__(self, parent=None):
        global _data_location
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.download_data_btn.clicked.connect(self.download_data_btn_clicked)
        self.download_report_btn.clicked.connect(self.download_report_btn_clicked)
        self.choose_location_btn.clicked.connect(self.choose_location_btn_clicked)
        self.send_report_btn.clicked.connect(self.send_report_btn_clicked)
        self.draw_signal_btn.clicked.connect(self.draw_signal_btn_clicked)
        self.log_out_btn.clicked.connect(self.log_out_btn_clicked)
        self.callback_btn.clicked.connect(self.callback_btn_clicked)

        self.suggestion_rdobtn.toggled.connect(self.suggestion_rdobtn_clicked)
        self.push_suggestion_btn.clicked.connect(self.push_suggestion_btn_clicked)

        self.my_start = my_start
        self.my_draw = None

        _data_location = os.getcwd()
        self.choose_location_info.setText("未选择路径，默认为当前程序路径：\n" + _data_location)
        # 设置状态栏
        self.statusBar()
        self.timeLabel = QLabel()
        self.statusBar().addWidget(self.timeLabel)

        # 设置默认
        self.date_info_year.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")[0:4])
        self.date_info_month.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")[5:7])
        self.date_info_day.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")[8:10])
        self.date_info_hour.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")[11:13])

        # 设置定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 每秒更新时间

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.timeLabel.setText(f"当前时间: {current_time}")

    def choose_location_btn_clicked(self):
        global _data_location
        temp_data_location = _data_location
        try:
            _data_location = QFileDialog.getExistingDirectory(self, 'Select Folder')
        except Exception as ex:
            print(ex)
        if _data_location:
            print('Folder selected:', _data_location)
        else:
            _data_location = temp_data_location
        self.choose_location_info.setText(_data_location)
        self.status_remind_text.setText(
            str(self.status_remind_text.toPlainText()) + str(self.timeLabel.text()) + '\n' + "已更改存储位置\n")

    def download_data_btn_clicked(self):
        _userid = self.userid_info.text()
        _date = f"{self.date_info_year.text()}{self.date_info_month.text()}{self.date_info_day.text()}{self.date_info_hour.text()}"
        doctor_dl_data_info = {'userid': str(_userid), 'date': str(_date)}
        response = requests.post("https://www.leftthetop.asia/BME/doctor_get_data_file", json=doctor_dl_data_info)
        self.status_remind_text.setText(str(self.status_remind_text.toPlainText()) + str(
            self.timeLabel.text()) + '\n' + f"当前用户为{_userid}，本次干预方式为：\n" + "光干预（默认蓝光）\n" + "已成功下载原始数据\n")
        if response.status_code != 200:
            print("ERROR")
            return
        print(response.headers)
        try:
            # 当文件不存在时
            print(response.json())
            return
        except Exception as ex:
            print(ex)
        print("aaaa")
        if not os.path.exists(_data_location + f"/{_userid}/{_date}/"):
            os.makedirs(_data_location + f"/{_userid}/{_date}/")
        with open(_data_location + f"/{_userid}/{_date}/" + "data.zip", 'wb') as file:
            for chunk in response.iter_content(1024):
                if chunk:
                    file.write(chunk)
        with zipfile.ZipFile(_data_location + f"/{_userid}/{_date}/" + "data.zip", 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(_data_location + f"/{_userid}/{_date}/" + "data.zip"))
        os.remove(_data_location + f"/{_userid}/{_date}/" + "data.zip")

    def download_report_btn_clicked(self):
        # _userid = self.userid_info.text()
        # _date = f"{self.date_info_year.text()}{self.date_info_month.text()}{self.date_info_day.text()}{self.date_info_hour.text()}"
        #
        # doctor_dl_data_info = {'userid': str(_userid), 'date': str(_date)}



        # response = requests.post("https://www.leftthetop.asia/SC/doctor_dl_report", json=doctor_dl_data_info)
        #
        # if response.status_code != 200:
        #     print("ERROR")
        #     msgbox = QMessageBox(self)
        #     msgbox.setWindowTitle('提示')
        #     msgbox.setText('服务器繁忙请稍后重试')
        #     msgbox.exec()
        #     return
        # print(response.headers)
        # try:
        #     print(response.json())
        # except Exception as ex:
        #     pass
        #     # print(ex)
        # if not os.path.exists(_data_location + f"/{_userid}/{_date}/"):
        #     os.makedirs(_data_location + f"/{_userid}/{_date}/")
        #
        # with open(_data_location + f"/{_userid}/{_date}/" + "分析报告.docx", 'wb') as file:
        #     for chunk in response.iter_content(1024):
        #         if chunk:
        #             file.write(chunk)
        self.status_remind_text.setText(
            str(self.status_remind_text.toPlainText()) + str(self.timeLabel.text()) + '\n' + "已下载报告\n")

    def send_report_btn_clicked(self):
        _userid = self.userid_info.text()
        _date = f"{self.date_info_year.text()}{self.date_info_month.text()}{self.date_info_day.text()}{self.date_info_hour.text()}"
        _emailaddress = self.emailaddress_info.text()

        sendemailaddress = {'userid': str(_userid), 'date': str(_date), "emailaddress": str(_emailaddress)}

        '''
        TODO
        '''
        response = requests.post("https://www.leftthetop.asia/SC/doctor_sd_report", json=sendemailaddress)

        # print(response.json())
        # if response.status_code == 200:
        #     self.status_remind_text.setText(str(self.status_remind_text.toPlainText()) + str(self.timeLabel.text()) + '\n' + f"已发送报告至{_emailaddress}\n")
        # else:
        #     self.status_remind_text.setText(str(self.status_remind_text.toPlainText()) + str(self.timeLabel.text()) + '\n' + f"发送报告失败，请重试！\n")
        #     print("ERROR")
        #     msgbox = QMessageBox(self)
        #     msgbox.setWindowTitle('提示')
        #     msgbox.setText('发送报告失败')
        #     msgbox.exec()
        self.status_remind_text.setText(str(self.status_remind_text.toPlainText()) + str(
            self.timeLabel.text()) + '\n' + f"已发送报告至{_emailaddress}\n")
    def draw_signal_btn_clicked(self):
        if not self.my_draw:
            self.my_draw = MyDrawForm(my_main=self)
        self.my_draw.show()
        self.hide()

    def log_out_btn_clicked(self):
        self.hide()
        self.my_start.show()

    def callback_btn_clicked(self):
        browser = webbrowser.get()
        browser.open("https://ouyangxuanyu.github.io/2024/04/01/callback/")

    def suggestion_rdobtn_clicked(self):
        _state = self.suggestion_rdobtn.isChecked()
        if _state:
            self.push_suggestion_btn.setEnabled(1)
            self.suggestion_textEdit.setEnabled(1)
        else:
            self.push_suggestion_btn.setEnabled(0)
            self.suggestion_textEdit.setEnabled(0)

    def push_suggestion_btn_clicked(self):
        _text = self.suggestion_textEdit.toPlainText()
        _userid = self.userid_info.text()
        _date = f"{self.date_info_year.text()}{self.date_info_month.text()}{self.date_info_day.text()}{self.date_info_hour.text()}"
        _suggestion_json = {'userid': str(_userid), 'date': str(_date), 'suggestion': str(_text)}
        push_suggestion_info = requests.post("https://www.leftthetop.asia/BME/get_doctor_suggestion", json=_suggestion_json)
        print(push_suggestion_info.json())


class MyDrawForm(QMainWindow, Ui_Form):
    def __init__(self, my_main=None, *args, **kwargs):
        # self.my_main = kwargs.get('my_main')
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.my_main = my_main
        self.x_start = 0
        self.x_end = 1000
        self.y_up = 1
        self.y_down = -1
        self.x_min = 0
        self.x_max = 1000
        self.process = False

        # Replace plotWidget with MplCanvas
        self.canvas = MplCanvas(self.plotWidget, width=5, height=4, dpi=100)
        self.verticalLayout.addWidget(self.canvas)

        self.canvas_2 = MplCanvas(self.plotWidget_2, width=5, height=4, dpi=100)
        self.verticalLayout_2.addWidget(self.canvas_2)

        # 按钮点击事件
        self.zoomInXButton.clicked.connect(self.zoom_in_x)
        self.zoomOutXButton.clicked.connect(self.zoom_out_x)
        self.zoomInYButton.clicked.connect(self.zoom_in_y)
        self.zoomOutYButton.clicked.connect(self.zoom_out_y)
        self._main_debug.clicked.connect(self.debug)
        self.get_file_path_btn.clicked.connect(self.get_file_path)
        self.x_move_left_btn.clicked.connect(self.x_move_left)
        self.x_move_right_btn.clicked.connect(self.x_move_right)
        self.y_move_up_btn.clicked.connect(self.y_move_up)
        self.y_move_down_btn.clicked.connect(self.y_move_down)
        self.back_to_main_btn.clicked.connect(self.back_to_main_btn_clicked)

        # 变化事件
        # 文本框
        self.x_start_edit.textChanged.connect(self.draw_renew_textEdit)
        self.x_end_edit.textChanged.connect(self.draw_renew_textEdit)
        self.y_range_edit_up.textChanged.connect(self.draw_renew_textEdit)
        self.y_range_edit_down.textChanged.connect(self.draw_renew_textEdit)

        self.x_start_slider.valueChanged.connect(self.draw_renew_slider)
        self.x_end_slider.valueChanged.connect(self.draw_renew_slider)
        self.y_range_up_slider.valueChanged.connect(self.draw_renew_slider)
        self.y_range_down_slider.valueChanged.connect(self.draw_renew_slider)

        # 整个流程
        # Load data from CSV file and plot it
        self.start_load()
        # self.load_data()

        self.file_path = ""
        self.signal_type = ""
        self.signal_sample_rate = ""
        self.signal_length = ""
        self.signal_date = ""
        self.signal_time = ""
        self.signal_continue_time = ""

    def start_load(self):
        self.x_end_slider.setValue(self.x_max)
        self.set_info()

    def load_data(self, _path_: str):
        data_read = []
        with open(_path_, "r", newline="") as file_read:
            reader = csv.reader(file_read)
            for row in reader:
                data_read.append(row[0])

        y_data = np.array(data_read)
        y_data = y_data.astype(np.int64)
        # y_data = abs(y_data)
        # y_data = 1000*y_data

        x_data = np.linspace(0, len(y_data) - 1, len(y_data))
        print(x_data)

        self.canvas.plot(x_data, y_data)
        canvas2_x, canvas2_y = FFT(128, y_data)
        self.canvas_2.plot(canvas2_x, canvas2_y)

        setTextEdit_info = _full_config_info["textEdit_template"].replace("{signal_type}", "ECG")
        setTextEdit_info = setTextEdit_info.replace("{signal_sample_rate}", "200")
        setTextEdit_info = setTextEdit_info.replace("{signal_date}", "2024-07-22")
        setTextEdit_info = setTextEdit_info.replace("{signal_time}", "08:56")
        setTextEdit_info = setTextEdit_info.replace("{signal_continue_time}", "3 分 12 秒")
        setTextEdit_info = setTextEdit_info.replace("{signal_length}", "38400")

        self.textEdit.setPlainText(setTextEdit_info)

        self.y_up = abs(max(y_data))
        self.y_down = 0 - self.y_up
        self.x_max = len(y_data)

        self.x_start_slider.setMaximum(len(y_data))
        self.x_end_slider.setMaximum(len(y_data))

        self.y_range_up_slider.setMaximum(int(1000 * self.y_up))
        self.y_range_down_slider.setMaximum(int(1000 * self.y_up))
        self.y_range_up_slider.setMinimum(int(1000 * self.y_down))
        self.y_range_down_slider.setMinimum(int(1000 * self.y_down))
        self.y_range_up_slider.setSingleStep(10)
        self.y_range_up_slider.setPageStep(10)

        self.y_range_up_slider.setValue(int(1000 * max(y_data)))
        self.y_range_down_slider.setValue(int(1000 * min(y_data)))
        self.x_end_slider.setValue(self.x_max)
        self.x_end_edit.setText(str(self.x_end))
        self.y_range_edit_up.setText(str(self.y_up / 1000))
        self.y_range_edit_down.setText(str(self.y_down / 1000))

    def set_info(self):
        self.textEdit.setPlainText("欢迎使用“悦心智愈”医用客户端\n信号波形绘图程序")

    def debug(self):
        # print(self.file_path)
        str_temp = self.textEdit.toPlainText()
        for i in str_temp:
            print(i, "a")
        self.textEdit.setPlainText("nihao\nwoshinibaba\ngongxifacai")
        aaa = self.canvas.x_y_lim_range()
        print(aaa[0])
        print(aaa[1])
        self.canvas.set_x_lim(0, 2000)

    def get_file_path(self):
        filters = "CSV files (*.csv)"
        csv_file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", filters)
        self.file_path = csv_file_path
        # 加载数据
        self.load_data(_path_=self.file_path)

    def draw_renew_textEdit(self):
        pass

    def draw_renew_slider(self):
        if ~self.process:
            if self.num_limit_slider() == 1:
                pass
        self.x_start = self.x_start_slider.value()
        self.x_end = self.x_end_slider.value()
        self.y_up = self.y_range_up_slider.value()
        self.y_down = self.y_range_down_slider.value()
        self.x_start_edit.setText(str(self.x_start))
        self.x_end_edit.setText(str(self.x_end))
        self.y_range_edit_up.setText(str(self.y_up / 1000))
        self.y_range_edit_down.setText(str(self.y_down / 1000))

        self.canvas.renew_canvas([self.x_start, self.x_end, self.y_up / 1000, self.y_down / 1000])

    def num_limit_slider(self):
        if self.x_start_slider.value() < self.x_min:
            self.x_start_slider.setValue(self.x_min)
            return 0
        elif self.x_end_slider.value() > self.x_max:
            self.x_end_slider.setValue(self.x_max)
            return 0
        elif self.x_start_slider.value() >= self.x_end_slider.value():
            self.x_start_slider.setValue(self.x_start)
            self.x_end_slider.setValue(self.x_end)
            return 0
        elif self.y_range_up_slider.value() < self.y_range_down_slider.value():
            self.y_range_up_slider.setValue(self.y_up)
            self.y_range_down_slider.setValue(self.y_down)
            return 0
        return 1

    def zoom_in_x(self):
        _temp_ = self.canvas.zoom_in_x()
        self.x_end_slider.setValue(int(_temp_[1]))
        self.x_end_edit.setText(str(int(_temp_[1])))
        self.x_start_slider.setValue(int(_temp_[0]))
        self.x_start_edit.setText(str(int(_temp_[0])))

    def zoom_out_x(self):
        _temp_ = self.canvas.zoom_out_x()
        self.x_end_slider.setValue(int(_temp_[1]))
        self.x_end_edit.setText(str(int(_temp_[1])))
        self.x_start_slider.setValue(int(_temp_[0]))
        self.x_start_edit.setText(str(int(_temp_[0])))

    def zoom_in_y(self):
        _temp_ = self.canvas.zoom_in_y()
        print(_temp_)
        self.y_range_up_slider.setValue(int(_temp_[1] * 1000))
        self.y_range_edit_up.setText(f"{_temp_[1]:.4f}")
        self.y_range_down_slider.setValue(int(_temp_[0] * 1000))
        self.y_range_edit_down.setText(f"{_temp_[0]:.4f}")

    def zoom_out_y(self):
        _temp_ = self.canvas.zoom_out_y()
        self.y_range_up_slider.setValue(int(_temp_[1] * 1000))
        self.y_range_edit_up.setText(f"{_temp_[1]:.4f}")
        self.y_range_down_slider.setValue(int(_temp_[0] * 1000))
        self.y_range_edit_down.setText(f"{_temp_[0]:.4f}")

    def x_move_left(self):
        self.canvas.x_move_left()

    def x_move_right(self):
        self.canvas.x_move_right()

    def y_move_up(self):
        self.canvas.y_move_up()

    def y_move_down(self):
        self.canvas.y_move_down()

    def back_to_main_btn_clicked(self):
        self.hide()
        self.my_main.show()


if __name__ == "__main__":
    with open(CONFIG_PATH, 'r', encoding='utf-8') as cf:
        _full_config_info = json.load(fp=cf)
    textEdit_template = _full_config_info["textEdit_template"]

    app_start = QApplication(sys.argv)
    # 初始化窗口
    my_start = MyStartForm()

    # 开始第一个窗口(start)
    my_start.show()

    app_start.exec()
