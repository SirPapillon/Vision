from PyQt5.QtWidgets import  QCheckBox
from vision.components.base import Widget
from vision.utils import *

class CheckBox(Widget):
    def __init__(self,name = None,
                 design:CheckBoxDesign = CheckBoxDesign(),
                 text:str = None,
                 onChanged:lambda checked:None = None,
                 style:TextStyle = TextStyle()
                 ):
        super().__init__(name)
        self.text = text
        self.design = design
        self.onChanged = onChanged
        self.style = style

    def _onChanged(self,state):
        print(state)
        if state == 0:
            self.onChanged(False)
        elif state == 2:
            self.onChanged(True)
    def configGestures(self):
        if self.onChanged is not None:
            self.widget.stateChanged.connect(self._onChanged)


    def buildWidget(self, parent):
        self.widget = QCheckBox(parent)
        self.widget.setObjectName(self.id)
        self.widget.setText(self.text)
        self.configGestures()
        self.applyStyle()
        return self.widget

    def applyStyle(self):
        design = self.design
        checkedDesign = design.checkedDesign
        self.widget.setStyleSheet(f"""
 
#{self.id}::indicator{{
    {self.design.buildStyle()}
    {self.style.buildStyle()}
}}
#{self.id}::indicator:checked {{
   {checkedDesign.buildStyle()}
}}
#{self.id}:checked, #{self.id}::indicator:checked {{
}}
#{self.id}:checked {{
}}
""")