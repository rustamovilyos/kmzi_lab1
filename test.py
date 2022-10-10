from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Рисуем линии")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        # canvas.grid()

        for x in range(40, 600, 2):
            canvas.create_line(x, 40, x, 580, fill='black')

        for y in range(40, 600, 2):
            canvas.create_line(40, y, 580, y, fill='black')

        canvas.create_line(40, 40, 580, 40, width=2)
        canvas.create_line(40, 40, 40, 580, width=2)

        canvas.create_line(80, 260, 280, 120, width=6)
        canvas.grid(row=1, column=1, padx=10)
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("600x350")
    root.mainloop()


if __name__ == '__main__':
    main()