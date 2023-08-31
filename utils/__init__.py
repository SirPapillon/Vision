from __future__ import annotations
from enum import Enum

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from vision.configs import configs
from vision.utils.colors import Colors


# from widgets import *


class StyleSheetBuilder:

    @classmethod
    def noneChecker(cls, value, prefix, suffix, repl=None, semicolon=True):
        if value is None:
            return ""
        return f"{prefix} {repl if repl is not None else value}{suffix}{';' if semicolon == True else ''}"

    @classmethod
    def buildBorderRadius(cls, borderRadius: BorderRadius):
        if borderRadius is None:
            return ""
        return f"""
        {cls.noneChecker(borderRadius.bottomLeft, "border-bottom-left-radius:", suffix="px")}
        {cls.noneChecker(borderRadius.bottomRight, "border-bottom-right-radius:", suffix="px")}
        {cls.noneChecker(borderRadius.topRight, "border-top-right-radius:", suffix="px")}
        {cls.noneChecker(borderRadius.topLeft, "border-top-left-radius:", suffix="px")}

"""

    @classmethod
    def buildBorder(cls, border: Border):

        if border is None:
            return ""
        return f"""
        {cls.noneChecker(value=f"{border.bottom}",
                         semicolon=False,
                         prefix="border-bottom:", suffix="", repl=f"{border.bottom.width}px solid {cls.buildColor(border.bottom.color)}")}
             
        {cls.noneChecker(value=f"{border.right}",
                         semicolon=False,

                         prefix="border-right:", suffix="", repl=f"{border.right.width}px solid {cls.buildColor(border.right.color)}")}
             
        {cls.noneChecker(value=f"{border.top}",
                         semicolon=False,

                         prefix="border-top:", suffix="", repl=f"{border.top.width}px solid {cls.buildColor(border.top.color)}")}
             
        {cls.noneChecker(value=f"{border.left}",
                         semicolon=False,
                         prefix="border-left:", suffix="", repl=f"{border.left.width}px solid {cls.buildColor(border.left.color)}")}
             

"""

    @classmethod
    def buildPadding(cls, padding: Padding):
        if padding is None:
            return ""
        return f"""
                     {cls.noneChecker(padding.bottom, "padding-bottom:", "px")}
                     {cls.noneChecker(padding.right, "padding-right:", "px")}
                     {cls.noneChecker(padding.top, "padding-top:", "px")}
                     {cls.noneChecker(padding.left, "padding-left:", "px")}

        """

    @classmethod
    def buildMargin(cls, margin: Margin):
        if margin is None:
            return ""
        return f"""
                     {cls.noneChecker(margin.bottom, "margin-bottom:", "px")}
                     {cls.noneChecker(margin.right, "margin-right:", "px")}
                     {cls.noneChecker(margin.top, "margin-top:", "px")}
                     {cls.noneChecker(margin.left, "margin-left:", "px")}

        """

    @classmethod
    def buildTextStyle(cls, style: TextStyle):
        if style is None:
            return ""

        return f"""
{cls.buildColor(style.color, prefix="color:")}
font-size: {style.fontSize}px;
font-weight: {style.fontWeight};
"""

    @classmethod
    def buildColor(cls, color: Colors, prefix=""):
        if color is None:
            return ""

        return f"""
        {"" if color is None else f"{prefix} rgba{color};"}
"""


class FontWeight:
    normal = "normal"
    # light = "light"
    # ultraLight = "ultralight"
    # heavy = "heavy"
    # ultraBold = "ultrabold"
    bold = "bold"


class Size:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def zero(cls) -> Size:
        return cls(0, 0)


class Offset:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls) -> Offset:
        return cls(0, 0)


class Padding:
    def __init__(self, left: float, top: float, right: float, bottom: float):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @classmethod
    def all(cls, value: float) -> Padding:
        return cls(left=value, top=value, right=value, bottom=value)

    @classmethod
    def symmetric(cls, horizontal: float = 0, vertical: float = 0):
        return cls(left=horizontal, top=vertical, right=horizontal, bottom=vertical)

    @classmethod
    def only(cls, left: float = 0, top: float = 0, right: float = 0, bottom: float = 0) -> Padding:
        return cls(left=left, top=top, right=right, bottom=bottom)

    @classmethod
    def zero(cls) -> Padding:
        return cls(left=0, top=0, right=0, bottom=0)

    def buildStyle(self):
        return f"""
                        {StyleSheetBuilder.buildPadding(padding=self)}

        """


