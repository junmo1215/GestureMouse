# coding = UTF8

import os

class HandMouseClassifier:
    CLASS_MOUSE_UP = [1, 0]
    CLASS_MOUSE_DOWN = [0, 1]

    def __init__(self, model_path) -> None:
        self.model_path = model_path

        if os.path.exists(model_path):
            self.model = self._build_model()

    def train(self):
        pass

    def classify(self):
        pass

    def _build_model():
        pass
