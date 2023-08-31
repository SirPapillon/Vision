from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from vision.components.base import Widget
from vision.utils import *

class TableView(Widget):
    def __init__(self,rows:list,headers:list=None,rowCount=None,headCount=None,
                 design:TableDesign = TableDesign(),name = None):
        super().__init__(name)
        self.headers = headers
        self.rows = rows
        self.design = design
        self.rowCount = rowCount if rowCount is not None else len(rows)
        self.headCount = headCount if headCount is not None else len(headers)

    def getHeadIndexByName(self, headName):
        col_count = self.headCount
        for col in range(col_count):
            if self.widget.horizontalHeaderItem(col).text() == headName:
                return col

    def buildRows(self):
        rowIndex = 0
        self.widget.setRowCount(self.rowCount)
        for i_r in range(len(self.rows)):
            for rowName in self.rows[i_r].kwargs:
                print(rowName)
                value = self.rows[i_r].kwargs[rowName]
                headIndex = self.getHeadIndexByName(rowName)
                if type(value) == Cell:
                    cell = QTableWidgetItem(value.title)
                    if value.backgroundColor is not None:
                        bgColor = value.backgroundColor.rgba()
                        cell.setBackground(QColor(bgColor[0],bgColor[1],bgColor[2]))

                    if value.style is not None:
                        style = value.style
                        if style.color is not None:
                            try:
                                color = style.color.rgba()
                            except:
                                color = style.color
                            cell.setForeground(QColor(color[0],color[1],color[2]))

                else:
                    cell = QTableWidgetItem(value)
                self.widget.setItem(rowIndex,headIndex,cell)
            rowIndex+=1





    def buildWidget(self, parent):
        self.widget = QTableWidget(parent)
        self.widget.setObjectName(self.id)
        if self.headers is not None:
            self.widget.setColumnCount(self.headCount)
            self.widget.setHorizontalHeaderLabels(self.headers)
        self.applyStyle()
        self.buildRows()

        return self.widget

    def renderWidget(self, parent):
        pass
    def applyStyle(self):
        self.widget.setStyleSheet(f"""
        #{self.id}{{
        {self.design.buildStyle()}
                        outline:none;

        }}
        
        
        
        #{self.id} QHeaderView::section{{
        


        }}
        
        #{self.id}::item{{
        {self.design.cellDesign.buildStyle()}
        }}
        
        #{self.id}::item:hover{{
        {self.design.hoverDesign.buildStyle()}
        }}
        
        #{self.id}::item:selected{{
        
                        {self.design.selectionDesign.buildStyle()}

        }}

        
        



""")

class TableRow:
    def __init__(self,**kwargs):
        self.kwargs = kwargs

class Cell:
    def __init__(self,title,backgroundColor:Colors = None,style:TextStyle = TextStyle()):
        self.title = title
        self.backgroundColor = backgroundColor
        self.style = style
