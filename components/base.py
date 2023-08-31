import random
from vision import widget_dict

class Widget:
    parent = None
    widget = None
    id = None


    def __init__(self,name):
        if self.id is not None:
            return

        self.id = str(random.randint(100000, 999999))
        self.name = self.id if name is None else str(name)
        widget_dict[self.name] = self


    def buildWidget(self, parent):
        pass

    def renderWidget(self, parent):
        pass

    def applyStyle(self):
        pass

    @property
    def widget_height(self):
        return self.widget.height()

    @property
    def widget_width(self):
        return self.widget.width()
