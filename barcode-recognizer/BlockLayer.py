class BlockLayer():


    def __init__(self, block_width, block_height, blocks, opacity_field, scene, pen, brush, value_column = False):
        self.primitives = []
        self.isVisible = None

        brush_color = brush.color()
        for column, blocks_column in enumerate(blocks):
            for row, block in enumerate(blocks_column):
                block_color = brush.color()
                block_color.setAlpha(block[opacity_field])
                brush.setColor(block_color)
                block_rect = scene.addRect(column * block_width,
                              row * block_height,
                              block_width,
                              block_height,
                              pen,
                              brush)
                block_rect.setVisible(False)
                self.primitives.append(block_rect)
                if value_column != False:
                    block_text = scene.addText(str(round(block[value_column], 3)))
                    block_text.setPos(column*block_width, row*block_height)
                    block_text.setVisible(False)
                    self.primitives.append(block_text)
        brush.setColor(brush_color)
        self.isVisible = False


    def _set_primitives_visiblity(self, primitives, is_visible):
        for primitive in primitives:
            primitive.setVisible(is_visible)

    def show(self):
        if not self.isVisible:
            self.isVisible = True
            self._set_primitives_visiblity(self.primitives, self.isVisible)

    def hide(self):
        if self.isVisible:
            self.isVisible = False
            self._set_primitives_visiblity(self.primitives, self.isVisible)