class Margin:
    def __init__(self, left: float, top: float, right: float, bottom: float):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @classmethod
    def all(cls, value: float) -> Margin:
        return cls(left=value, top=value, right=value, bottom=value)

    @classmethod
    def only(cls, left: float = 0, top: float = 0, right: float = 0, bottom: float = 0) -> Margin:
        return cls(left=left, top=top, right=right, bottom=bottom)

    @classmethod
    def symmetric(cls, horizontal: float = 0, vertical: float = 0):
        return cls(left=horizontal, top=vertical, right=horizontal, bottom=vertical)

    @classmethod
    def zero(cls) -> Margin:
        return cls(left=0, top=0, right=0, bottom=0)

    def buildStyle(self):
        return f"""
{StyleSheetBuilder.buildMargin(self)}
"""


class ButtonDesign:
    def __init__(self,
                 style: TextStyle = None,
                 text: str = "Button",
                 padding: Padding = Padding.zero(),

                 backgroundColor: Colors = None,
                 enableFocus: bool = False,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 ):
        self.backgroundColor = backgroundColor
        self.style = style
        self.text = text
        self.enableFocus = enableFocus
        self.border = border
        self.borderRadius = borderRadius
        self.padding = padding

    def buildStyle(self):
        return f"""
{StyleSheetBuilder.buildColor(self.backgroundColor, prefix="background-color:")}        
        {StyleSheetBuilder.buildTextStyle(self.style)}
        {StyleSheetBuilder.buildBorder(self.border)}
        {StyleSheetBuilder.buildBorderRadius(self.borderRadius)}
                {StyleSheetBuilder.buildPadding(self.padding)}

"""


class TextStyle:
    def __init__(self,
                 color: Colors = None, fontSize: float = None,
                 fontWeight: FontWeight = FontWeight.normal,
                 ):
        self.color = color
        self.fontSize = fontSize
        self.fontWeight = fontWeight

    def buildStyle(self):
        return f"""
        {StyleSheetBuilder.buildTextStyle(style=self)}
        
        """


class FieldDesign:
    def __init__(self, backgroundColor: Colors = None,
                 placeHolderText: str = None,
                 borderRadius: BorderRadius = None,
                 padding: Padding = None,
                 border: Border = None,
                 style: TextStyle = TextStyle()):
        self.backgroundColor = backgroundColor
        self.style = style
        self.borderRadius = borderRadius
        self.border = border
        self.padding = padding
        self.placeHolderText = placeHolderText

    def buildStyle(self):
        return f"""
{StyleSheetBuilder.buildColor(color=self.backgroundColor, prefix="background-color:")}
            {StyleSheetBuilder.buildBorderRadius(self.borderRadius)}
            {StyleSheetBuilder.buildBorder(self.border)}
            {StyleSheetBuilder.buildPadding(self.padding)}
            {StyleSheetBuilder.buildTextStyle(self.style)}
"""


class FieldHandler:
    def setText(self, text: str):
        pass

    def text(self):
        return ""
        # pass

    def clear(self):
        pass

    def insert(self, text: str, index: int = -1):
        pass


class LabelHandler:
    def setText(self, text: str):
        pass

    def text(self):
        pass


class HorizontalArrange(Enum):
    start = "start"
    center = "center"
    end = "end"
    spaceBetween = "spaceBetween"
    spaceAround = "spaceAround"


class WidgetGrid:

    def __init__(self, row=None, column=None,
                 rowspan=None,
                 columnspan=None,
                 sticky=None):
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.sticky = sticky

    @classmethod
    def _start(cls, row: int, col: int) -> WidgetGrid:
        return cls(
            row=0,
            column=col

        )


class VerticalArrange(Enum):
    start = "start"
    center = "center"
    end = "end"
    spaceBetween = "spaceBetween"
    spaceAround = "spaceAround"
    widgetGrid = WidgetGrid()

    def _start(self, row, col) -> WidgetGrid:
        return WidgetGrid(

        )


