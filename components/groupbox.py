from PyQt5.QtWidgets import QGroupBox, QFormLayout
from vision.components.base import Widget
from vision.utils import *



class GroupBox(Widget):
    def __init__(self,children:list,
                 style:TextStyle=TextStyle(),
                 titlePadding:Padding=Padding.zero(),
                 titleMargin:Margin=Margin.zero(),
                 design:BoxDesign=BoxDesign(),
                 titleDesign:BoxDesign=BoxDesign(),
                 name=None,title="GroupBox"):
        super().__init__(name)
        self.children = children
        self.title = title
        self.style = style
        self.design = design
        self.titleDesign = titleDesign
        self.titlePadding = titlePadding
        self.titleMargin = titleMargin

    def buildItems(self):
        innerLayout = QFormLayout()
        self.widget.setLayout(innerLayout)

        for child in self.children:
            innerLayout.addWidget(child.buildWidget(self.widget))
    def buildWidget(self, parent):
        self.widget = QGroupBox(self.title)
        self.widget.setObjectName(self.id)
        self.buildItems()
        self.applyStyle()
        return self.widget

    def applyStyle(self):

        self.widget.setStyleSheet(
            f"""

            #{self.id}::title {{
                subcontrol-position: top left;
                {StyleSheetBuilder.buildTextStyle(self.style)}
                {self.titlePadding.buildStyle()}
                {self.titleMargin.buildStyle()}
                {self.titleDesign.buildStyle()}
                
            }}
            
            #{self.id}{{
            {self.design.buildStyle()}
            }}

""")