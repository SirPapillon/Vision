import functools

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QComboBox, QStyledItemDelegate, QProgressBar, QStatusBar, QLabel, QWidget, \
    QTabWidget, QToolBar, QAction

from vision import widget_dict
from vision.components.base import Widget
from vision.utils import *
from threading import Thread

from vision.utils.aligns.toolbarside import TBarSide


class ToolBar(Widget):
    def __init__(self,
                 children,
                 title="toolBar",
                 padding:Padding = Padding.zero(),
                 margin:Margin = Margin.zero(),
                 design:BoxDesign=BoxDesign(),
                 side:TBarSide = TBarSide.top(),
                 movable:bool = True,
                 allowedSides:list = None,
                 name = None):
        super().__init__(name)
        self.side = side
        self.children = children
        self.title = title
        self.padding = padding
        self.margin = margin
        self.design = design
        self.movable = movable
        self.allowedSides = [] if allowedSides is None else allowedSides

    def buildItems(self):
        for child in self.children:
            self.widget.addWidget(child.buildWidget(self.widget))

    def buildWidget(self, parent):
        self.widget = QToolBar(self.title)
        self.widget.setObjectName(self.id)
        self.widget.setMovable(self.movable)
        if len(self.allowedSides) != 0:
            self.widget.setAllowedAreas(
                functools.reduce(lambda a, b: a | b, self.allowedSides)
            )
        self.buildItems()
        self.applyStyle()
        return self.widget

    def renderWidget(self, parent):
        pass
    def applyStyle(self):
        self.widget.setStyleSheet(
            f"""
            #{self.id}{{
                {self.design.buildStyle()}
                {self.padding.buildStyle()}
                {self.margin.buildStyle()}

            }}

"""
        )