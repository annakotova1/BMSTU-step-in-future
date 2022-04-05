
import itertools
from PIL import Image
from dotmap import DotMap

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPen


class BarcodeFinder():

    state = DotMap()
    def __init__(self, image_filename):
        self.state.image = Image.open(image_filename)  # PIL:Image изображение в формате библиотеки PIL
        self.state.image_width = self.state.image.size[0]
        self.state.image_height = self.state.image.size[1]
        self.set_settings(20, "horizontal")

    def set_settings(self, blockCount, orientation):
        blockSize = int(min(self.state.image_width, self.state.image_height)/blockCount)

        if orientation == "horizontal":
            self.state.horizontal_step = blockSize * 2
            self.state.vertical_step = blockSize
        elif orientation == "vertical":
            self.state.horizontal_step = blockSize
            self.state.vertical_step = blockSize * 2
        else:
            self.state.horizontal_step = blockSize
            self.state.vertical_step = blockSize

        # кол-во блоков в высоте картинки
        self.state.height_step_count = int(self.state.image_height / self.state.vertical_step)
        # кол-во блоков в ширине картинки
        self.state.width_step_count = int(self.state.image_width / self.state.horizontal_step)

    def convert_image_to_bw(self):
        # Изображение в двух битах преобразованное по средней точке
        self.state.image_gray = self.state.image.convert('L')  # PIL:Image изображение с серыми пикселями
        self.state.image_bw = self.state.image_gray.point(lambda x: 0 if x < 128 else 255, '1')
        self.state.bw_pixel_list = tuple(self.state.image_bw.getdata())  # массив содержащий 1 или 0 для каждого пикселя изображения

    def calculate_blocks_statistics(self, method_state):
        blocks_statistics = DotMap()
        blocks_statistics.math_waiting = [[0] * method_state.height_step_count
                                         for i in range(method_state.width_step_count)]
        blocks_statistics.max_math_waiting = 0

        blocks_statistics.dispersions = [[0] * method_state.height_step_count
                                         for i in range(method_state.width_step_count)]
        blocks_statistics.min_dispersion = method_state.horizontal_step**2
        blocks_statistics.max_dispersion = 0

        gradient_array = [[0] * method_state.image_height for i in
                                                 range(method_state.width_step_count)]

        for width_step_num in range(method_state.width_step_count):
            for height_pixel_num in range(method_state.image_height):
                row_start = height_pixel_num * method_state.image_width + method_state.horizontal_step * width_step_num

                bw_pixel_slice = method_state.bw_pixel_list[row_start:row_start+method_state.horizontal_step-1]  # все пиксели данной строки
                lenght = len(list(itertools.groupby(bw_pixel_slice)))  # кол-во групп пикселей в строке
                gradient_array[width_step_num][height_pixel_num] = lenght  # группы пикселей в данной сторке данного блока

        for width_step_num in range(method_state.width_step_count):
            for height_step_num in range(method_state.height_step_count):
                sum = 0

                for vertical_delta in range(method_state.vertical_step):
                    sum += gradient_array[width_step_num][height_step_num * method_state.vertical_step + vertical_delta]

                # Математическое ожидание
                average = sum / method_state.vertical_step
                blocks_statistics.math_waiting[width_step_num][height_step_num] = average
                if blocks_statistics.max_math_waiting < average:
                    blocks_statistics.max_math_waiting = average

                quad_sum = 0
                for vertical_delta in range(method_state.vertical_step):
                    quad_sum += (gradient_array[width_step_num][
                                 height_step_num * method_state.vertical_step + vertical_delta] - average) ** 2

                # Дисперсия
                dispersion = quad_sum/method_state.vertical_step
                blocks_statistics.dispersions[width_step_num][height_step_num] = dispersion
                if float(blocks_statistics.min_dispersion) > dispersion:
                    blocks_statistics.min_dispersion = dispersion

                if float(blocks_statistics.max_dispersion) < dispersion:
                    blocks_statistics.max_dispersion = dispersion

        return blocks_statistics





