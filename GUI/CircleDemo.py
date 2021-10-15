# coding = UTF8

import tkinter as tk
from tkinter.constants import TRUE

class CircleDemo:
    WIDTH = 300
    HEIGHT = 300
    RADIUS = 10
    def show(self):
        window = tk.Tk()
        window.title = "GestureMouse"

        self.canvas = tk.Canvas(
            window, bg="white",
            width=self.WIDTH, height=self.HEIGHT)
        self.canvas.focus_set()
        self.canvas.pack()

        self.canvas.bind(sequence="<Button-1>", func=self._on_mouse_l_down)
        self.canvas.bind(sequence="<ButtonRelease-1>", func=self._on_mouse_l_up)
        self.canvas.bind(sequence="<B1-Motion>", func=self._on_mouse_l_move)

        self.state = {
            "mouse_down": False,
            "circle_position_x": self.WIDTH / 2,
            "circle_position_y": self.HEIGHT / 2
        }

        self._draw()

        # window.mainloop()

    def _get_state(self, key):
        if key not in self.state:
            raise BaseException("Argument Error")
        return self.state[key]

    def _set_state(self, new_state:dict={}):
        for key, _ in new_state.items():
            if key not in self.state:
                raise BaseException("Argument Error")

        old_state = self.state.copy()
        for key, value in new_state.items():
            self.state[key] = value

        position_changed = False
        for key in ["circle_position_x", "circle_position_y"]:
            if old_state[key] != self.state[key]:
                position_changed = True
        
        if position_changed:
            self._draw()

    def _draw(self):
        position_x, position_y = self._get_state("circle_position_x"), self._get_state("circle_position_y")
        x1, y1 = position_x - self.RADIUS, position_y - self.RADIUS
        x2, y2 = position_x + self.RADIUS, position_y + self.RADIUS

        self.canvas.delete("all")
        self.canvas.create_oval(x1, y1, x2, y2, fill="#FF0000")

    def _on_mouse_l_down(self, event):
        print("on_mouse_l_down", event.x, event.y)
        self.set_down()

    def _on_mouse_l_up(self, event):
        print("on_mouse_l_up", event.x, event.y)
        self.set_up()

    def _on_mouse_l_move(self, event):
        print("on_mouse_l_move", event.x, event.y)
        self.set_position(event.x, event.y)
    
    def set_down(self):
        self._set_state({"mouse_down": True})

    def set_up(self):
        self._set_state({"mouse_down": False})

    def set_position(self, x, y):
        if self._get_state("mouse_down"):
            self._set_state({
                "circle_position_x": x,
                "circle_position_y": y
            })

