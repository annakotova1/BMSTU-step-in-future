from dotmap import DotMap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QBrush, QColor, QPen
from Ui_MainWindow import Ui_MainWindow
from BarcodeFinder import BarcodeFinder
from BlockLayer import BlockLayer
from HistogramDraw import HistogramDraw

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()



class Controller:

    barcodeFinder = None
    logger = None
    mainWindow = None

    def __init__(self):
        self.logger = self.dummy_logger
        pass

    def show_gui(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.ui = Ui_MainWindow()
        self.ui.controller = self
        self.ui.setupUi(self.main_window)


    def set_image(self,image_filename):
        self.barcodeFinder = BarcodeFinder(image_filename)

    def isImageSet(self):
        if self.barcodeFinder:
            return True
        else:
            return False

    def calculate_horizontal_analize_data(self):
        method_fields = ("image_height",      "image_width",
                         "height_step_count", "width_step_count",
                         "horizontal_step",   "vertical_step",
                         "bw_pixel_list")
        method_state = DotMap()
        for field in method_fields:
            method_state[field] = self.barcodeFinder.state[field]
        method_state.blocks_statistics = self.barcodeFinder.calculate_blocks_statistics(method_state)
        return method_state

    def calculate_vertical_analize_data(self):
        swap_fields = {"height_step_count": "width_step_count",
                       "horizontal_step":   "vertical_step"}
        method_state = DotMap()

        for state_field, method_field in swap_fields.items():
            method_state[method_field] = self.barcodeFinder.state[state_field]
        for method_field, state_field in swap_fields.items():
            method_state[method_field] = self.barcodeFinder.state[state_field]

        crop_width = self.barcodeFinder.state.width_step_count * self.barcodeFinder.state.horizontal_step
        crop_height = self.barcodeFinder.state.height_step_count * self.barcodeFinder.state.vertical_step

        method_state.image_width = crop_height
        method_state.image_height = crop_width

        crop_box = (0,
                    0,
                    crop_width,
                    crop_height
                    )

        rotated_image = self.barcodeFinder.state.image_bw.crop(crop_box).rotate(270, 0, 1)
        rotated_image.save("rotated.png")
        method_state.bw_pixel_list = tuple(rotated_image.getdata())
        method_state.blocks_statistics = self.barcodeFinder.calculate_blocks_statistics(method_state)
        return method_state

    def calculate(self):
        if self.barcodeFinder is None:
            return False
        self.logger("Конвертируем изображение в черно-белое.")
        self.barcodeFinder.convert_image_to_bw()
        self.logger("Вычисляем матожидание и дисперсию смены цвета пикселей в строках блоков.")
        self.barcodeFinder.state.horizontal_analize_data = self.calculate_horizontal_analize_data()
        self.logger("Вычисляем матожидание и дисперсию смены цвета пикселей в столбцах блоков.")
        self.barcodeFinder.state.vertical_analize_data = self.calculate_vertical_analize_data()
        pass

    def dummy_logger(self, message):
        print(message)

    def set_logger(self, logger):
        self.logger = logger

    def draw_layers(self, scene):
        layers = {}
        hstep = self.barcodeFinder.state.horizontal_step
        vstep = self.barcodeFinder.state.vertical_step
        st = self.barcodeFinder.state
        hstat = st.horizontal_analize_data.blocks_statistics
        vstat = st.vertical_analize_data.blocks_statistics
        blocks = [[DotMap(zero=0) for j in range(st.height_step_count)]
                  for i in range(st.width_step_count)]
        st.math_waiting_delta_min = 255
        st.math_waiting_delta_max = 0
        st.math_waiting_delta = [[0 for j in range(st.height_step_count)]
                  for i in range(st.width_step_count)]

        max_block_weight = 0
        max_math_waiting = max(hstat.max_math_waiting, vstat.max_math_waiting)
        for row, blocks_row in enumerate(blocks):
            columns_count = len(blocks_row)
            for column, block in enumerate(blocks_row):
                v_column = columns_count-1-column
                block.math_waiting_h = hstat.math_waiting[row][column]
                block.math_waiting_v = vstat.math_waiting[v_column][row]
                block.dispersion_h = hstat.dispersions[row][column]
                block.dispersion_v = vstat.dispersions[v_column][row]
                block.math_waiting_delta = block.math_waiting_h/hstep - block.math_waiting_v/vstep

                if abs(block.math_waiting_delta) < abs(st.math_waiting_delta_min):
                    st.math_waiting_delta_min = block.math_waiting_delta
                if abs(block.math_waiting_delta) > abs(st.math_waiting_delta_max):
                    st.math_waiting_delta_max = block.math_waiting_delta

        h_good_dispersion = hstat.min_dispersion+(hstat.max_dispersion-hstat.min_dispersion)*0.2
        v_good_dispersion = vstat.min_dispersion+(vstat.max_dispersion-vstat.min_dispersion)*0.2
        delta_dif = abs(st.math_waiting_delta_max)-abs(st.math_waiting_delta_min)

        for row, blocks_row in enumerate(blocks):
            for column, block in enumerate(blocks_row):
                if block.math_waiting_delta > 0:
                    block.barcode_vertical = False
                    if block.dispersion_h < h_good_dispersion:
                        block.weight = block.math_waiting_h/max_math_waiting*0.3 + \
                               abs(block.math_waiting_delta)/abs(st.math_waiting_delta_max)*0.9
                    else:
                        block.weight = 0
                else:
                    block.barcode_vertical = True
                    if block.dispersion_h < h_good_dispersion:
                        block.weight = block.math_waiting_v/max_math_waiting*0.3 + \
                               abs(block.math_waiting_delta)/abs(st.math_waiting_delta_max)*0.9
                    else:
                        block.weight = 0

                max_block_weight = max(block.weight, max_block_weight)

        for row, blocks_row in enumerate(blocks):
            for column, block in enumerate(blocks_row):
                block.math_waiting_delta_opacity = 128 - (abs(block.math_waiting_delta)-abs(st.math_waiting_delta_min)) / delta_dif * 128
                block.math_waiting_h_opacity = 128 - block.math_waiting_h / hstat.max_math_waiting * 128
                block.math_waiting_v_opacity = 128 - block.math_waiting_v / vstat.max_math_waiting * 128

                if block.dispersion_h < h_good_dispersion:
                    opacity = 0
                else:
                    opacity = 128
                block.dispersion_opacity_h = opacity

                if block.dispersion_v < v_good_dispersion:
                    opacity = 0
                else:
                    opacity = 128

                block.dispersion_opacity_v = opacity

                block.weight_opacity = 128 - block.weight/max_block_weight*128

                if block.weight > max_block_weight*0.6:
                    block.has_barcode = True

                    if block.barcode_vertical:
                        block.has_barcode_opacity = 100
                    else:
                        block.has_barcode_opacity = 200
                else:
                    block.has_barcode = False
                    block.has_barcode_opacity = 0

        barcode_regions = {"vertical": DotMap(), "horizontal": DotMap()}

        for region_name, barcode_region in barcode_regions.items():
            barcode_region.min_row = -1
            barcode_region.max_row = -1
            barcode_region.min_column = -1
            barcode_region.max_column = -1

        for row, blocks_row in enumerate(blocks):
            for column, block in enumerate(blocks_row):
                if block.barcode_vertical:
                    barcode_region = barcode_regions["vertical"]
                else:
                    barcode_region = barcode_regions["horizontal"]
                if block.has_barcode:
                    if (row < barcode_region.min_row) or (barcode_region.min_row == -1) :
                        barcode_region.min_row = row
                    elif row > barcode_region.max_row:
                        barcode_region.max_row = row
                    if (column < barcode_region.min_column) or (barcode_region.min_column == -1):
                        barcode_region.min_column = column
                    elif column > barcode_region.max_column:
                        barcode_region.max_column = column

        for row, blocks_row in enumerate(blocks):
            for column, block in enumerate(blocks_row):
                for region_name, barcode_region in barcode_regions.items():
                    if (row >= barcode_region.min_row) and (row <= barcode_region.max_row) and \
                            (column >= barcode_region.min_column) and (column <= barcode_region.max_column):
                        block["barcode_opacity_"+region_name] = 0
                    else:
                        block["barcode_opacity_"+region_name] = 128

        for row, blocks_row in enumerate(blocks):
            for column, block in enumerate(blocks_row):
                for region_name, barcode_region in barcode_regions.items():

                    if ((barcode_region.max_row+1)*hstep) > st.image_width:
                        max_x = barcode_region.max_row
                    else:
                        max_x = barcode_region.max_row +1
                    if ((barcode_region.max_column + 1) * vstep) > st.image_height:
                        max_y = barcode_region.max_column
                    else:
                        max_y = barcode_region.max_column+1
                    if (row >= barcode_region.min_row-1) and (row <= max_x) and (column >= barcode_region.min_column-1) and (column <= max_y):
                        block["full_barcode_opacity_"+region_name] = 0
                    else:
                        block["full_barcode_opacity_"+region_name] = 128

        layers["01. Границы блоков"] = BlockLayer(
                            hstep, vstep,
                            blocks,"zero", scene, QPen(Qt.blue), QBrush(QColor(255, 0, 0, 0))
                          )

        layers["02. Матожидание (строки)"] = BlockLayer(
                            hstep, vstep,
                            blocks,"math_waiting_h_opacity",
                            scene, QPen(Qt.transparent),
                            QBrush(QColor(255, 255, 0, 0)), "math_waiting_h"
                          )

        layers["03. Матожидание (столбцы)"] = BlockLayer(
                            hstep, vstep,
                            blocks, "math_waiting_v_opacity",
                            scene, QPen(Qt.transparent),
                            QBrush(QColor(255, 255, 0, 0)), "math_waiting_v"
                          )

        layers["04. Разность матожиданий"] = BlockLayer(
                            hstep, vstep,
                            blocks, "math_waiting_delta_opacity", scene, QPen(Qt.transparent), QBrush(QColor(0, 0, 255, 0)), "math_waiting_delta"
                          )


        layers["06. Дисперсия (строки)"] = BlockLayer(
                            hstep, vstep,
                            blocks, "dispersion_opacity_h", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
                          )
        layers["07. Дисперсия (столбцы)"] = BlockLayer(
                            hstep, vstep,
                            blocks,"dispersion_opacity_v", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
                          )

        layers["08. Веса блоков"] = BlockLayer(
                            hstep, vstep,
                            blocks, "weight_opacity", scene, QPen(Qt.transparent), QBrush(QColor(0, 0, 255, 0)), "weight"
                          )

        layers["09. Внутренние блоки штрихкода"] = BlockLayer(
                            hstep, vstep,
                            blocks, "has_barcode_opacity", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
                          )

        layers["10. Блоки горизонтального штрихкода"] = BlockLayer(
            hstep, vstep,
            blocks, "barcode_opacity_horizontal", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
            )

        layers["11. Блоки вертикального штрихкода"] = BlockLayer(
            hstep, vstep,
            blocks, "barcode_opacity_vertical", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
            )

        layers["12. Штрихкод горизонтальный"] = BlockLayer(
            hstep, vstep,
            blocks, "full_barcode_opacity_horizontal", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
        )

        layers["13. Штрихкод вертикальный"] = BlockLayer(
            hstep, vstep,
            blocks, "full_barcode_opacity_vertical", scene, QPen(Qt.transparent), QBrush(QColor(0, 255, 0, 0))
        )

        layers["12. Штрихкод горизонтальный"].show()

        return layers

    def draw_histogram(self, scene):
        return HistogramDraw(self.barcodeFinder.state.image_gray.histogram(), scene)

