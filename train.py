# coding = UTF*

import os
import cv2
import imutils
from imutils import paths
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split

from Brain.HandMouseClassifier import HandMouseClassifier

DATA_DIR = os.path.join(".", "Datas")
IMG_SIZE = HandMouseClassifier.IMAGE_SIZE

def load_datas():
    data = []
    labels = []
    classes = ["down", "up"]
    for label in range(len(classes)):
        class_name = classes[label]
        for image_file in paths.list_images(os.path.join(DATA_DIR, class_name)):
            image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
            image = np.expand_dims(image, axis=2)

            data.append(image)
            labels.append(label)

            # print(image_file, label)
            # print(image.shape)
            # cv2.imshow("test", image)
            # cv2.waitKey(0)
            # break
    
    data = np.array(data, dtype="float") / 255.0
    # data = np.array(data)
    labels = np.array(labels)
    # print(labels)
    # print(data.shape, labels.shape)

    return data, labels

def train():
    data, labels = load_datas()
    (x_train, x_test, y_train, y_test) = train_test_split(data, labels, test_size=0.2, random_state=0)

    print(x_train.shape, y_train.shape)
    print(x_test.shape, y_test.shape)

    print(y_test.shape)
    lb = LabelBinarizer().fit(y_train)
    one_hot = OneHotEncoder()
    y_train = one_hot.fit_transform(lb.transform(y_train)).toarray()
    y_test = one_hot.fit_transform(lb.transform(y_test)).toarray()

    # print(y_test)
    print(y_test.shape)

    handClassifier = HandMouseClassifier("./SavedModels/1.h5")
    handClassifier.train(x_train, y_train)

    print("done")
    cv2.destroyAllWindows()

def test():
    data, labels = load_datas()
    (x_train, x_test, y_train, y_test) = train_test_split(data, labels, test_size=0.2, random_state=0)

    print(x_train.shape, y_train.shape)
    print(x_test.shape, y_test.shape)

    print(y_test.shape)
    lb = LabelBinarizer().fit(y_train)
    one_hot = OneHotEncoder()
    y_train = one_hot.fit_transform(lb.transform(y_train)).toarray()
    y_test = one_hot.fit_transform(lb.transform(y_test)).toarray()

    # print(y_test)
    print(y_test.shape)

    handClassifier = HandMouseClassifier("./SavedModels/1.h5")
    y_predict = handClassifier.predict(x_test)
    i = 0
    for i in range(len(y_predict)):
        print(y_predict[i], y_test[i])
        if (y_predict[i][0] - y_predict[i][1]) * (y_test[i][0] - y_test[i][1]) > 0:
            i += 1
    print(i, i / len(y_test))

def show_train_history():
    import json
    with open("history.json", "r", encoding="utf-8") as hist_f:
        history = json.load(hist_f)
        print(history)

if __name__ == "__main__":
    # train()
    # test()
    show_train_history()
