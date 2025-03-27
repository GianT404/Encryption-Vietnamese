import os
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets

class ReportViewer(QtWidgets.QMainWindow):
    def __init__(self, stats_file="stats.json", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Báo cáo thống kê")
        self.resize(800, 600)
        self.stats_file = stats_file

        # Tạo một widget trung tâm để chứa biểu đồ
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Tạo Matplotlib Figure và Canvas
        self.figure = plt.figure(figsize=(8,6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Nút Refresh
        refresh_button = QtWidgets.QPushButton("Refresh Report")
        refresh_button.clicked.connect(self.plot_report)
        layout.addWidget(refresh_button)

        self.plot_report()

    def plot_report(self):
        # Đọc thống kê từ file JSON
        if os.path.exists(self.stats_file):
            with open(self.stats_file, "r", encoding="utf-8") as f:
                stats = json.load(f)
        else:
            stats = {}

        self.figure.clear()
        ax = self.figure.add_subplot(211)
        # Biểu đồ số lần sử dụng các thuật toán
        algorithm_usage = stats.get("algorithm_usage", {})
        if algorithm_usage:
            algorithms = list(algorithm_usage.keys())
            counts = list(algorithm_usage.values())
            ax.bar(algorithms, counts, color='skyblue')
            ax.set_title("Số lần sử dụng các thuật toán")
            ax.set_ylabel("Số lần")
        else:
            ax.text(0.5, 0.5, "Chưa có dữ liệu thống kê", horizontalalignment='center', verticalalignment='center')
        
        # # Biểu đồ thời gian mã hóa trung bình cho từng thuật toán
        # ax2 = self.figure.add_subplot(212)
        # encryption_times = stats.get("encryption_times", {})
        # avg_times = {}
        # for algo, times in encryption_times.items():
        #     if times:
        #         avg_times[algo] = sum(times)/len(times)
        # if avg_times:
        #     algorithms = list(avg_times.keys())
        #     avg_time_values = list(avg_times.values())
        #     ax2.bar(algorithms, avg_time_values, color='lightgreen')
        #     ax2.set_title("Thời gian mã hóa trung bình (giây)")
        #     ax2.set_ylabel("Thời gian (s)")
        # else:
        #     ax2.text(0.5, 0.5, "Chưa có dữ liệu thống kê", horizontalalignment='center', verticalalignment='center')
        
        self.canvas.draw()
