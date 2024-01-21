from tkinter import *
from tkinter import ttk
from typing import List

from .table_comp import TableComponent


class MainView:
    """
    Main screen for the app. Pass the tkinter root/Tk object to the constructor.
    """

    ## To do: Add side bar (for navigation between transfers and assets), search bar, menu.
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("IT Asset Manager")
        self.root.geometry("1200x800")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        # self.main_frame.columnconfigure(0, weight=2)
        self.main_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.main_frame.grid(row=0, column=0, sticky="NSEW")
        self.render_table()

    def render_table(self):
        table_columns = ("id", "descript", "location", "remarks", "date_in")
        self.table = TableComponent(
            self.main_frame,
            columns=table_columns,
            show="headings",
        )
        self.table.heading("id", text="ID")
        self.table.heading("descript", text="Description")
        self.table.heading("location", text="Location")
        self.table.heading("remarks", text="Remarks")
        self.table.heading("date_in", text="Date In")

        data = [
            {
                "id": 1,
                "descript": "Desktop PC",
                "location": "Secretary",
                "remarks": "For workuse",
                "date_in": "12/05/2021",
            },
            {
                "id": 2,
                "descript": "Laptop",
                "location": "Manager",
                "remarks": "For work use",
                "date_in": "12/05/2021",
            },
        ]

        for i in range(len(data)):
            id = data[i]["id"]
            descript = data[i]["descript"]
            location = data[i]["location"]
            remarks = data[i]["remarks"]
            date_in = data[i]["date_in"]
            self.table.insert(
                "",
                "end",
                values=(id, descript, location, remarks, date_in),
                tags=("even" if i % 2 == 0 else "odd"),
            )

        self.table.row_colour("#E1F0DA", "#EEF5FF")
        self.table.grid(column=1, row=0, columnspan=5, rowspan=5, sticky="NSEW")
        self.table.bind("<<TreeviewSelect>>", lambda _: self.table.get_selection())
        self.table.bind("<Delete>", lambda _: self.delete_selected())

    def get_selection(self) -> List[str | int]:
        """Returns the data of a selected row/rows in the table."""

        selected_data = [self.table.item(i)["values"] for i in self.table.selection()]
        return selected_data

    def delete_selected(self) -> None:
        """Deletes the selected row/rows in the table."""
        for i in self.table.selection():
            self.table.delete(i)
