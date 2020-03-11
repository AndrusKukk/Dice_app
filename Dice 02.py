import tkinter as tk
import random

class Dice:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.btn_text = tk.StringVar()
        self.button1 = tk.Button(
            self.frame,
            textvariable = self.btn_text,
            font = ("Impact", 60),
            bg="grey",
            width = 6,
            # height = 10,
            command = self.update_btn_text)
        self.button1.pack()
        self.frame.pack()
        
        self.btn_text.set("Click!")
        
    def update_btn_text(self):
         self.btn_text.set(str(random.randint(1, 6)))


def main(): 
    root = tk.Tk()
    app = Dice(root)
    root.mainloop()

if __name__ == '__main__':
    main()
