from PyQt5.QtWidgets import QStatusBar
from vision.components.base import Widget
from vision.utils import *


class StatusBar(Widget):
    def __init__(self,
                 items: list,
                 space:float=0,
                 padding:Padding=Padding.zero(),
                 name = None,
                 expandable:bool = True,
                 design:BoxDesign = BoxDesign()

                 ):
        super().__init__(name)
        self.design = design
        self.items = items
        self.space = space
        self.padding = padding
        self.expandable = expandable

    def buildItems(self):
        padding = self.padding
        self.widget.setContentsMargins(padding.left,padding.top,padding.right,padding.bottom)


        for i in range(len(self.items)):
            item = self.items[i]
            child = item.buildWidget(self.widget)
            if i != 0:
                child.setContentsMargins(self.space,0,0,0)
            self.widget.addWidget(child)
    def buildWidget(self, parent):
        self.widget = QStatusBar()
        self.widget.setObjectName(self.id)
        self.widget.setSizeGripEnabled(self.expandable)
        self.buildItems()

        self.applyStyle()

        return self.widget

    def applyStyle(self):
        self.widget.setStyleSheet(f"""
#{self.id}{{
{self.design.buildStyle()}

}}
#{self.id}::handle {{ background: red; border: 1px solid black; }}

#{self.id}::item{{
background-color:transparent;
}}

""")