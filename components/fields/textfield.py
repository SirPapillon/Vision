from PyQt5.QtWidgets import QLineEdit
from vision import widget_dict
from vision.components.base import Widget
from vision.utils import *


class TextField(Widget):
    def __init__(self,name = None,
                 show=None, handler: FieldHandler = FieldHandler(),
                 text:str=None,
                 style:TextStyle=None,
                 onHovered: lambda TextField:None = None,
                 design: FieldDesign = FieldDesign(),
                 hoverDesign: FieldDesign = FieldDesign(),
                 focusDesign: FieldDesign = FieldDesign(),

                onChanged:lambda text: str = None):
        super().__init__(name)
        self.design = design
        self.hoverDesign = hoverDesign
        self.focusDesign = focusDesign
        self.onChanged = onChanged
        self.handler = handler
        self.text = text
        self.configHandler()
        self.onHovered = onHovered
        self.show = show
        self.style = style
        widget_dict[self.name] = self


    def configHandler(self):
        self.handler.text = self.text
        self.handler.setText = self.setText
        self.handler.clear = self.clear
        self.handler.insert = self.insert

    def text(self):
        return self.widget.get()

    def setText(self, text: str):
        self.widget.setText(text)

    def clear(self):
        self.widget.delete(0, "end")  # Clear the current text

    def insert(self, text: str, index: int = -1):
        self.widget.insert(text)

    def buildWidget(self, parent):
        self.widget = QLineEdit(parent)
        self.widget.setObjectName(self.id)
        self.setText(self.text)
        self.widget.setPlaceholderText(self.design.placeHolderText)
        if self.onChanged is not None:
            self.widget.textChanged.connect(self.onChanged)

        if self.hoverDesign.placeHolderText is not None:
            self.widget.enterEvent = lambda event:self._onHovered(event)
            self.widget.leaveEvent = lambda event:self.widget.setPlaceholderText(self.design.placeHolderText)


        self.applyStyle()
        return self.widget

    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)


    def applyStyle(self):

        self.widget.setStyleSheet(
            f"""
            #{self.id}{{
            {StyleSheetBuilder.buildColor(color=self.design.backgroundColor,prefix="background-color:")}
            {StyleSheetBuilder.buildBorderRadius(self.design.borderRadius)}
            {StyleSheetBuilder.buildBorder(self.design.border)}
            {StyleSheetBuilder.buildPadding(self.design.padding)}
            {StyleSheetBuilder.buildTextStyle(self.design.style)}
            }}
            
            #{self.id}::hover{{
            {StyleSheetBuilder.buildColor(self.hoverDesign.backgroundColor,prefix="background-color:")}
            {StyleSheetBuilder.buildBorderRadius(self.hoverDesign.borderRadius)}
            {StyleSheetBuilder.buildBorder(self.hoverDesign.border)}
            {StyleSheetBuilder.buildPadding(self.hoverDesign.padding)}
            {StyleSheetBuilder.buildTextStyle(self.hoverDesign.style)}
            }}
            
            #{self.id}::focus{{
            {StyleSheetBuilder.buildColor(self.focusDesign.backgroundColor,prefix="background-color:")}
            {StyleSheetBuilder.buildBorderRadius(self.focusDesign.borderRadius)}
            {StyleSheetBuilder.buildBorder(self.focusDesign.border)}
            {StyleSheetBuilder.buildPadding(self.focusDesign.padding)}
            {StyleSheetBuilder.buildTextStyle(self.focusDesign.style)}
            }}
            
            
      
            """
        )


    def _onHovered(self,event):
        self.widget.setPlaceholderText(self.hoverDesign.placeHolderText)
        self.onHovered(self)

