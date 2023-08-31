from PyQt5.QtWidgets import QPushButton
from vision.components.base import Widget
from vision.utils import *
from vision import widget_dict

class Button(Widget):

    def __init__(self,
                 onPressed: lambda: None,
                 onReleased: lambda: None = None,
                 onHovered: lambda: None = None,
                 onLeaved: lambda: None = None,
                 name=None,
                 design: ButtonDesign = ButtonDesign(),
                 hoverDesign: ButtonDesign = ButtonDesign(text=None),
                 x: float = 0, y: float = 0):
        super().__init__(name)

        self.onPressed = onPressed
        self.onReleased = onReleased
        self.onHovered = onHovered
        self.onLeaved = onLeaved
        self.hoverDesign = hoverDesign
        self.x = x
        self.y = y
        self.design = design
        widget_dict[self.name] = self

    def _onHovered(self,event):
        print(self.hoverDesign.text)
        # if self.hoverDesign.text is not None:
        #     self.widget.setText(self.hoverDesign.text)
        if self.onHovered is not None:
            self.onHovered()


    def _onLeaved(self,event):
        self.widget.setText(self.design.text)
        if self.onLeaved is not None:
            self.onLeaved()
    def configGesture(self):
        if self.onPressed is not None:
            self.widget.mousePressEvent = lambda e:self.onPressed()
        if self.onReleased is not None:
            self.widget.released.connect(self.onReleased)

        self.widget.enterEvent = lambda event: self._onHovered(event)
        self.widget.leaveEvent = lambda event: self._onLeaved(event)

            # onLeaved
    def buildWidget(self, parent):
        self.widget = QPushButton(self.design.text,parent)

        self.widget.setObjectName(self.id)
        self.configGesture()

        self.applyStyle()
        return self.widget

    def renderWidget(self, parent):
        self.parent = self.parent
        self.buildWidget(parent)

    def applyStyle(self):

        self.widget.setStyleSheet(f"""
        #{self.id}{{
        {self.design.buildStyle()}
        }}
        #{self.id}::hover{{
        {self.hoverDesign.buildStyle()}
        }}
        """)



    def getHeight(self):
        return self.widget.winfo_height()

    def getWidth(self):
        return self.widget.winfo_width()
