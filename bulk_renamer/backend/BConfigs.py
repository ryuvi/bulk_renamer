from tkinter import ttk
from ttkthemes import THEMES

class Configs:
    def __init__(self):
        self._themes_list = ttk.Style() + THEMES
        
    def get_theme_list(self):
        return self._themes_list.theme_names()
