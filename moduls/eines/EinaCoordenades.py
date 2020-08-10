# https://www.qtcentre.org/threads/53745-QPixmap-as-background-of-QWidget
from moduls.QvImports  import *

from qgis.core import QgsRectangle, QgsPointXY
from qgis.gui import QgsMapTool
from moduls.QvConstants import QvConstants
from moduls.QvPushButton import QvPushButton
from configuracioQvista import *
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout 
from PyQt5.QtWidgets import QHBoxLayout, QFrame
from PyQt5.QtWidgets import  QApplication
from moduls import QvFuncions


# import time

@QvFuncions.creaEina(titol="Eina Coordenades", esEinaGlobal = True, apareixDockat = False)
class EinaCoordenades(QWidget):

    def __init__(self, pare):
        
        QWidget.__init__(self)
        if isinstance(pare, QgsMapCanvas):
            self.canvas = pare
        else: 
            self.canvas = pare.canvas
        self.setParent(pare)
        self.pare = pare
        self.nova = True

        lay = QVBoxLayout()
        self.setLayout(lay)

        def novaCoordenada():
            self.nova = True

        nou = QPushButton()
        nou.pressed.connect(novaCoordenada)
        nou.setText("Nou punt")
        lay.addWidget(nou)

        lay1 = QHBoxLayout()
        lay2 = QHBoxLayout()
        lay3 = QHBoxLayout()

        lblnom1 = QLabel()
        lblnom1.setText("ETRS 89")
        lblnom2 = QLabel()
        lblnom2.setText("Lat/Long")
        lblnom3 = QLabel()
        lblnom3.setText("TRESOR")

        self.leXcoord1 = QLineEdit()
        self.leXcoord1.setReadOnly(True)
        self.leYcoord1 = QLineEdit()
        self.leYcoord1.setReadOnly(True)

        self.leXcoord2 = QLineEdit()
        self.leXcoord2.setReadOnly(True)
        self.leYcoord2 = QLineEdit()
        self.leYcoord2.setReadOnly(True)

        self.leXcoord3 = QLineEdit()
        self.leXcoord3.setReadOnly(True)
        self.leYcoord3 = QLineEdit()
        self.leYcoord3.setReadOnly(True)

        def f1():
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text1)
        
        def f2():
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text2)
        
        def f3():
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text3)

        icona_copiar = QIcon('Imatges/file-document.png')
        b1 = QPushButton()
        b1.pressed.connect(f1)
        b1.setIcon(icona_copiar)
        b1.setToolTip("Copia al portaretalls")
        b2 = QPushButton()
        b2.pressed.connect(f2)
        b2.setIcon(icona_copiar)
        b2.setToolTip("Copia al portaretalls")
        b3 = QPushButton()
        b3.pressed.connect(f3)
        b3.setIcon(icona_copiar)
        b3.setToolTip("Copia al portaretalls")

        lay1.addWidget(lblnom1)
        lay1.addWidget(self.leXcoord1)
        lay1.addWidget(self.leYcoord1)
        lay1.addWidget(b1)
        lay2.addWidget(lblnom2)
        lay2.addWidget(self.leXcoord2)
        lay2.addWidget(self.leYcoord2)
        lay2.addWidget(b2)
        lay3.addWidget(lblnom3)
        lay3.addWidget(self.leXcoord3)
        lay3.addWidget(self.leYcoord3)
        lay3.addWidget(b3)

        lay.addLayout(lay1)
        lay.addLayout(lay2)
        lay.addLayout(lay3)

        def showXY(p): 
            if self.nova:
                sistemaCoords = canvas.mapSettings().destinationCrs().authid()
                
                if sistemaCoords != "EPSG:25831":
                    self.transformacio = QgsCoordinateTransform(QgsCoordinateReferenceSystem(sistemaCoords), 
                        QgsCoordinateReferenceSystem("EPSG:25831"), 
                        QgsProject.instance())
                    p=self.transformacio.transform(p)
                x1=str("%.3f" % p.x())
                y1=str("%.3f" % p.y())
                self.leXcoord1.setText(x1)
                self.leYcoord1.setText(y1)
                self.text1 = x1 + ", " + y1

                if sistemaCoords != "EPSG:4326":
                    self.transformacio = QgsCoordinateTransform(QgsCoordinateReferenceSystem(sistemaCoords), 
                            QgsCoordinateReferenceSystem("EPSG:4326"), 
                            QgsProject.instance())
                    p=self.transformacio.transform(p)
                y2 = str("%.7f" % p.x())
                x2 = str("%.7f" % p.y())
                self.leXcoord2.setText(x2)
                self.leYcoord2.setText(y2)
                self.text2 = x2 + ", " + y2

                x3= str(int((float(x1) - 400000) * 1000))
                y3= str(int((float(y1) - 4500000) * 1000))
                self.leXcoord3.setText(x3)
                self.leYcoord3.setText(y3)
                self.text3 = x3 + ", " + y3
        
        self.canvas.xyCoordinates.connect(showXY)

        class PointTool(QgsMapTool):   
            def __init__(self, canvas, parent):
                QgsMapTool.__init__(self, canvas)
                self.canvas = canvas  
                self.parent = parent
                self.m1 = QgsVertexMarker(canvas)
                self.m1.setColor(QColor(255,0, 0)) #(R,G,B)
                self.m1.setIconSize(12)
                self.m1.setIconType(QgsVertexMarker.ICON_CROSS)
                self.m1.setPenWidth(3)

            def canvasPressEvent(self, event):
                self.parent.nova = False
                x = self.parent.leXcoord1.text()
                y = self.parent.leYcoord1.text()
                self.m1.setCenter(QgsPointXY(float(x),float(y)))
                self.m1.show()

        self.tool = PointTool(self.canvas, self)
        self.canvas.setMapTool(self.tool)

    def hideEvent(self,event):
        super().hideEvent(event)
        self.canvas.unsetMapTool(self.tool)
        self.canvas.scene().removeItem(self.tool.m1)

    def showEvent(self,event):
        super().showEvent(event)
        self.canvas.setMapTool(self.tool)

        
if __name__ == "__main__":
       
    with qgisapp() as app:
        from qgis.gui import  QgsLayerTreeMapCanvasBridge
        from moduls.QvLlegenda import QvLlegenda
        from qgis.gui import QgsMapCanvas
        from qgis.core import QgsProject
        from qgis.core.contextmanagers import qgisapp
     
        # Canvas, projecte i bridge
        start1 = time.time()
        canvas=QgsMapCanvas()
        
        canvas.show()
        canvas.setRotation(0)
        project = QgsProject.instance()
        projecteInicial='mapesOffline/qVista default map.qgs'

        if project.read(projecteInicial):
            root = project.layerTreeRoot()
            bridge = QgsLayerTreeMapCanvasBridge(root, canvas)
            qvEinaCoords = EinaCoordenades(pare=canvas)
            #dwLay = QVBoxLayout()
            dwEC = QDockWidget()
            dwEC.setWidget(qvEinaCoords)
            dwEC.show()
            print ('resto: ',time.time()-start1)
        else:
            print("error en carga del proyecto qgis")