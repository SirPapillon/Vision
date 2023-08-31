from PyQt5.QtWidgets import QSpinBox
from vision.components.base import Widget
from vision.utils import *



class NumberPicker(Widget):
    value = None

    def __init__(self, numbers: list,name=None,
                 style: TextStyle = TextStyle(color=Colors.black),
                 default = None,
                 onChanged: lambda value: str = None):
        super().__init__(name)
        self.numbers = numbers
        self.default = default if default is not None else numbers[-1]
        self.style = style
        self.onChanged = onChanged
        self.value = self.default

    def _onChanged(self, text: str):
        if self.value == text:
            return
        self.value = text
        self.onChanged(text)

    def buildItems(self):
        for n in self.numbers:
            self.widget.setValue(n)

    def buildWidget(self, parent) -> QSpinBox:
        self.widget = QSpinBox(parent)
        self.widget.setMinimum(min(self.numbers))
        self.widget.setMaximum(max(self.numbers))
        self.buildItems()

        self.widget.setValue(self.default)
        return self.widget

    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)
        self.widget.grid()

    def applyStyle(self):
        pass
