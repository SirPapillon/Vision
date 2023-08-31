from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import  QTreeWidget,QTreeWidgetItem
from vision.components.base import Widget
from vision.utils import *


class TreeView(Widget):
    def __init__(self,nodes:list,design:TreeDesign = TreeDesign(),name = None):
        super().__init__(name)
        self.nodes = nodes
        self.design = design

    def buildNodes(self):

        self.widget.setColumnCount(1)
        item1 = QTreeWidgetItem(self.widget, ["Item 1"])
        for node in self.nodes:
            node.buildNodes(item1)



    def buildWidget(self, parent):
        self.widget = QTreeWidget(parent)
        self.buildNodes()
        self.applyStyle()
        return self.widget

    def applyStyle(self):
        self.widget.setStyleSheet(f"""
            QTreeView {{
                {self.design.buildStyle()}
            }}
            QTreeView::item {{  
{self.design.nodeDesign.buildStyle()}

            }}
            QTreeView::item:hover {{
            {self.design.hoverDesign.buildStyle()}

            }}
            QTreeView::item:selected {{
{self.design.selectionDesign.buildStyle()}

            }}
         
         
           
        """)

class TreeNode:
    def __init__(self,title,nodes:list = None):
        self.nodes = nodes
        self.title = title

    def buildNodes(self,parent):
        _node = QTreeWidgetItem(parent,[self.title])

        if self.nodes == 0 or self.nodes is None:
            return _node
        for node in self.nodes:
            node.buildNodes(_node)

#                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);
