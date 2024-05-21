from tkinter import Frame
import json

class item:
    def __init__(self, root: Frame, name: str, description: str, pinned: bool, completed: bool) -> None:
        self.data: dict[str, bool | str | None] = []
        self.root = root
        self.name: str = name
        self.desc: str = description
        self.pinned: bool = pinned
        self.comp: bool = completed


    def run(self):
        ...
    

    def generator(self):
        self.created: Frame = Frame(self.root)
