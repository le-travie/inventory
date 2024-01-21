from tkinter import *
from tkinter import ttk
from typing import List


class TableComponent(ttk.Treeview):
    """
    Custom prestyled table compoenet. Meant to display data from the database.
    """

    def __init__(self, root: Tk, columns: list, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self["columns"] = columns
        self.table = None

    def row_colour(
        self,
        odd_bgc: str,
        even_bgc: str,
        even_fgc: str = "black",
        odd_fgc: str = "black",
    ) -> None:
        """
        Sets the colour of the rows in the table.
        Takes string values for background colours of odd and even rows.
        Foreground colours are optional.
        """
        self.tag_configure("odd", background=odd_bgc, foreground=odd_fgc)
        self.tag_configure("even", background=even_bgc, foreground=even_fgc)

    def get_selection(self) -> List[str | int]:
        """Returns the data of a selected row/rows in the table."""

        selected_data = [self.item(i)["values"] for i in self.selection()]
        print(selected_data)
        return selected_data

    def delete_selected(self) -> None:
        """Deletes the selected row/rows in the table."""
        for i in self.selection():
            self.delete(i)
