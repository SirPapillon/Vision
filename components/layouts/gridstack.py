from PyQt5.QtWidgets import QGridLayout, QWidget
from vision.components.base import Widget
from vision.utils import *


class GridStack(Widget):
    def __init__(self,items:list, name = None):
        super().__init__(name)
        self.items = items
        self.grid = QGridLayout()

    def buildItems(self):
        for item in self.items:
            child = item.child.buildWidget(self.parent)
            if item.hStretchBehavior is not None:
                child.setSizePolicy(item.hStretchBehavior, item.hStretchBehavior)


            self.grid.addWidget(child,
                                item.row,
                                item.col,
                                item.rowSpan,
                                item.colSpan)
    def buildWidget(self, parent):
        self.parent = parent
        self.widget = QWidget(parent)
        self.buildItems()
        self.widget.setLayout(self.grid)
        return self.widget

class GridItem:
    def __init__(self,child,row:int,col:int,
                 hStretchBehavior:StretchBehavior=None,
                 vStretchBehavior:StretchBehavior=None,
                 rowSpan:int = 1,colSpan:int=1):
        self.child = child
        self.row = row
        self.col = col
        self.rowSpan = rowSpan
        self.colSpan = colSpan
        self.hStretchBehavior = hStretchBehavior
        self.vStretchBehavior = vStretchBehavior