from PyQt5.QtWidgets import QProgressBar
from vision.components.base import Widget
from vision.utils import *



class ProgressBarHandler:
    def __init__(self):
        pass

    def setValue(self, value):
        pass

    def reset(self):
        pass


class ProgressBar(Widget):
    def __init__(self,
                 action: lambda progressBar: ProgressBar,
                 onChanged: lambda value: None = None,
                 onEnd: lambda: None = None,
                 design: ProgressBarDesign = ProgressBarDesign(),
                 endDesign: ProgressBarDesign = ProgressBarDesign(),
                 handler: ProgressBarHandler = None,
                 range: range = range(0, 100),
                 name=None):
        super().__init__(name)

        if handler is not None:
            handler.reset = self.reset
            handler.setValue = self.setValue

        self.action = action
        self.range = range
        self.handler = handler
        self.design = design
        self.onChanged = onChanged
        self.endDesign = endDesign
        self.onEnd = onEnd

    def setValue(self, value):
        self.widget.setValue(value)

    def reset(self):
        self.widget.reset()

    def configGestures(self):
        # Thread(target=self.action, args=[self]).start()
        self.widget.valueChanged.connect(lambda value: self._onChanged(value))

    def _onChanged(self, value):

        if self.onChanged is not None:
            self.onChanged()

        if self.onEnd is not None:
            if value is self.widget.maximum():
                self.onEnd()

        if self.endDesign is None:
            return

        if value == self.widget.maximum():
            self.widget.setStyleSheet(
                f"""
                {self.widget.styleSheet()}
                #{self.id} {{
                {StyleSheetBuilder.buildBorder(self.endDesign.border)}
                {StyleSheetBuilder.buildPadding(self.endDesign.padding)}
                {StyleSheetBuilder.buildBorderRadius(self.endDesign.borderRadius)}
                {StyleSheetBuilder.buildColor(self.endDesign.backgroundColor, prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(self.endDesign.style)}
                text-align: center;
                    }}
                    #{self.id}::chunk {{
                    {StyleSheetBuilder.buildColor(self.endDesign.chunkColor, prefix="background-color:")}
                    {StyleSheetBuilder.buildBorderRadius(self.endDesign.chunkBorderRadius)}
                    {StyleSheetBuilder.buildBorder(self.endDesign.chunkBorder)}
                    }}
                        
"""
            )

    def buildWidget(self, parent):
        self.widget = QProgressBar(parent)
        self.applyStyle()
        self.widget.setObjectName(self.id)
        self.widget.setMaximum(self.range.stop)
        self.widget.setMinimum(self.range.start)
        self.configGestures()
        return self.widget

    def renderWidget(self, parent):
        pass

    def applyStyle(self):
        if self.design.backgroundColor is not None and self.design.borderRadius is None:
            self.design.borderRadius = BorderRadius.zero()
        # if self.design.borderRadius is not None and self.design.chunkBorderRadius is  None:
        #     self.design.chunkBorderRadius = self.design.borderRadius
        self.widget.setStyleSheet(f"""
        
                    #{self.id} {{
                {StyleSheetBuilder.buildBorder(self.design.border)}
                {StyleSheetBuilder.buildPadding(self.design.padding)}
                {StyleSheetBuilder.buildBorderRadius(self.design.borderRadius)}
                {StyleSheetBuilder.buildColor(self.design.backgroundColor, prefix="background-color:")}
                {StyleSheetBuilder.buildTextStyle(self.design.style)}
                text-align: center;
                    }}
                    #{self.id}::chunk {{
                    {StyleSheetBuilder.buildColor(self.design.chunkColor, prefix="background-color:")}
                    {StyleSheetBuilder.buildBorderRadius(self.design.chunkBorderRadius)}
                    {StyleSheetBuilder.buildBorder(self.design.chunkBorder)}
                    }}
                """)
