from PyQt5.QtWidgets import QHBoxLayout, QWidget
from vision import widget_dict
from vision.components.base import Widget
from vision.utils import *


class HStack(Widget):
    def __init__(self, children: list,name=None,
                 mainArrange = MainArrange.start,
                 crossArrange = CrossArrange.start,

                 ):
        super().__init__(name)
        self.children = children
        self.mainArrange = mainArrange
        self.crossArrange = crossArrange

        widget_dict[self.name] = self


    def buildWidget(self, parent) -> QHBoxLayout:
        self.widget = QHBoxLayout(parent)
        self.widget.setSpacing(0)
        self.widget.setContentsMargins(0, 0, 0, 0)
        self.widget.setAlignment(self.mainArrange[1])
        widget = QWidget()
        widget.setLayout(self.widget)

        for child in self.children:
            self.widget.addWidget(child.buildWidget(parent),0,self.crossArrange[1])

        return widget

    def renderWidget(self, parent):
        rowFrame = self.buildWidget(parent)

