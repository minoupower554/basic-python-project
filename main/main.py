#data read format: [{name: str, description: str, pinned: bool, completed: bool, is_dummy: bool}]
from tkinter import Tk, Frame, Button
from templates import item
from json import dump, load, JSONDecodeError
data: list[dict[str: str, str: str, str: bool, str: bool]] = []

try:
    with load("data.json") as file:
        data = file
except JSONDecodeError:
    data.append({"name": "dummy", "description": "dummy", "pinned": False, "completed": True, "is_dummy": True})


class maker:
    def __init__(self, root: Tk):
        self.items: list[Frame] = []
        self.name: str
        self.desc: str
        self.pinned: bool
        self.comp: bool
        self.is_dummy: bool
        self.root: Frame = root
    

    def unpacker(self, data: list):
        for item in data:
            if item.is_dummy: return
            self.name = item.name
            self.desc = item.description
            self.pinned = item.pinned
            self.comp = item.completed
            self.is_dummy = item.is_dummy
    

    def maker(self):
        current_item_class: item = item(self.root, self.name, self.desc, self.pinned, self.comp)
        current_item: Frame = current_item_class.run()
        self.items.append(current_item)


    def run(self, data: list):
        self.unpacker(data)
        self.maker()

def window_maker():
    root: Tk = Tk()
    root.title("todo list")
    root.geometry("300x440")
    return root


def main():
    root: Tk = window_maker()
    app: maker = maker()

    


if __name__ == "__main__":
    main()