class AlignmentHandler:
    def __init__(self, parent, widget, col: int, row: int, horizontalArrange: HorizontalArrange,
                 verticalArrange: VerticalArrange):
        self.horizontalArrange = horizontalArrange
        self.verticalArrange = verticalArrange
        self.widget = widget
        self.parent = parent
        self.col = col
        self.row = row

    def grid(self):
        self.parent.grid_columnconfigure(self.col, weight=1)
        # rowSettings = self.rowAlign
        # colSettings = self.colAlign
        settings = WidgetGrid._start(row=self.row, col=self.col)

        self.widget.grid(row=0, column=settings.column, )


class Border:
    def __init__(self, width: float = 0, left: Border = None, top: Border = None, right: Border = None,
                 bottom: Border = None, color: Colors = Colors.black):
        self.width = width
        self.color = color
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    @classmethod
    def all(cls, width: float, color: Colors) -> Border:
        return cls(
            left=Border(width=width, color=color),
            top=Border(width=width, color=color),
            bottom=Border(width=width, color=color),
            right=Border(width=width, color=color),
        )

    @classmethod
    def symmetric(cls, horizontal: Border = None, vertical: Border = None):
        horizontal = horizontal if horizontal is not None else Border()
        vertical = vertical if vertical is not None else Border()
        return cls(left=horizontal, top=vertical, right=horizontal, bottom=vertical)

    @classmethod
    def only(cls, left: Border = None, top: Border = None, right: Border = None, bottom: Border = None) -> Border:
        left = left if left is not None else Border()
        right = right if right is not None else Border()
        top = top if top is not None else Border()
        bottom = bottom if bottom is not None else Border()
        return cls(left=left, top=top, right=right, bottom=bottom)

    @classmethod
    def zero(cls) -> Border:
        return cls(left=Border(width=0), top=Border(width=0), right=Border(width=0), bottom=Border(width=0))


class SelectedDesign:
    parent = None

    def __init__(self, backgroundColor: Colors = Colors.blue,
                 border: Border = Border.zero()):
        self.backgroundColor = backgroundColor
        self.border = border


class ListBoxDesign:
    parent = None

    def __init__(self, backgroundColor: Colors = Colors.transparent,
                 selectedDesign: SelectedDesign = SelectedDesign(),
                 border: Border = Border.zero()):
        self.backgroundColor = backgroundColor
        self.border = border
        self.selectedDesign = selectedDesign


class BorderRadius:
    def __init__(self, topLeft: float, topRight: float, bottomRight: float, bottomLeft: float):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomRight = bottomRight
        self.bottomLeft = bottomLeft

    @classmethod
    def all(cls, value: float) -> BorderRadius:
        return cls(topLeft=value, topRight=value, bottomRight=value, bottomLeft=value)

    @classmethod
    def symmetric(cls, horizontal: float = 0, vertical: float = 0):
        return cls(topLeft=horizontal, topRight=vertical, bottomRight=horizontal, bottomLeft=vertical)

    @classmethod
    def only(cls, topLeft: float = 0, topRight: float = 0, bottomRight: float = 0,
             bottomLeft: float = 0) -> BorderRadius:
        return cls(topLeft=topLeft, topRight=topRight, bottomRight=bottomRight, bottomLeft=bottomLeft)

    @classmethod
    def zero(cls) -> BorderRadius:
        return cls(topLeft=0, topRight=0, bottomRight=0, bottomLeft=0)


class BoxDesign:
    parent = None

    def __init__(self, backgroundColor: Colors = Colors.transparent, border: Border = None,
                 borderRadius: BorderRadius = None):
        self.backgroundColor = backgroundColor
        self.border = border
        self.borderRadius = borderRadius


    def buildStyle(self):
        return f"""
                                {StyleSheetBuilder.buildBorderRadius(borderRadius=self.borderRadius)}
                {StyleSheetBuilder.buildColor(color=self.backgroundColor, prefix="background-color:")}
                {StyleSheetBuilder.buildBorder(border=self.border)}

"""


