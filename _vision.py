from PyQt5.QtWidgets import QApplication
from .components.inherited_classes.derived_qwindow import DerivedQMainWindow
from .themes import ThemeMode
from .utils import *
from .components import *
from vision import widget_dict
from vision.components.base import Widget
from vision.utils.messageTypes import WarningMessage, QuestionMassage
import sys

class Vision(QApplication):

    def __init__(self,body,themeMode:ThemeMode =ThemeMode.default,
                 onMouseMove:lambda e:None=None,
                 trackMouseMovement:lambda x,y:None=None,
                 menuBar: MenuBar = None,
                 toolBars:list = None,
                 dockBody=None,
                 statusBar: StatusBar = None,

                 title="Vision App" , minSize=Size.zero(), maxSize=Size.zero(), size=Size(200, 200),
                 backgroundColor=Colors.white):
        super().__init__(sys.argv)

        self.statusBar = statusBar
        self.menuBar = menuBar
        self.dockBody = dockBody
        self.toolBars = toolBars


        # root configs
        self.minSize = size
        self.maxSize = size
        self.backgroundColor = backgroundColor

        self.onMouseMove = onMouseMove
        self.trackMouseMovement = trackMouseMovement


        self.body = body

        # self.setStyle(QStyleFactory.create('Cleanlooks'))
        self.window = DerivedQMainWindow()
        self.window.setWindowTitle(title)
        self.window.buildMenu(self.menuBar)
        self.window.buildStatusBar(self.statusBar)
        self.window.buildDockBody(self.dockBody)
        self.window.buildToolBars(self.toolBars)

        self.window.setGeometry(100, 100, size.width, size.height)
        self.configGesture()
        self.window.setObjectName("mainWindow")
        self.window.setStyleSheet(f"""
        #mainWindow{{
                {StyleSheetBuilder.buildColor(color=self.backgroundColor,prefix="background-color:")}

        }}
        """)

        # widgets tree
        self.body.renderWidget(parent=self.window)
        self.window.show()
        sys.exit(self.exec_())


    def configGesture(self):
        if self.onMouseMove is not None:
            self.window.mouseMoveEvent = self.onMouseMove


    def refresh(self):
        pass

    def getWidget(self,name) -> Widget:
        return widget_dict[name]




    def run(self):
        pass


    @property
    def height(self):
        return

    @property
    def width(self):
        return


def runApp(app):
    app()