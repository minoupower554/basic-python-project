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


root: Tk = Tk()
root.title("todo list")
root.geometry("300x440")


