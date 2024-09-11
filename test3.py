import csv
import json
import re
import sys
import pandas as pd
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from UI_Ex.Draw_3 import Ui_Form  # 导入由pyuic6生成的UI类
import numpy as np
from preprocess import FFT
import ast

CONFIG_PATH = 'config.json'

# signal_info 模板
textEdit_template = ""
file_type = ""


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

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
        self.axes.set_xlim([x_y_range[0], x_y_range[1]])
        self.axes.set_ylim([x_y_range[3], x_y_range[2]])
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




class MainWindow(QMainWindow, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

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
        global file_type
        file_type = self.judge_type(_path_)
        print(file_type)
        current_row = 0
        y_data = []

        if file_type == "ecg":
            with open(_path_, 'r', newline='') as csv_file_read:
                total_row = sum(1 for _ in open(_path_, 'r', newline=''))
                reader = csv.reader(csv_file_read)
                for row in reader:
                    current_row += 1
                    if current_row == total_row:
                        for j in range(1, len(row)):
                            result_list = ast.literal_eval(row[j])
                            print(len(result_list))
                            for k in range(1, len(result_list)-2, 2):
                                y_data.append(int(256 * int(result_list[k]) + int(result_list[k+1])))
        elif file_type == "eeg":
            with open(_path_, 'r', newline='') as csv_file_read:
                total_row = sum(1 for _ in open(_path_, 'r', newline=''))
                reader = csv.reader(csv_file_read)
                for row in reader:
                    current_row += 1
                    if current_row == total_row:
                        for j in range(1, len(row)):
                            result_list = ast.literal_eval(row[j])
                            print(len(result_list))
                            for k in range(1, len(result_list) - 2, 2):
                                y_data.append(int(256 * int(result_list[k]) + int(result_list[k + 1])))

        elif file_type == "ppg":
            with open(_path_, 'r', newline='') as csv_file_read:
                total_row = sum(1 for _ in open(_path_, 'r', newline=''))
                reader = csv.reader(csv_file_read)
                for row in reader:
                    current_row += 1
                    if current_row == total_row:
                        for j in range(1, len(row)):
                            result_list = ast.literal_eval(row[j])
                            print(len(result_list))
                            for k in range(1, len(result_list) - 1, 1):
                                y_data.append(int(result_list[k]))
        x_data = np.linspace(0, len(y_data) - 1, len(y_data))
        # print(x_data)
        # print(len(x_data), len(y_data))

        self.canvas.plot(x_data, y_data)

        self.textEdit.setPlainText(_full_config_info["file_name_template"])

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
        self.textEdit.setPlainText("欢迎使用****医用客户端\n信号查看程序")

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

    def judge_type(self, _path_):
        if "ecg" in _path_:
            return "ecg"
        elif "eeg" in _path_:
            return "eeg"
        elif "ppg" in _path_:
            return "ppg"
        elif "skin" in _path_:
            return "skin"
        return "null"


if __name__ == "__main__":
    with open(CONFIG_PATH, 'r', encoding='utf-8') as cf:
        _full_config_info = json.load(fp=cf)
    textEdit_template = _full_config_info["textEdit_template"]
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
