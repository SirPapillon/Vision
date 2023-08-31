from PyQt5.QtWidgets import QRadioButton
from vision.components.base import Widget
from vision.utils import *
from vision.components import RadioGroup


class RadioButton(Widget):
    def __init__(self,
                 style:TextStyle = TextStyle(),
                 design:RadioButtonDesign = RadioButtonDesign(
                 ),
                 onChanged: lambda checked: None = None,

                 group:RadioGroup = None,name = None):
        super().__init__(name)
        self.group = group
        self.style = style
        self.design = design
        self.onChanged = onChanged

    def _onChanged(self,state):
        pass
    def configGestures(self):
        if self.onChanged is not None:
            self.widget.stateChanged.connect(self._onChanged)


    def buildWidget(self, parent):
        self.widget = QRadioButton(parent)
        self.widget.setObjectName(self.id)
        if self.group is not None:
            self.group.widget.addButton(self.widget)

        self.applyStyle()
        self.configGestures()
        return self.widget

    def applyStyle(self):
        checkedDesign = self.design.checkedDesign

        self.widget.setStyleSheet(f"""
               
QRadioButton::indicator{{
{self.design.buildStyle()}

    {self.style.buildStyle()}
}}
QRadioButton::indicator:checked {{
   {checkedDesign.buildStyle()}
}}
QRadioButton:checked, QRadioButton::indicator:checked {{
}}
QRadioButton:checked {{
}}
""")

