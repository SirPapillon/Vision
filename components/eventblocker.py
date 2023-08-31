from vision.components.base import Widget



class EventBlocker(Widget):
    def __init__(self,
                 child,
                 name=None,
                 blockAll=False,
                 blockMousePress = False,

                 ):
        super().__init__(name)
        self.child = child
        self.blockAll = blockAll
        self.blockMousePress = blockMousePress

    def blockGestures(self,widget):
        if self.blockMousePress or self.blockAll:
            widget.mousePressEvent = None


    def buildWidget(self, parent):
        self.parent = parent
        self.widget = self.child.buildWidget(parent)
        self.blockGestures(self.widget)
        return self.widget
    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)