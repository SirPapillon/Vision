from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QSizePolicy

from vision import widget_dict
from vision.components.base import Widget
from vision.components.statusbar import StatusBar
from vision.utils import Padding
from ..inherited_classes.derived_qwindow import DerivedQMainWindow
from ..menubar import MenuBar
from ...utils.handlers.vhandler import VHandler


class VBody(Widget):
    index = 0
    def __init__(self, body: list,
                 handler:VHandler=None,
                 contentPadding:Padding = Padding.zero(),
                 name=None,


                 ):
        super().__init__(name)
        self.body = body
        self.contentPadding = contentPadding


        self.handler = handler
        self.stackedWidget = None


        widget_dict[self.name] = self

        if self.handler is not None:
            self.handler.moveToView = self.moveToView
            self.handler.pop = self.pop

    def moveToView(self,view):
        self.stackedWidget.addWidget(view.buildWidget(self.parent))
        self.index += 1
        self.stackedWidget.setCurrentIndex(self.index)
    def pop(self):
        self.index -= 1
        self.stackedWidget.setCurrentIndex(self.index)

    def renderWidget(self, parent:DerivedQMainWindow):

        self.parent = parent

        if self.stackedWidget is None:
            self.stackedWidget = QStackedWidget(parent)
        self.widget = self.buildWidget(self.stackedWidget)

        self.stackedWidget.addWidget(self.widget)
        parent.setCentralWidget(self.stackedWidget)
    def buildWidget(self, parent):

        body = QVBoxLayout()
        body.setSpacing(0)
        body.setContentsMargins(
            self.contentPadding.left,
            self.contentPadding.top,
            self.contentPadding.right,
            self.contentPadding.bottom
        )

        body.setAlignment(Qt.AlignTop)
        widget = QWidget()
        widget.setLayout(body)

        for child in self.body:
            body.addWidget(child.buildWidget(parent=parent))

        return widget

