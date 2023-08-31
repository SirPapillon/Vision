from PyQt5.QtWidgets import  QButtonGroup
from vision.components.base import Widget

class RadioGroup(Widget):
    def __init__(self, name = None):
        super().__init__(name)
        self.buildWidget(None)

    def buildWidget(self, parent):
        self.widget = QButtonGroup()
        return self.widget
