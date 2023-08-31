from PyQt5.QtWidgets import   QFrame, QVBoxLayout
from vision.components.base import Widget
from vision.utils import *

class ExpandedView(Widget):
    def __init__(self,child, name = None):
        super().__init__(name)
        self.child = child

    def buildWidget(self, parent):
        self.parent = parent
        self.widget = QFrame(parent)
        inner_layout = QVBoxLayout()
        inner_layout.setContentsMargins(0, 0, 0, 0)
        c = self.child.buildWidget(self.widget)
        c.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        inner_layout.addWidget(c)
        self.widget.setLayout(inner_layout)


        return self.widget