class MenuBarDesign:
    def __init__(self,
                 backgroundColor: Colors = None,
                 itemsBgColor: Colors = None,
                 itemsHoverBgColor=None,
                 itemsHoverFrColor=None,
                 actionsHoverBgColor=None,
                 actionsHoverFrColor=None,
                 actionsBgColor: Colors = None,
                 itemsFrColor: Colors = None,
                 actionsFrColor: Colors = None,
                 seperatorColor: Colors = None,
                 seperatorWidth=None,
                 border: Border = None,
                 actionsBorder: Border = None,
                 itemsPadding=None

                 ):
        self.backgroundColor: Colors = backgroundColor
        self.itemsBgColor: Colors = itemsBgColor
        self.actionsBgColor: Colors = actionsBgColor
        self.itemsFrColor: Colors = itemsFrColor
        self.actionsFrColor: Colors = actionsFrColor
        self.itemsHoverBgColor: Colors = itemsHoverBgColor
        self.itemsHoverFrColor: Colors = itemsHoverFrColor
        self.actionsHoverBgColor: Colors = actionsHoverBgColor
        self.actionsHoverFrColor: Colors = actionsHoverFrColor
        self.seperatorColor: Colors = seperatorColor
        self.seperatorWidth: Colors = seperatorWidth
        self.actionsBorder = actionsBorder
        self.border = border
        self.itemsPadding = itemsPadding


class DropDownDesign:
    def __init__(self,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 backgroundColor: Colors = None,
                 color: Colors = None,
                 margin: Margin = None,
                 icon=""
                 ):
        self.border = border
        self.borderRadius = borderRadius
        self.backgroundColor = backgroundColor
        self.color = color
        self.icon = icon
        self.margin = margin


class ItemDesign:
    def __init__(self,
                 backgroundColor=None,
                 style: TextStyle = None,
                 margin: Margin = None,
                 padding: Padding = None,
                 borderRadius: BorderRadius = None,
                 border: Border = None,
                 ):
        self.backgroundColor = backgroundColor
        self.style = style
        self.margin = margin
        self.padding = padding
        self.border = border
        self.borderRadius = borderRadius

    def buildStyle(self):
        return f"""
        {StyleSheetBuilder.buildColor(self.backgroundColor, prefix="background-color:")}
        {StyleSheetBuilder.buildTextStyle(self.style)}
        {StyleSheetBuilder.buildBorder(self.border)}
        {StyleSheetBuilder.buildBorderRadius(self.borderRadius)}
        {StyleSheetBuilder.buildPadding(self.padding)}
        {StyleSheetBuilder.buildMargin(self.margin)}

"""


class ListDesign:
    def __init__(self,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 backgroundColor: Colors = None,
                 listBgColor: Colors = None,
                 listBorderRadius: BorderRadius = None,
                 listBorder: Border = None,
                 style: TextStyle = None,
                 contentPadding: Padding = None,
                 itemsDesign: ItemDesign = ItemDesign(),
                 hoverDesign: ItemDesign = ItemDesign(),
                 selectionDesign: ItemDesign = ItemDesign(),
                 ):
        self.border = border
        self.borderRadius = borderRadius
        self.backgroundColor = backgroundColor
        self.listBgColor = listBgColor
        self.listBorderRadius = listBorderRadius
        self.listBorder = listBorder
        self.style = style
        self.contentPadding = contentPadding
        self.itemsDesign = itemsDesign
        self.hoverDesign = hoverDesign
        self.selectionDesign = selectionDesign


class TabViewDesign:
    def __init__(self,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 backgroundColor: Colors = None,
                 # contentPadding: Padding = None,
                 tabDesign: ItemDesign = ItemDesign(),
                 hoverDesign: ItemDesign = ItemDesign(),
                 selectionDesign: ItemDesign = ItemDesign(),
                 ):
        self.border = border
        self.borderRadius = borderRadius
        self.backgroundColor = backgroundColor
        self.tabDesign = tabDesign
        self.hoverDesign = hoverDesign
        self.selectionDesign = selectionDesign


