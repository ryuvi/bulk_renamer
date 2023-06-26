import tkinter as tk
import components as interface_components

class Main_Page(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Basic interface configuration
        self.title("Bulk Renamer")
        self.geometry("800x600")
        self.tree_frame = tk.Frame(self)
        self.tree_frame.grid(row=0, column=0, padx=25, pady=25)
        self.folder_tree = interface_components.FolderTree(self.tree_frame, '.')


if __name__ == '__main__':
    Main_Page().mainloop()
