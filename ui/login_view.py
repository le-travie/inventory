from tkinter import *
from tkinter import ttk


class LoginWindow:
    def __init__(self, root: Tk):
        # Root will be the main window manager which should be passed here not not defined.
        root.title("Login")
        root.geometry("250x320")
        root.resizable(False, False)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        mainframe = ttk.Frame(root, width=250, height=320)
        mainframe.grid(column=0, row=0, sticky="NSWE")
        mainframe.columnconfigure((0, 1, 2), weight=1)
        mainframe.rowconfigure((0, 1, 2, 3), weight=1)

        self.__user_name = StringVar()
        self.__pwd = StringVar()

        input_frame = ttk.Frame(mainframe)
        input_frame.grid(column=0, row=1, columnspan=3)
        ttk.Label(input_frame, text="Username:").grid(column=0, row=0, padx=4)
        ttk.Label(input_frame, text="Password:").grid(column=0, row=1, pady=6)

        user_field = ttk.Entry(input_frame, textvariable=self.__user_name)
        pwd_field = ttk.Entry(input_frame, textvariable=self.__pwd, show="*")
        user_field.grid(column=1, row=0)
        pwd_field.grid(column=1, row=1, pady=6)

        ttk.Button(mainframe, text="Login", command=self.login, width=15).grid(
            column=1, row=2
        )

        self.error = ttk.Label(mainframe, text="").grid(columnspan=3, column=0, row=3)

        # for child in mainframe.winfo_children():
        #     child.grid_configure(padx=2, pady=2)
        user_field.focus()
        root.bind("<Return>", lambda e: self.login())

    def login(self) -> None:
        print(self.__user_name.get())
