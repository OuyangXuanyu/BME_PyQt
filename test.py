import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from UI_Ex.Draw_ import Ui_Form  # 导入由pyuic6生成的UI类
import numpy as np


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

    def zoom_in_x(self):
        xlim = self.axes.get_xlim()
        self.axes.set_xlim([xlim[0] + (xlim[1] - xlim[0]) * 0.1, xlim[1] - (xlim[1] - xlim[0]) * 0.1])
        self.draw()

    def zoom_out_x(self):
        xlim = self.axes.get_xlim()
        self.axes.set_xlim([xlim[0] - (xlim[1] - xlim[0]) * 0.1, xlim[1] + (xlim[1] - xlim[0]) * 0.1])
        self.draw()

    def zoom_in_y(self):
        ylim = self.axes.get_ylim()
        self.axes.set_ylim([(ylim[0] + (ylim[1] - ylim[0]) * 0.1)/1000, (ylim[1] - (ylim[1] - ylim[0]) * 0.1)/1000])
        self.draw()

    def zoom_out_y(self):
        ylim = self.axes.get_ylim()
        self.axes.set_ylim([(ylim[0] - (ylim[1] - ylim[0]) * 0.1)/1000, (ylim[1] + (ylim[1] - ylim[0]) * 0.1)/1000])
        self.draw()


class MainWindow(QMainWindow, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Replace plotWidget with MplCanvas
        self.canvas = MplCanvas(self.plotWidget, width=5, height=4, dpi=100)
        self.verticalLayout.addWidget(self.canvas)

        # Connect buttons to zoom functions
        self.zoomInXButton.clicked.connect(self.canvas.zoom_in_x)
        self.zoomOutXButton.clicked.connect(self.canvas.zoom_out_x)
        self.zoomInYButton.clicked.connect(self.canvas.zoom_in_y)
        self.zoomOutYButton.clicked.connect(self.canvas.zoom_out_y)

        # Load data from CSV file and plot it
        self.load_data()

    def load_data(self):
        # Assuming the CSV file has two columns: 'x' and 'y'
        data = pd.read_csv('eegsignals.csv')
        y_data = data['y'].values
        print(y_data)
        x_data = np.linspace(0, len(y_data) - 1, len(y_data))
        self.canvas.plot(x_data, y_data)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())
