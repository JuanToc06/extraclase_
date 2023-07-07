import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gastos Trimestrales")
        self.geometry("400x300")

        self.table_widget = ttk.Treeview(self)
        self.table_widget["columns"] = ("Trimestre", "Agua", "Luz", "Gas")
        self.table_widget.column("#0", width=0, stretch=tk.NO)
        self.table_widget.column("Trimestre", anchor=tk.CENTER, width=100)
        self.table_widget.column("Agua", anchor=tk.CENTER, width=100)
        self.table_widget.column("Luz", anchor=tk.CENTER, width=100)
        self.table_widget.column("Gas", anchor=tk.CENTER, width=100)

        self.table_widget.heading("#0", text="")
        self.table_widget.heading("Trimestre", text="Trimestre")
        self.table_widget.heading("Agua", text="Agua")
        self.table_widget.heading("Luz", text="Luz")
        self.table_widget.heading("Gas", text="Gas")

        self.initialize_table()

        self.table_widget.pack(fill=tk.BOTH, expand=True)

    def initialize_table(self):
        data = [
            ("1er trimestre", "Q120", "Q85", "Q18"),
            ("2do trimestre", "Q420", "Q105", "Q225"),
            ("3er trimestre", "Q360", "Q90", "Q160")
        ]

        for row in data:
            self.table_widget.insert("", tk.END, values=row)


if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()




