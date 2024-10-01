import tkinter as tk


def add():
  result = 10 + 5
  label_result.config(text=f"Result: {result}")


def subtract():
  result = 10 - 5
  label_result.config(text=f"Result: {result}")


def multiply():
  result = 10 * 5
  label_result.config(text=f"Result: {result}")


def divide():
  result = 10 / 5
  label_result.config(text=f"Result: {result}")


window = tk.Tk()
window.title("Simple Calculator")
window.config(bg="lightblue")

button_add = tk.Button(window, text="Add 10 + 5", command=add, bg="white")
button_add.pack(pady=5)

button_subtract = tk.Button(window,
                            text="Subtract 10 - 5",
                            command=subtract,
                            bg="white")
button_subtract.pack(pady=5)

button_multiply = tk.Button(window,
                            text="Multiply 10 * 5",
                            command=multiply,
                            bg="white")
button_multiply.pack(pady=5)

button_divide = tk.Button(window,
                          text="Divide 10 / 5",
                          command=divide,
                          bg="white")
button_divide.pack(pady=5)

label_result = tk.Label(window, text="Result: ", bg="lightblue")
label_result.pack(pady=10)

window.mainloop()
