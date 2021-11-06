# coding = UTF8

import os
import tensorflow as tf
import json

class HandMouseClassifier:
    CLASS_MOUSE_DOWN = [1, 0]
    CLASS_MOUSE_UP = [0, 1]
    IMAGE_SIZE = 48

    def __init__(self, model_path=None) -> None:
        if model_path is None:
            self.model_path = os.path.join(".", "SavedModels", "xxx.h5")
        else:
            self.model_path = model_path

        if os.path.exists(self.model_path):
            self.model = tf.keras.models.load_model(self.model_path)
        else:
            self.model = self._build_model()

    def train(self, img, label):
        history = self.model.fit(img, label, epochs=100, batch_size=16)
        self.model.save(self.model_path)
        # print(history)
        json.dump(history.history, open("./history.json", "w+"))



    def predict(self, imgs):
        pred = self.model.predict(imgs)
        result = []
        for item in pred:
            if item[0] > item[1]:
                result.append(HandMouseClassifier.CLASS_MOUSE_DOWN)
            else:
                result.append(HandMouseClassifier.CLASS_MOUSE_UP)
        return result

    def _build_model(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.Input(shape=(self.IMAGE_SIZE, self.IMAGE_SIZE, 1, )))
        model.add(tf.keras.layers.Conv2D(64, (5, 5), activation="relu"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(3, 3), strides=2))
        model.add(tf.keras.layers.Conv2D(64, (5, 5), activation="relu"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(3, 3), strides=2))
        model.add(tf.keras.layers.Conv2D(128, (4, 4), activation="relu"))
        model.add(tf.keras.layers.Dropout(rate=0.3))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(3072, activation="relu"))
        model.add(tf.keras.layers.Dense(2, activation="softmax"))
        model.add(tf.keras.layers.Activation("softmax"))

        model.compile(optimizer="SGD", loss=tf.keras.losses.categorical_crossentropy)
        model.summary()

        return model
