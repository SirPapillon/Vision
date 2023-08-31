from PyQt5.QtWidgets import QListWidget
from vision.utils import *
from vision.components.base import Widget


class ListBox(Widget):
    def __init__(self, items: list, name=None, design: ListBoxDesign = ListBoxDesign()):
        super().__init__(name)
        self.items = items
        self.design = design

    def buildItems(self):
        for index in range(len(self.items)):
            self.widget.addItem(self.items[index])

    def buildWidget(self, parent):
        self.widget = QListWidget(parent)
        self.buildItems()
        # self.applyStyle()
        return self.widget

    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)

    def applyStyle(self):
        design = self.design
        self.widget.configure(
            relief="flat",
            highlightthickness=design.border.width,
            selectbackground=f"{design.selectedDesign.backgroundColor}",
            highlightcolor=f"{design.border.color}",
            # highlightbackground=
            # highlightcolor=f"{design.border.color}",
            background=f"{design.backgroundColor}")
