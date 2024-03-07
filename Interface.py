import tkinter as tk
from config import settings as cfg

class GUI:
    def __init__(self) -> None:
        self.window = tk.Tk()

    def startMainLoop(self) -> None:
        self.window.mainloop()

    def packWidgetDict(self, *widgets: dict):
        for x in widgets:
            for name, widget in x.items():
                widget.pack()

    def createSettingsWidgets(self) -> None:
        labels = {}
        entries = {}

        row_counter = 0
        for name, value in cfg.items():
            labels[name] = tk.Label(self.window, text=str(name))
            entries[name] = tk.Entry(self.window, textvariable=name)
            entries[name].insert(0, value)

            labels[name].grid(row=row_counter, column=0)
            entries[name].grid(row=row_counter, column=1)
            row_counter += 1

        #self.packWidgetDict(labels, entries)
