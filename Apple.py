from FieldStub import FieldStub


class Apple(FieldStub):
    def __init__(self, field_x=0, field_y=0):
        super().__init__(field_x, field_y)
        self.set_image_for_apple('Apple')
