from PyQt5.QtWidgets import (
    QCalendarWidget,
    QFrame,
    QVBoxLayout,
)
from vision.components.base import Widget
from vision.utils import *


class Calendar(Widget):
    def __init__(
            self,
            design: CalendarDesign = CalendarDesign(),
            headerDesign: HeaderDesign = HeaderDesign(),
            backgroundColor: Colors = None,
            padding: Padding = Padding.zero(),
            border:Border=Border.zero(),
            borderRadius:BorderRadius=BorderRadius.zero(),
            name=None,
    ):
        super().__init__(name)
        self.design = design
        self.border = border
        self.borderRadius = borderRadius
        self.headerDesign = headerDesign
        self.backgroundColor = backgroundColor
        self.padding = padding

    def buildWidget(self, parent):
        frame = QFrame(parent)
        frame.setObjectName(f"{self.id}_frame")
        frame.setStyleSheet(
            f"""
                #{self.id}_frame{{
                {StyleSheetBuilder.buildColor(self.backgroundColor, prefix="background-color:")}
                {StyleSheetBuilder.buildBorder(self.border)}
                {StyleSheetBuilder.buildBorderRadius(self.borderRadius)}
                }}
"""
        )
        inner_layout = QVBoxLayout()
        inner_layout.setContentsMargins(self.padding.left, self.padding.top, self.padding.right, self.padding.bottom)
        frame.setLayout(inner_layout)
        self.widget = QCalendarWidget()
        inner_layout.addWidget(self.widget)

        self.applyStyle()
        return frame

    def renderWidget(self, parent):
        pass

    def applyStyle(self):
        design = self.design
        self.widget.setStyleSheet(
            f"""
        QCalendarWidget QMenu {{
  	width: 150px;
  	left: 20px;
  	color: white;
  	font-size: 18px;
  	background-color: rgb(100, 100, 100);
  }}
      QCalendarWidget{{ 
        background-color:transparent;
}}

    QCalendarWidget QWidget {{
  {StyleSheetBuilder.buildPadding(self.headerDesign.padding)}

    {StyleSheetBuilder.buildColor(design.sidesBgColor, prefix="alternate-background-color:")}
    }}
    QCalendarWidget QAbstractItemView::enabled
  {{
  {StyleSheetBuilder.buildPadding(design.padding)}
  {StyleSheetBuilder.buildMargin(design.margin)}


            {StyleSheetBuilder.buildBorderRadius(design.borderRadius)}
            {StyleSheetBuilder.buildBorder(design.border)}


    {design.style.buildStyle()}
    {StyleSheetBuilder.buildColor(design.selectedBgColor, prefix="selection-background-color:")}
    {StyleSheetBuilder.buildColor(design.selectedFrColor, prefix="selection-color:")}
    {StyleSheetBuilder.buildColor(design.backgroundColor if design.backgroundColor is not None else Colors.white, prefix="background-color:")}
  }}

  QCalendarWidget QAbstractItemView::disabled{{
  background-color:red;
      {StyleSheetBuilder.buildColor(design.disableColor, prefix="color:")}

  }}



      QCalendarWidget QWidget#qt_calendar_navigationbar

{{                  

{self.headerDesign.buildStyle()}
}}


        """
        )
