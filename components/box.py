from PyQt5.QtWidgets import QFrame, QVBoxLayout
from vision.components.base import Widget
from vision.utils import *


class Box(Widget):
    def __init__(self, name=None, child: Widget = None, width: float = None, height: float = None,
                 padding: Padding = None,
                 margin: Margin = None,
                 design: BoxDesign = BoxDesign()):
        super().__init__(name)
        design.parent = self.parent
        self.design = design

        self.width = width
        self.height = height
        self.child = child
        self.padding = padding
        self.margin = margin

    def buildWidget(self, parent) -> QFrame:


        width = self.width
        height = self.height

        self.widget = QFrame(parent)

        self.widget.setObjectName(self.id)
        #
        # self.widget.setFixedWidth(width)
        # self.widget.setFixedHeight(height)
        self.applyStyle()


        if self.child is None:
            width = 0 if self.width is None else self.width
            height = 0 if self.height is None else self.height
            self.widget.setFixedWidth(width)
            self.widget.setFixedHeight(height)
            return self.widget



        if self.child is not None:
            inner_layout = QVBoxLayout()
            inner_layout.setContentsMargins(0, 0, 0, 0)
            inner_layout.addWidget(self.child.buildWidget(self.widget))
            self.widget.setLayout(inner_layout)


        return self.widget

    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)

    def applyStyle(self):
        border = self.design.border
        self.widget.setStyleSheet(
            f"""
            #{self.id}{{
              {StyleSheetBuilder.buildPadding(self.padding)}
             {StyleSheetBuilder.buildColor(color=self.design.backgroundColor,prefix="background-color: ")}
             {StyleSheetBuilder.buildBorderRadius(self.design.borderRadius)}
             {StyleSheetBuilder.buildBorder(self.design.border)}
             {StyleSheetBuilder.buildPadding(self.padding)}
             {StyleSheetBuilder.buildMargin(self.margin)}
             

}}
             """)
