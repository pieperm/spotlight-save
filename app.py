from tkinter import *


class App(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets(master)

    def create_widgets(self, master=None):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        header_canvas = Canvas(master,
                               width=screen_width,
                               height=screen_height / 4)
        header_canvas.pack()
        header_canvas.create_rectangle(0, 0, screen_width, screen_height, fill="blue")

        title_label = Label(header_canvas,
                            text="Spotlight Save",
                            font=("Helvetica", 20))
        title_label.pack()


root = Tk()
app = App(master=root)
app.master.title("Spotlight Save")
app.master.size(800, 600)
app.master.resizable = False
app.mainloop()