class ValuePickerDesign(ListDesign):
    def __init__(self, border: Border = None,
                 borderRadius: BorderRadius = None,
                 backgroundColor: Colors = None,
                 listBgColor: Colors = None,
                 listBorderRadius: BorderRadius = None,
                 listBorder: Border = None,
                 style: TextStyle = None,
                 contentPadding: Padding = None,
                 itemsDesign: ItemDesign = ItemDesign(),
                 hoverDesign: ItemDesign = ItemDesign(),
                 dropDownDesign: DropDownDesign = DropDownDesign(borderRadius=BorderRadius.zero())):
        super().__init__(border,
                         borderRadius,
                         backgroundColor,
                         listBgColor,
                         listBorderRadius,
                         listBorder,
                         style,
                         contentPadding,
                         itemsDesign,
                         hoverDesign,
                         )
        self.dropDownDesign = dropDownDesign


class ProgressBarDesign:
    def __init__(self,
                 backgroundColor: Colors = None,
                 padding: Padding = None,
                 border: Border = None,
                 style: TextStyle = None,
                 borderRadius: BorderRadius = None,
                 chunkColor: Colors = None,
                 chunkBorder: Border = None,
                 chunkBorderRadius: BorderRadius = None,
                 ):
        self.backgroundColor = backgroundColor
        self.border = border
        self.padding = padding
        self.style = style
        self.borderRadius = borderRadius
        self.chunkColor = chunkColor
        self.chunkBorder = chunkBorder
        self.chunkBorderRadius = chunkBorderRadius


class Icon:
    def __init__(self, name: str, width=None, height=None):
        self.name = name
        self.path = configs.extra.kwargs[name]
        self.width = width
        self.height = height


class DockBarDesign:
    def __init__(self,
                 closeIcon: Icon = None,
                 normalIcon: Icon = None,

                 ):
        self.closeIcon = closeIcon
        self.normalIcon = normalIcon


class TabItem:
    def __init__(self, body, title="tab"):
        self.title = title
        self.body = body


class CellDesign:
    def __init__(self, backgroundColor: Colors = None,
                 border: Border = Border.zero(),
                 borderRadius: BorderRadius = BorderRadius.zero()
                 , style: TextStyle = TextStyle()):
        self.backgroundColor = backgroundColor
        self.style = style
        self.borderRadius = borderRadius
        self.border = border

    def buildStyle(self):
        return f"""
        {StyleSheetBuilder.buildColor(self.backgroundColor, prefix="background-color:")}
        {StyleSheetBuilder.buildTextStyle(self.style)}
        {StyleSheetBuilder.buildBorder(self.border)}
        {StyleSheetBuilder.buildBorderRadius(self.borderRadius)}
"""


class TableDesign(BoxDesign):
    def __init__(self,
                 cellDesign: CellDesign = CellDesign(),
                 hoverDesign: CellDesign = CellDesign(),
                 selectionDesign: CellDesign = CellDesign(),
                 backgroundColor: Colors = None, border: Border = None, borderRadius: BorderRadius = None):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )
        self.cellDesign = cellDesign
        self.hoverDesign = hoverDesign
        self.selectionDesign = selectionDesign


class NodeDesign:
    def __init__(self, backgroundColor: Colors = None, style: TextStyle = TextStyle(),
                 border: Border = Border.zero(),
                 borderRadius: BorderRadius = BorderRadius.zero(),

                 ):
        self.backgroundColor = backgroundColor
        self.style = style
        self.border = border
        self.borderRadius = borderRadius

    def buildStyle(self):
        return f"""
                    {StyleSheetBuilder.buildTextStyle(self.style)}
                    {StyleSheetBuilder.buildColor(self.backgroundColor, prefix="background-color:")}
                    {StyleSheetBuilder.buildBorder(self.border)}
                    {StyleSheetBuilder.buildBorderRadius(self.borderRadius)}
"""


class TreeDesign(BoxDesign):
    def __init__(self,
                 nodeDesign: NodeDesign = NodeDesign(),
                 hoverDesign: NodeDesign = NodeDesign(),
                 selectionDesign: CellDesign = NodeDesign(),
                 backgroundColor: Colors = None, border: Border = None, borderRadius: BorderRadius = None):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )

        self.nodeDesign = nodeDesign
        self.hoverDesign = hoverDesign
        self.selectionDesign = selectionDesign


