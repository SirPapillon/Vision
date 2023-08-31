from PyQt5.QtWidgets import QVBoxLayout, QWidget
from vision import widget_dict
from vision.components.base import Widget
from vision.utils import *


class VStack(Widget):
    def __init__(self, children: list, name=None,
                 mainArrange = MainArrange.start,
                 crossArrange = CrossArrange.start,
                 ):
        print(MainArrange.start)
        super().__init__(name)
        self.children = children
        self.mainArrange = mainArrange
        self.crossArrange = crossArrange

        widget_dict[self.name] = self

    def buildWidget(self, parent):
        self.widget = QVBoxLayout()
        self.widget.setSpacing(0)
        self.widget.setContentsMargins(0, 0, 0, 0)
        self.widget.setAlignment(self.mainArrange[0])

        widget = QWidget()
        widget.setLayout(self.widget)

        for child in self.children:
            self.widget.addWidget(child.buildWidget(parent),0,self.crossArrange[0])

        return widget

    def renderWidget(self, parent):
        colFrame = self.buildWidget(parent)
