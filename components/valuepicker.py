from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate
from vision.components.base import Widget
from vision.utils import *



class ValuePicker(Widget):
    def __init__(self,values,name=None,
                 design:ValuePickerDesign = ValuePickerDesign(),
                 default = None,
                 outLine=False,
                 editable:bool=False,
                 onSubmitted: lambda value,index:None = None,
                 onHovered: lambda value,index:None = None,
                 ):
        super().__init__(name,)
        self.values = values
        self.design = design
        self.default = default
        self.onSubmitted = onSubmitted
        self.onHovered = onHovered
        self.outLine = outLine
        self.editable = editable

        self.value = self.default


    def configGestures(self):
        if self.onHovered is not None:
            self.widget.highlighted.connect(lambda i:self.onSubmitted(self.values[i],i))

        if self.onSubmitted is not None:
            self.widget.currentIndexChanged.connect(lambda i:self.onSubmitted(self.widget.currentText(),i))

    def buildItems(self):
        self.widget.addItems(self.values)
    def buildWidget(self, parent):
        self.widget = QComboBox(parent)
        self.configGestures()
        self.widget.setEditable(self.editable)
        self.widget.setItemDelegate(QStyledItemDelegate(self.widget))
        self.widget.setObjectName(self.id)
        self.buildItems()
        self.applyStyle()
        return self.widget
    def renderWidget(self, parent):
        pass

    def applyStyle(self):
        dropDownDesign = self.design.dropDownDesign
        itemsDesign = self.design.itemsDesign
        hoverDesign = self.design.hoverDesign
        self.widget.setStyleSheet(
            f"""
            #{self.id}
            {{
                {StyleSheetBuilder.buildBorderRadius(borderRadius=self.design.borderRadius)}
                {StyleSheetBuilder.buildColor(color=self.design.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildBorder(border=self.design.border)}
                {StyleSheetBuilder.buildPadding(padding=self.design.contentPadding)}
                {StyleSheetBuilder.buildTextStyle(style=self.design.style)}
            }}
            
 
            #{self.id}::drop-down 
            {{
                {StyleSheetBuilder.buildColor(color=dropDownDesign.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildColor(color=dropDownDesign.color,prefix="color:")}
                {StyleSheetBuilder.buildMargin(margin=dropDownDesign.margin)}
                {StyleSheetBuilder.buildBorder(border=dropDownDesign.border)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=dropDownDesign.borderRadius)}
            }}
                    
         #{self.id} QAbstractItemView::item:selected{{
            {StyleSheetBuilder.buildPadding(hoverDesign.padding)}
            {StyleSheetBuilder.buildMargin(hoverDesign.margin)}
                {StyleSheetBuilder.buildColor(color=hoverDesign.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(style=hoverDesign.style)}
                  {StyleSheetBuilder.buildTextStyle(style=hoverDesign.style)}
                {StyleSheetBuilder.buildBorder(border=hoverDesign.border)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=hoverDesign.borderRadius)}
            }}
            #{self.id} QAbstractItemView::item{{
            {StyleSheetBuilder.buildPadding(itemsDesign.padding)}
            {StyleSheetBuilder.buildMargin(itemsDesign.margin)}
                {StyleSheetBuilder.buildColor(color=itemsDesign.backgroundColor,prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(style=itemsDesign.style)}
                {StyleSheetBuilder.buildBorder(border=itemsDesign.border)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=itemsDesign.borderRadius)}
            }}
            #{self.id} QAbstractItemView 
            {{
                outline: {self.outLine}; 
                border:none;
                {StyleSheetBuilder.buildColor(self.design.listBgColor,prefix="background-color:")}
                {StyleSheetBuilder.buildMargin(margin=self.design.contentPadding)}
                {StyleSheetBuilder.buildBorderRadius(borderRadius=self.design.listBorderRadius)}
                {StyleSheetBuilder.buildBorder(border=self.design.listBorder)}



            }}
            

"""
        )
