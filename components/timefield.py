from PyQt5.QtWidgets import QTimeEdit
from vision.components.base import Widget
from vision.utils import *


class TimeField(Widget):
    def __init__(self,name = None,design:FieldDesign = FieldDesign()):
        super().__init__(name)
        self.design = design

    def buildWidget(self, parent):
        self.widget = QTimeEdit(parent)
        self.widget.setObjectName(self.id)
        self.applyStyle()
        return self.widget

    def applyStyle(self):
        self.widget.setStyleSheet(f"""
        #{self.id}{{
                {self.design.buildStyle()}

                }}
                #{self.id}::down-button{{ 
                 }}
                 #{self.id}::down-arrow{{
                 
                 }}
""")