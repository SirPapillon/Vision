from PyQt5.QtWidgets import  QListWidget,QListWidgetItem
from vision.components.base import Widget
from vision.utils import *


class ListView(Widget):
    def __init__(self,children:list,
                 name=None,
                 design:ListDesign=ListDesign()
                 ):
        super().__init__(name)
        self.design = design
        self.children = children

    def buildItems(self):
        for child in self.children:
            rt = QListWidgetItem()
            self.widget.addItem(rt)
            self.widget.setItemWidget(rt, child.buildWidget(self.widget))
    def buildWidget(self, parent):
        self.widget = QListWidget(parent)
        self.widget.setObjectName(self.id)
        self.buildItems()
        self.applyStyle()
        return self.widget

    def applyStyle(self):
        itemsDesign = self.design.itemsDesign
        hoverDesign = self.design.hoverDesign
        selectionDesign = self.design.selectionDesign
        self.widget.setStyleSheet(
            f"""
#{self.id}{{
outline:none;
                {StyleSheetBuilder.buildBorderRadius(borderRadius=self.design.borderRadius)}
                {StyleSheetBuilder.buildColor(color=self.design.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildBorder(border=self.design.border)}
                {StyleSheetBuilder.buildPadding(padding=self.design.contentPadding)}
                {StyleSheetBuilder.buildTextStyle(style=self.design.style)}
            }}
            
            #{self.id}::item{{
            
            {StyleSheetBuilder.buildPadding(itemsDesign.padding)}
            {StyleSheetBuilder.buildMargin(itemsDesign.margin)}
                {StyleSheetBuilder.buildColor(color=itemsDesign.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(style=itemsDesign.style)}
                {StyleSheetBuilder.buildBorder(border=itemsDesign.border)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=itemsDesign.borderRadius)}
            }}
            
            #{self.id}::item:hover{{
            {StyleSheetBuilder.buildPadding(hoverDesign.padding)}
            {StyleSheetBuilder.buildMargin(hoverDesign.margin)}
                {StyleSheetBuilder.buildColor(color=hoverDesign.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(style=hoverDesign.style)}
                  {StyleSheetBuilder.buildTextStyle(style=hoverDesign.style)}
                {StyleSheetBuilder.buildBorder(border=hoverDesign.border)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=hoverDesign.borderRadius)}
            }}
            
            #{self.id}::item:selected{{
            {StyleSheetBuilder.buildPadding(selectionDesign.padding)}
            {StyleSheetBuilder.buildMargin(selectionDesign.margin)}
                {StyleSheetBuilder.buildColor(color=selectionDesign.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(style=selectionDesign.style)}
                  {StyleSheetBuilder.buildTextStyle(style=selectionDesign.style)}
                {StyleSheetBuilder.buildBorder(border=selectionDesign.border)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=selectionDesign.borderRadius)}
            }}
"""
        )