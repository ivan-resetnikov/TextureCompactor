import tkinter as tk
import tkinter.ttk as ttk

from tkinter import filedialog

import core



class App:
    def __init__(self):
        self.window: tk.Tk = tk.Tk()
        self.window.title("Texture compactor")
        self.window.resizable(False, False)
    

    def _init_wigets(self) -> None:
        ttk.Label(text="Map 0 ").grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(text="Browse", command=lambda: self._browse_map_file(0)).grid(row=0, column=2, padx=10, pady=10)
        self.map_0_entry: ttk.Entry = ttk.Entry()
        self.map_0_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(text="Map 1 ").grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(text="Browse", command=lambda: self._browse_map_file(1)).grid(row=1, column=2, padx=10, pady=10)
        self.map_1_entry: ttk.Entry = ttk.Entry()
        self.map_1_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(text="Map 2 ").grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(text="Browse", command=lambda: self._browse_map_file(2)).grid(row=2, column=2, padx=10, pady=10)
        self.map_2_entry: ttk.Entry = ttk.Entry()
        self.map_2_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(text="Combine", command=self._combine).grid(row=3, column=1, padx=10, pady=10)


    def _browse_map_file(self, id: int) -> None:
        path_raw: str = tk.filedialog.askopenfilename(
            filetypes=(
                ("Compressed png", "*.png"),
                ("Compressed jpg", ("*.jpg", "*.jpeg")),
                ("Uncompressed bmp", "*.bmp"),
                ("Uncompressed tga", "*.tga"),
                ("Uncompressed tiff", ("*.tif", "*.tiff")),
                ("Raw", "*.*")
            )
        )

        path: str = path_raw.split(" ")[0]  # Tkinter moment

        if not path: return  # Stop in canceled

        match id:
            case 0: core.tools.set_entry_text(self.map_0_entry, path_raw)
            case 1: core.tools.set_entry_text(self.map_1_entry, path_raw)
            case 2: core.tools.set_entry_text(self.map_2_entry, path_raw)


    def _combine(self) -> None:
        output_path: str = filedialog.asksaveasfilename(defaultextension=".png")
        output_path: str = output_path.split(" ")[0]  # Tkinter moment

        if not output_path: return  # Stop if canceled

        core.compactor.combine_textures(
            map_0=self.map_0_entry.get(),
            map_1=self.map_1_entry.get(),
            map_2=self.map_2_entry.get(),
            output=output_path
        )


    def run(self) -> None:
        self._init_wigets()

        self.window.mainloop()


if __name__ == "__main__":
    App().run()