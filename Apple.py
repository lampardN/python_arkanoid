from FieldStub import FieldStub


class Apple(FieldStub):
    def __init__(self, field_x, field_y):
        super().__init__(field_x, field_y)
        self.set_image_for_apple('Apple')
