from PyQt5.QtWidgets import QFrame
from vision.components.base import Widget


class Gap(Widget):
    def __init__(self,name = None,width = 0,height = 0):
        super().__init__(name)
        self.width = width
        self.height = height

    def buildWidget(self, parent):
        self.widget = QFrame(parent)
        self.widget.setFixedHeight(self.height)
        self.widget.setFixedWidth(self.width)
        return self.widget