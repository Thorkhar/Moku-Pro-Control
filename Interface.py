import tkinter as tk
from config import settings as cfg
from Moku import Moku
from Waveform import Waveform

class GUI:
    def __init__(self, moku_a: Moku, moku_b: Moku) -> None:
        self.moku_a = moku_a
        self.moku_b = moku_b
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
            if isinstance(value, list):
                for i in range(len(value)):
                    labels[name+str(i)] = tk.Label(self.window, text=name+str(i))
                    entries[name+str(i)] = tk.Entry(self.window, textvariable=name+str(i))
                    entries[name+str(i)].insert(0, str(value[i]))

                    labels[name+str(i)].grid(row=row_counter, column=0)
                    entries[name+str(i)].grid(row=row_counter, column=1)
                    row_counter += 1
            else:
                labels[name] = tk.Label(self.window, text=str(name))
                entries[name] = tk.Entry(self.window, textvariable=name)
                entries[name].insert(0, value)

                labels[name].grid(row=row_counter, column=0)
                entries[name].grid(row=row_counter, column=1)
                row_counter += 1
