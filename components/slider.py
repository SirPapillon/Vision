from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
from vision.components.base import Widget


class Slider(Widget):
    def __init__(self,name=None, range: range = range(100),
                 interval = None,
                  onChanged: lambda value: float = None):
        super().__init__(name)
        self.range = range
        self.interval = interval
        self.onChanged = onChanged

    def buildWidget(self, parent):
        self.widget = QSlider(Qt.Horizontal)
        self.widget.setMinimum(self.range.start)
        self.widget.setMaximum(self.range.stop)
        self.widget.setTickPosition(QSlider.TicksBelow)

        if self.onChanged is not None:
            self.widget.valueChanged.connect(self.onChanged)

        if self.interval is not None:
            self.widget.setTickInterval(self.interval)

        return self.widget

    def renderWidget(self, parent):
        self.widget = self.buildWidget(parent)
        self.widget.grid()
