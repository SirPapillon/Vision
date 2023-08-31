from PyQt5.QtCore import Qt


class TBarSide:
    @classmethod
    def left(cls):
        return Qt.LeftToolBarArea

    @classmethod
    def right(cls):
        return Qt.RightToolBarArea

    @classmethod
    def top(cls):
        return Qt.TopToolBarArea

    @classmethod
    def bottom(cls):
        return Qt.BottomToolBarArea
