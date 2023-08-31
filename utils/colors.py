from __future__ import annotations

from PyQt5.QtGui import QColor

class Color:
    def __init__(self,hexColor:Colors,alpha=100):
        self.alpha = alpha
        if hexColor[0]!="#":
            hexColor+="#"

        self.hexColor = hexColor

    def __str__(self):
        return str(self.rgba())

    def rgba(self):
        hexColor = self.hexColor.lstrip("#")
        return (tuple(int(hexColor[i:i+2], 16) for i in (0, 2, 4)))+(self.alpha * 2.55,)

    def withAlpha(self,alpha):
        self.alpha = alpha
        return self.rgba()

class Colors:
    white = Color("#FFFFFF")
    black = Color("#000000")
    transparent = Color("#00000000").withAlpha(0)
    red = Color("#FF0000")
    pink = Color("#FFC0CB")
    purple = Color("#800080")
    deepPurple = Color("#673AB7")
    indigo = Color("#3F51B5")
    blue = Color("#2196F3")
    lightBlue = Color("#87CEEB")
    cyan = Color("#00BCD4")
    teal = Color("#009688")
    green = Color("#4CAF50")
    lightGreen = Color("#8BC34A")
    lime = Color("#CDDC39")
    yellow = Color("#FFEB3B")
    amber = Color("#FFC107")
    orange = Color("#FF9800")
    deepOrange = Color("#FF5722")
    brown = Color("#795548")
    grey = Color("#9E9E9E")
    blueGrey = Color("#607D8B")

    def __init__(self,hexColor:Colors):
        self.hexColor = hexColor

    @classmethod
    def fromHex(cls,hex):
        return Color(hex)









