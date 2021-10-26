# coding = UTF8

import cv2
import mediapipe as mp

class HandMouseDetection:
    def __init__(self) -> None:
        myHands= mp.solutions.hands
        self.hands = myHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def get_position(self, img):
        img_R = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = self.hands.process(img_R)
        if result.multi_hand_landmarks:
            for handLms in  result.multi_hand_landmarks:
                for id,lm in enumerate(handLms.landmark):
                    if id == 8:
                        # 食指
                        h, w, _ = img.shape
                        x, y = int(lm.x * w), int(lm.y * h)
        else:
            x, y = 0, 0
        return x, y
