# coding = UTF8

from .HandMouseClassifier import HandMouseClassifier
from .HandMouseDetection import HandMouseDetection

# import cv2
# index = 1063

class HandMouse:
    def __init__(self, model_path) -> None:
        self.classifier = HandMouseClassifier(model_path)
        self.detection = HandMouseDetection()

    def process(self, img):
        is_mouse_down = False
        ret, x, y, position = self.detection.get_position(img)
        if not ret:
            return ret, x, y, is_mouse_down

        # 裁剪出手的位置
        sub_img = img[
            position[1]:position[3],
            position[0]:position[2],
            :
        ]

        self.classifier.predict(sub_img)
        
        # cv2.rectangle(img, (position[0], position[1]), (position[2], position[3]), (255, 0, 0), 2)
        # cv2.imshow("debug", img)
        # if cv2.waitKey(5) & 0xFF == 27:
        #     return ret, x, y, is_mouse_down

        # 数据收集
        # global index
        # cv2.imwrite("./Datas/{}.png".format(index), sub_img)
        # index += 1

        return ret, x, y, is_mouse_down
