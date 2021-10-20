# coding = UTF8

import cv2
import numpy as np

from GUI import CircleDemo
from Brain import HandMouse

class Player():
    def __init__(self, cam=0, model_path="") -> None:
        """
        cam: camera name or index
        """
        # if last mouse state is down
        # use this state compare with newest state fot generating mouse event
        self.last_mouse_is_down = False

        self.game = CircleDemo()
        self.capture = cv2.VideoCapture(cam)
        self.brain = HandMouse(model_path)

    def play(self):
        while True:
            # read hand state from camera
            ret, frame = self.capture.read()
            # if ret
            #     break

            x, y, is_mouse_down = self.brain.process(frame)

            if is_mouse_down != self.last_mouse_is_down:
                # trigger mouse up/down event when state change
                if is_mouse_down:
                    self.game.set_down()
                else:
                    self.game.set_up()
                self.last_mouse_is_down = is_mouse_down

            self.game.set_position(x, y)

def main():
    circle_demo = CircleDemo()
    circle_demo.show()

    while True:
        cmd = input(">>> ")
        if cmd == "q":
            break

        try:
            if cmd == "d":
                circle_demo.set_down()
            elif cmd == "u":
                circle_demo.set_up()
            elif cmd.startswith("p"):
                arr = cmd.split(" ")
                x, y = int(arr[1]), int(arr[2])
                circle_demo.set_position(x, y)
        except Exception as ex:
            print("ex:", ex)

if __name__ == "__main__":
    main()
    # player = Player()
    # player.play()
