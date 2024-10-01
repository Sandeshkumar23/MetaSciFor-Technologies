import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")

        self.pen_color = "black"
        self.eraser_color = "white"
        self.brush_size = 2

        self.setup_ui()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.start_paint)

    def setup_ui(self):
        self.frame = tk.Frame(self.root, width=200, height=400)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)
        
        pen_button = tk.Button(self.frame, text="pen", command=self.use_pen)
        pen_button.pack(pady=5)

        brush_button = tk.Button(self.frame, text="brush", command=self.use_brush)
        brush_button.pack(pady=5)

        color_button = tk.Button(self.frame, text="color", command=self.choose_color)
        color_button.pack(pady=5)

        eraser_button = tk.Button(self.frame, text="eraser", command=self.use_eraser)
        eraser_button.pack(pady=5)

        self.size_slider = tk.Scale(self.frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Pen Size")
        self.size_slider.pack(pady=5)

        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
    def use_pen(self):
        self.pen_color = "black"
    
    def use_brush(self):
        self.pen_color = "black"
        self.brush_size = self.size_slider.get()
    
    def choose_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]
    
    def use_eraser(self):
        self.pen_color = self.eraser_color
    
    def change_size(self, e):
        self.brush_size = self.size_slider.get()
    
    def start_paint(self, event):
        self.x = event.x
        self.y = event.y

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_line(self.x, self.y, event.x, event.y, fill=self.pen_color, width=self.brush_size)
        self.x = event.x
        self.y = event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
