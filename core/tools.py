import tkinter as tk
import tkinter.ttk as ttk

from dataclasses import dataclass



def _set_entry_text(entry: tk.Entry|ttk.Entry, text: str) -> None:
    entry.delete(0, tk.END)
    entry.insert(0, text)
    return


@dataclass
class tools:
    set_entry_text = _set_entry_text