class HeaderDesign(BoxDesign):
    def __init__(self,
                 margin: Margin = Margin.zero(),
                 padding: Padding = Padding.zero(),
                 backgroundColor: Colors = None,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 ):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )
        self.margin = margin
        self.padding = padding

    def buildStyle(self):
        style = super().buildStyle()
        return f"""
{style}
{StyleSheetBuilder.buildMargin(self.margin)}
{StyleSheetBuilder.buildPadding(self.padding)}
"""


class CalendarDesign(BoxDesign):
    def __init__(self,
                 padding: Padding = Padding.zero(),
                 margin: Margin = Margin.zero(),
                 backgroundColor: Colors = None,
                 sidesBgColor: Colors = None,

                 style: TextStyle = TextStyle(),
                 disableColor: Colors = None,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 selectedFrColor: Colors = None,
                 selectedBgColor: Colors = None,

                 ):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )
        self.sidesBgColor = sidesBgColor
        self.style = style
        self.selectedFrColor = selectedFrColor
        self.selectedBgColor = selectedBgColor
        self.disableColor = disableColor
        self.padding = padding
        self.margin = margin


class StretchBehavior:
    @classmethod
    def expand(cls):
        return QSizePolicy.Expanding

    @classmethod
    def default(cls):
        return QSizePolicy.Expanding


class CheckedDesign(BoxDesign):
    def __init__(self,
                 text=None,
                 backgroundColor: Colors = None,
                 border: Border = None,
                 borderRadius: BorderRadius = None,
                 icon=None,
                 width=None,
                 height=None
                 ):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )
        self.text = text
        self.icon = icon
        self.width = width
        self.height = height

    def buildStyle(self):
        return f"""
                {super().buildStyle()}
                {StyleSheetBuilder.noneChecker(value=self.width, prefix="width:", suffix="px")}
                {StyleSheetBuilder.noneChecker(value=self.height, prefix="height:", suffix="px")}
                
"""


class CheckBoxDesign(BoxDesign):
    def __init__(self,
                 backgroundColor: Colors = None,
                 border: Border = None,
                 width=None,
                 height=None,
                 borderRadius: BorderRadius = None,
                 checkedDesign: CheckedDesign = CheckedDesign()
                 ):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )
        self.checkedDesign = checkedDesign
        self.width = width
        self.height = height


    def buildStyle(self):
        print(f"""
        {super().buildStyle()}
                {StyleSheetBuilder.noneChecker(value=self.width, prefix="width:", suffix="px")}
                {StyleSheetBuilder.noneChecker(value=self.height, prefix="height:", suffix="px")}
                
""")

        return f"""
        {super().buildStyle()}
                {StyleSheetBuilder.noneChecker(value=self.width, prefix="width:", suffix="px")}
                {StyleSheetBuilder.noneChecker(value=self.height, prefix="height:", suffix="px")}
                
"""


class RadioButtonDesign(BoxDesign):
    def __init__(self,
                 backgroundColor: Colors = None,
                 border: Border = None,
                 width=None,
                 height=None,
                 borderRadius: BorderRadius = None,
                 checkedDesign: CheckedDesign = CheckedDesign()
                 ):
        super().__init__(
            backgroundColor=backgroundColor,
            border=border,
            borderRadius=borderRadius,
        )
        self.checkedDesign = checkedDesign
        self.width = width
        self.height = height

    def buildStyle(self):
        return f"""
        {super().buildStyle()}
        {StyleSheetBuilder.noneChecker(value=self.width, prefix="width:", suffix="px")}
         {StyleSheetBuilder.noneChecker(value=self.height, prefix="height:", suffix="px")}
                
"""


class MainArrange:
    start = [Qt.AlignTop, Qt.AlignLeft]
    center = [Qt.AlignVCenter, Qt.AlignHCenter]
    end = [Qt.AlignBottom, Qt.AlignRight]


class CrossArrange:
    start = [Qt.AlignLeft, Qt.AlignTop]
    center = [Qt.AlignHCenter, Qt.AlignVCenter]
    end = [Qt.AlignRight, Qt.AlignBottom]
