from PyQt5.QtWidgets import QLineEdit, QComboBox, QStyledItemDelegate, QProgressBar, QStatusBar, QLabel, QWidget, \
    QTabWidget

from vision import widget_dict
from vision.components.base import Widget
from vision.utils import *
from threading import Thread


class TabView(Widget):
    def __init__(self, tabs: list, name=None,design:TabViewDesign=TabViewDesign()):
        super().__init__(name)
        self.tabs = tabs
        self.design = design

    def buildTabs(self):
        for tab in self.tabs:
            self.widget.addTab(tab.body.buildWidget(self.widget),tab.title)
    def buildWidget(self, parent):
        self.widget = QTabWidget(parent)
        self.widget.setObjectName(self.id)
        self.buildTabs()
        self.applyStyle()
        return self.widget

    def applyStyle(self):
        print(self.design.hoverDesign.buildStyle())
        self.widget.setStyleSheet(
            f"""
     
            
            #{self.id} QTabBar::tab {{
                 {self.design.tabDesign.buildStyle()}

            }}
            
            #{self.id} QTabBar::tab:hover {{
                {self.design.hoverDesign.buildStyle()}
            }}

            #{self.id} QTabBar::tab:selected {{
                 {self.design.selectionDesign.buildStyle()}

            }}

"""
        )



