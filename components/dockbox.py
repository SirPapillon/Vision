from PyQt5.QtWidgets import QDockWidget
from vision.components.base import Widget
from vision.utils import *


class DockBox(Widget):
    def __init__(self,child,title="dockBox",barDesign:DockBarDesign = DockBarDesign(),design:BoxDesign= BoxDesign() ,name = None):
        super().__init__(name)
        self.child = child
        self.title = title
        self.design = design
        self.barDesign = barDesign


    def buildWidget(self, parent):
        self.widget = QDockWidget(self.title,parent)
        self.widget.setObjectName(self.id)
        self.widget.setWidget(self.child.buildWidget(self.widget))
        self.applyStyle()
        return self.widget
    def applyStyle(self):
        # with open("./media/upload.png")
        self.widget.setStyleSheet(f"""
        
#{self.id} {{
        {self.design.buildStyle()}

                titlebar-close-icon: url({self.barDesign.closeIcon.path});
                titlebar-normal-icon: url({self.barDesign.normalIcon.path});
  
                background-color: #F0F0F0;
                border: 1px solid #C0C0C0;
            }}
""")