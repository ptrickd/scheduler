from Window import Main_Frame


class Main_Window(Main_Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
    pass
