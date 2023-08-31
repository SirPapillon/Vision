from vision.components.base import Widget


class EventRecognizer(Widget):
    def __init__(self,child,
                 onPressed:lambda event:None=None,
                 onHovered:lambda event:None=None,
                 onLeave:lambda event:None=None,
                 onMouseDoubleClick:lambda event:None=None,
                 onDraging:lambda event:None=None,
                 name=None):
        super().__init__(name)
        self.child = child
        self.onPressed = onPressed
        self.onHovered = onHovered
        self.onLeave = onLeave
        self.onMouseDoubleClick = onMouseDoubleClick
        self.onDraging = onDraging

    def configGestures(self,widget):

        if self.onPressed is not None:
            widget.mousePressEvent = lambda event:self.onPressed(event)

        if self.onHovered is not None:
            widget.enterEvent = lambda event:self.onHovered(event)

        if self.onLeave is not None:
            widget.leaveEvent = lambda event:self.onLeave(event)

        if self.onMouseDoubleClick is not None:
            widget.mouseDoubleClickEvent = lambda event:self.onMouseDoubleClick(event)

        if self.onDraging:
            widget.moveEvent = lambda event:self.onDraging(event)


    def buildWidget(self, parent):
        self.parent = parent
        self.widget = self.child.buildWidget(parent)
        self.configGestures(self.widget)
        return self.widget
    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)