# coding = UTF8

from .HandMouseClassifier import HandMouseClassifier
from .HandMouseDetection import HandMouseDetection

class HandMouse:
    def __init__(self, model_path) -> None:
        self.classifier = HandMouseClassifier(model_path)
        self.detection = HandMouseDetection()

    def process(self, img):
        is_mouse_down = False
        x, y = self.detection.get_position(img)
        return x, y, is_mouse_down
