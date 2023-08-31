from PyQt5.QtWidgets import QAction
from vision.components.base import Widget
from ..components.inherited_classes import DerivedQMainWindow
from vision.utils import *



class MenuBar(Widget):
    def __init__(self, items: list, design: MenuBarDesign = MenuBarDesign(), name=None):
        super().__init__(name)
        self.items = items
        self.design = design

    def buildItems(self):
        for item in self.items:
            item.buildItem(self.widget)

    def buildWidget(self, parent: DerivedQMainWindow):
        self.widget = parent.menuBar()
        self.buildItems()
        self.applyStyle()
        return self.widget

    def renderWidget(self, parent: DerivedQMainWindow):
        self.widget = self.buildWidget(parent)

    def applyStyle(self):
        design = self.design
        itemsPadding = self.design.itemsPadding
        border = design.border
        actionsBorder = design.actionsBorder
        stylesheet = f"""
        QMenuBar {{
    {StyleSheetBuilder.buildColor(color=design.backgroundColor, prefix="background-color:")};
            {"" if border is None else f"border: {border.width}px solid {border.color};"}
        }}

        QMenuBar::item {{
            {"" if itemsPadding is None else f"padding: {itemsPadding.left}px,{itemsPadding.top}px,{itemsPadding.right}px,{itemsPadding.bottom}px;"}
                {StyleSheetBuilder.buildColor(color=design.itemsBgColor, prefix="background-color:")};
                {StyleSheetBuilder.buildColor(color=design.itemsFrColor, prefix="color:")};
        }}

        QMenuBar::item:selected {{
            {StyleSheetBuilder.buildColor(color=design.itemsHoverBgColor, prefix="background-color:")};
            color: {design.itemsHoverFrColor}
        }}
        
        QMenu::item::selected{{
         {StyleSheetBuilder.buildColor(color=design.actionsHoverBgColor, prefix="background-color:")};
        color: {design.actionsHoverFrColor};
        }}
        
        QMenu::separator {{
            {StyleSheetBuilder.buildColor(color=design.seperatorColor, prefix="background-color:")};

            height: {1 if design.seperatorWidth is None else design.seperatorWidth}px;
        }}

        QMenu {{
            {"" if actionsBorder is None else f"border: {actionsBorder.width}px solid {actionsBorder.color};"}
            {StyleSheetBuilder.buildColor(color=design.actionsBgColor, prefix="background-color:")};
            {StyleSheetBuilder.buildColor(color=design.actionsFrColor, prefix="color:")};

        }}
        """

        self.widget.setStyleSheet(stylesheet)


class MenuAction:
    def __init__(self, title, actions: list = None,
                 shortcut:str=None,
                 onPressed: lambda: None = None,
                 hoverColor: Colors = Colors.blue,
                 backgroundColor: Colors = Colors.white):
        self.title = title
        self.actions = actions
        self.hoverColor = hoverColor
        self.backgroundColor = backgroundColor
        self.onPressed = onPressed
        self.shortcut = shortcut

    def buildAction(self, parent):
        if self.actions is None:
            actMenu = QAction(self.title, parent)
            if self.shortcut is not None:
                actMenu.setShortcut(self.shortcut)
            actMenu.triggered.connect(self.onPressed if self.onPressed is not None else lambda: None)
            parent.addAction(actMenu)
            return

        subMenu = parent.addMenu(self.title)

        subMenu.triggered.connect(self.onPressed if self.onPressed is not None else lambda: None)

        for action in self.actions:
            action.buildAction(subMenu)


class MenuItem:
    def __init__(self, title, actions: list = None, onPressed: lambda: None = None,
                 shortcut:str = None,
                 hoverColor: Colors = Colors.blue,
                 backgroundColor: Colors = Colors.white):
        self.title = title
        self.actions = actions
        self.onPressed = onPressed
        self.hoverColor = hoverColor
        self.backgroundColor = backgroundColor
        self.shortcut = shortcut

    def buildItem(self, parent: DerivedQMainWindow):
        if self.actions is None:
            actMenu = QAction(self.title, parent)
            actMenu.triggered.connect(self.onPressed if self.onPressed is not None else lambda: None)
            return
        subMenu = parent.addMenu(self.title)


        for action in self.actions:
            action.buildAction(subMenu)


class MenuSeperator:
    def __init__(self):
        pass

    def buildAction(self, parent):
        parent.addSeparator()
