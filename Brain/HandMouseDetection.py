# coding = UTF8

import cv2
import mediapipe as mp

class HandMouseDetection:
    # 食指顶部ID
    INDEX_FINGER_TIP = 8
    MARGIN = 10
    def __init__(self) -> None:
        mp_hands= mp.solutions.hands
        self.hands = mp_hands.Hands()

    def get_position(self, img):
        ret = True
        h, w, _ = img.shape
        img_R = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = self.hands.process(img_R)
        if not result.multi_hand_landmarks:
            return False, 0, 0, (0, 0, w, h)

        # 手在的位置
        x_min, x_max, y_min, y_max = 1, 0, 1, 0
        for hand_lms in  result.multi_hand_landmarks:
            for mp_id, lm in enumerate(hand_lms.landmark):
                x_min = min(lm.x, x_min)
                x_max = max(lm.x, x_max)
                y_min = min(lm.y, y_min)
                y_max = max(lm.y, y_max)
                if mp_id == self.INDEX_FINGER_TIP:
                    x, y = int(lm.x * w), int(lm.y * h)

        x_min, x_max = int(x_min * w), int(x_max * w)
        y_min, y_max = int(y_min * h), int(y_max * h)
        
        x_min = max(0, x_min - self.MARGIN)
        x_max = min(w, x_max + self.MARGIN)
        y_min = max(0, y_min - self.MARGIN)
        y_max = min(h, y_max + self.MARGIN)
        return ret, x, y, (x_min, y_min, x_max, y_max)
