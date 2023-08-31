from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow


class DerivedQMainWindow(QMainWindow):
    def __init__(self,trackMouseMovement:lambda x,y:None = None):
        super().__init__()

        self.trackMouseMovement = trackMouseMovement
        self.configGestures()

    def buildMenu(self,menu):
        if menu is None:
            return
        menu.buildWidget(self)

    def buildDockBody(self,dockBody):
        if dockBody is None:
            return
        dockBody.buildWidget(self)

    def buildToolBars(self,toolBars):
        if toolBars is None:
            return
        for bar in toolBars:
            self.addToolBar(bar.side,bar.buildWidget(self))


    def buildStatusBar(self,statusBar):
        if statusBar is None:
            return
        self.setStatusBar(statusBar.buildWidget(self))
    def configGestures(self):
        if self.trackMouseMovement is not None:
            self.setMouseTracking(True)
            mouse_tracked = pyqtSignal(int, int)
            mouse_tracked.connect(self.trackMouseMovement)

