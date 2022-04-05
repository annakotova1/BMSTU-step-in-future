from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt

class HistogramDraw:
    columns = []

    def __init__(self, histogram, scene):
        self.max_histogram_pixel_value = max(histogram)
        # for pixel_value in histogram:
        #     if histogram(pixel_value) > self.max_histogram_pixel_value:
        #         self.max_histogpam_pixel_value=histogram(pixel_value)

        # h_width = scene.width()
        # h_height = scene.height()
        self.h_width = 500
        self.h_height = 500

        column_width = self.h_width/256 - 1
        for pixel_value in range(len(histogram)):
            pixel_count = histogram[pixel_value]
            x = self.h_width/256*pixel_value
            y = self.h_height/self.max_histogram_pixel_value * pixel_count
            self.columns.append(scene.addRect(x,self.h_height-y, column_width, y,
                                              QPen(Qt.blue), QBrush(QColor(255, 0, 0, 0))))



