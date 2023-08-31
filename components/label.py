from PyQt5.QtWidgets import QLabel

from vision import widget_dict
from vision.components.base import Widget
from vision.utils import *


class Label(Widget):
    def __init__(self, text: str,name=None, handler: LabelHandler = LabelHandler(), backgroundColor: Colors = Colors.white,
                 style: TextStyle = TextStyle()):
        super().__init__(name)
        self.text = text
        self.style = style
        self.backgroundColor = backgroundColor
        self.handler = handler
        self.configHandler()
        widget_dict[self.name] = self

    def configHandler(self):
        return
        self.handler.text = self.text
        self.handler.setText = self.setText

    def text(self):
        return self.text

    def setText(self, text: str):
        self.text = text
        self.widget.config(text=text)

    def buildWidget(self, parent) -> QLabel:
        self.parent = parent
        self.widget = QLabel(parent)
        self.widget.setText(self.text)

        self.applyStyle()
        return self.widget

    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)

    def applyStyle(self):

        self.widget.setStyleSheet(f"""
{self.style.buildStyle()}
""")
