from PyQt5.QtWidgets import QVBoxLayout, QFrame
from vision.components.base import Widget
from vision.utils import *


class PaddingBox(Widget):
    def __init__(self,
                 padding:Padding,
                 child,
                 name = None):
        super().__init__(name)
        self.padding = padding
        self.child = child

    def buildWidget(self, parent):
        self.widget = QFrame(parent)
        inner_layout = QVBoxLayout()
        padding = self.padding
        inner_layout.setContentsMargins(padding.left,padding.top,padding.left,padding.bottom)
        inner_layout.addWidget(self.child.buildWidget(self.widget))
        self.widget.setLayout(inner_layout)
        return self.widget
