# https://www.qtcentre.org/threads/53745-QPixmap-as-background-of-QWidget
from moduls.QvImports  import *

from qgis.core import QgsRectangle, QgsPointXY
from qgis.gui import QgsMapTool
from moduls.QvConstants import QvConstants
from moduls.QvPushButton import QvPushButton
from configuracioQvista import *
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QApplication, QMessageBox
from moduls import QvFuncions
from moduls.QVCercadorAdreca import QCercadorAdreca
from moduls.QvMultiruta import *
from moduls.QvReverse import QvReverse

class QAdrecaPostalLineEdit(QLineEdit):
    def focusInEvent(self, event):
        if self.text().startswith("Punt seleccionat"):
            self.setText('')
        super(QAdrecaPostalLineEdit, self).focusInEvent(event)

class QPointNameLabel(QLabel):
    def __init__(self, buddy, parent = None):
        super(QPointNameLabel, self).__init__(parent)
        self.buddy = buddy

    # When it's clicked, hide itself and show its buddy
    def mousePressEvent(self, event):
        self.hide()
        self.buddy.show()
        self.buddy.setFocus() # Set focus on buddy so user doesn't have to click again

class PointUI:
    pointList = []
    #layout
    #eina

    def __init__(self,lay,eina):
        self.layout = lay
        self.eina = eina

    def addItem(self,customName):
        new_element = PointUI_element(self.layout,len(self.pointList),customName,self) #la classe PointUI_element ja s'encarrega d'afegir al layout el conjunt d'elements
        self.pointList.append(new_element)
        # self.eina.routePoints.append(QgsPointXY(-1,-1))
        # self.eina.routePointMarkers.append(QgsVertexMarker(self.eina.canvas))
        self.refreshLayout()
        self.checkRemoveButtons()

    def addBetweenPoints(self,actPoint,customName):
        new_element = PointUI_element(self.layout,actPoint,customName,self) #la classe PointUI_element ja s'encarrega d'afegir al layout el conjunt d'elements
        i = actPoint
        while i < len(self.pointList):
            self.pointList[i].pointNumber = self.pointList[i].pointNumber + 1
            self.pointList[i].updateLbl()
            i += 1
        self.pointList.insert(actPoint, new_element)
        self.refreshLayout()
        self.checkRemoveButtons()

    #check whether the remove items need to be enabled or not
    def checkRemoveButtons(self):
        if len(self.pointList) > 2:
            self.enableRemoveButtons()
        else:
            self.disableRemoveButtons()

    def enableRemoveButtons(self):
        for el in self.pointList:
            el.buttonRemovePoint.setEnabled(True)

    def disableRemoveButtons(self):
        for el in self.pointList:
            el.buttonRemovePoint.setEnabled(False)

    def refreshLayout(self):
        #eliminar i tornar a afegir els layouts per a que estiguin endreçats
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).setParent(None)

        for el in self.pointList:
            self.layout.addLayout(el.layoutPunt)

    def refreshLabels(self):
        #refrescar els labels que hi ha per cada punts
        for el in self.pointList:
            el.updateLbl()

    def removeItem(self,item):
        actLayout = self.layout.itemAt(item)

        #delete the marker
        self.eina.canvas.scene().removeItem(self.pointList[item].marker)

        #delete all the widgets from the layout
        for i in reversed(range(actLayout.count())):
            if actLayout.itemAt(i).widget() != None:
                actLayout.itemAt(i).widget().setParent(None)

        #delete the layout from the list
        actLayout.setParent(None)
        self.pointList.pop(item)

        #renumerate the points
        for i, el in enumerate(self.pointList):
            el.pointNumber = i

        #refresca els textos dels noms dels punts
        self.refreshLabels()

        self.checkRemoveButtons()

    def pressButtonGPS(self,item):
        if self.pointList[item].buttonGPS.isChecked():
            for pointElement in self.pointList:
                pointElement.buttonGPS.setChecked(False)
                pointElement.LECarrer.setEnabled(True)
                pointElement.LENumero.setEnabled(True)
            self.pointList[item].buttonGPS.setChecked(True)
            self.pointList[item].LECarrer.setEnabled(False)
            self.pointList[item].LENumero.setEnabled(False)
        else:
            self.pointList[item].LECarrer.setEnabled(True)
            self.pointList[item].LENumero.setEnabled(True)
        
    #retornar els punts
    def getPoints(self):
        ret = []
        for pointElement in self.pointList:
            ret.append(pointElement.point)
        return ret

    #retornar els markers
    def getMarkers(self):
        ret = []
        for pointElement in self.pointList:
            ret.append(pointElement.marker)
        return ret

    #escriure el resultat de la reverse search als QLineEdits
    def setReverse(self,item,result):
        self.pointList[item].LECarrer.setText(result.nomCarrer)
        if (result.numCarrer != ""):
            self.pointList[item].LENumero.setText(result.numCarrer)

    def resetUI(self):
        #TODO: improve speed
        for i in reversed(range(len(self.pointList))):
            self.eina.canvas.scene().removeItem(self.pointList[i].marker)
            actLayout = self.pointList[i].layoutPunt
            #delete all the widgets from the layout
            for j in reversed(range(actLayout.count())):
                if actLayout.itemAt(j).widget() != None:
                    actLayout.itemAt(j).widget().setParent(None)

            #delete the layout from the list
            actLayout.setParent(None)
            self.pointList.pop(i)
        self.addItem("")
        self.addItem("")


class PointUI_element:
    #parent (layout)
    index = -1
    pointNumber = -1
    customName = ""
    #buttonGPS
    #point = QgsPointXY(-1,-1)

    def updateLbl(self):
        self.pointText_label.setText("Punt #" + str(self.pointNumber) + " " + self.customName)

    def pointNameEdited(self):
        self.customName = self.pointText_edit.text()
        self.updateLbl()
        self.pointText_edit.hide()
        self.pointText_label.show()

    def __init__(self,parent,pointNumber,customName,UIparent):
        self.parent = parent
        self.pointNumber = pointNumber
        self.UIparent = UIparent
        self.point = QgsPointXY(-1,-1)
        self.marker = QgsVertexMarker(self.UIparent.eina.canvas)
        eina = UIparent.eina

        self.layoutPunt = QHBoxLayout()

        self.pointText_edit = QLineEdit()
        self.pointText_edit.hide()
        self.pointText_edit.editingFinished.connect(self.pointNameEdited)
        self.pointText_label = QPointNameLabel(self.pointText_edit)
        self.pointText_label.setText("Punt #" + str(self.pointNumber) + " " + self.customName) #TODO: personalitzar noms
        self.layoutPunt.addWidget(self.pointText_edit)
        self.layoutPunt.addWidget(self.pointText_label)

        self.layoutAdrecaPostal = QHBoxLayout()
        self.layoutPunt.addLayout(self.layoutAdrecaPostal) #TODO: cercador postal universal

        self.lblTextCarrer = QLabel('Carrer:')
        self.LECarrer = QAdrecaPostalLineEdit()
        self.LECarrer.setToolTip('Introdueix adreça i selecciona de la llista')
        self.LECarrer.setMinimumWidth(200)

        self.lblTextNumero = QLabel('Núm:')
        self.LENumero = QAdrecaPostalLineEdit()
        self.LENumero.setToolTip('Introdueix número, selecciona de la llista i prem RETURN')
        self.LENumero.setMaximumWidth(100)
        self.LENumero.setMinimumWidth(100)

        self.buttonGPS = QPushButton("")
        self.buttonGPS.setGeometry(200, 150, 100, 30)
        self.parent.pointUI_index = self.pointNumber
        self.buttonGPS.clicked.connect(lambda: eina.getCoords(self.pointNumber))
        self.buttonGPS.setCheckable(True)
        self.buttonGPS.setIcon(QIcon('Imatges/logoGPS.png'))
        
        self.buttonNewPoint = QPushButton("")
        self.buttonNewPoint.setGeometry(200, 150, 100, 30)
        self.buttonNewPoint.clicked.connect(lambda:self.UIparent.addBetweenPoints(self.pointNumber+1,""))
        self.buttonNewPoint.setIcon(QIcon('Imatges/logoNewPoint.png'))

        self.buttonRemovePoint = QPushButton("")
        self.buttonRemovePoint.setGeometry(200, 150, 100, 30)
        self.buttonRemovePoint.clicked.connect(lambda:self.UIparent.removeItem(self.pointNumber))
        self.buttonRemovePoint.setIcon(QIcon('Imatges/logoRemovePoint.png'))

        self.layoutPunt.addWidget(self.lblTextCarrer)
        self.layoutPunt.addWidget(self.LECarrer)
        self.layoutPunt.addWidget(self.lblTextNumero)
        self.layoutPunt.addWidget(self.LENumero)
        self.layoutPunt.addWidget(self.buttonGPS)
        self.layoutPunt.addWidget(self.buttonNewPoint)
        self.layoutPunt.addWidget(self.buttonRemovePoint)

        self.cercador = QCercadorAdreca(self.LECarrer, self.LENumero,'SQLITE')
        self.cercador.sHanTrobatCoordenades.connect(lambda:eina.APostaltoCoord(self.pointNumber))

class PointTool(QgsMapTool):  
        def __init__(self, canvas, parent):
            QgsMapTool.__init__(self, canvas)
            self.canvas = canvas  
            self.parent = parent

        def canvasPressEvent(self, event):
            auxPoint = QgsPointXY(event.mapPoint())
            print(str(self.parent.pointUI_index) + str(auxPoint))
            self.parent.pointUI.pointList[self.parent.pointUI_index].point = auxPoint
            self.parent.pointUI.pointList[self.parent.pointUI_index].marker.setCenter(auxPoint)
            self.parent.pointUI.setReverse(self.parent.pointUI_index, QvReverse(auxPoint))

@QvFuncions.creaEina(titol="Eina Multiruta (OSRM)", esEinaGlobal = True, apareixDockat = False)
class EinaMultiruta(QWidget):
    getPoint = 0
    """
    Valors del getPoint:
        0 - no seleccionar un punt
        1 - seleccionar punt inicial
        2 - seleccionar punt final
    """
    # canvas
    tool = None

    # pGirs = [] #punts de gir
    # indicacions = [] #descripcions de la ruta

    # routePoints = []
    # routePointMarkers = []

    ruta = QvMultiruta([None,None])
    roundtrip = False
    source = True
    destination = True

    #pointUI
    pointUI_index = -1

    def APostaltoCoord(self, index):
        self.pointUI_index = index
        auxPoint = self.pointUI.pointList[self.pointUI_index].cercador.coordAdreca
        if (auxPoint != None):
            self.pointUI.pointList[self.pointUI_index].point = auxPoint
            self.pointUI.pointList[self.pointUI_index].marker.setCenter(auxPoint)

    def getCoords(self, index):
            """
            handling botó d'obtenir punt inicial
            """
            self.pointUI_index = index
            self.canvas.setMapTool(self.tool)
            self.pointUI.pressButtonGPS(self.pointUI_index)

    def setRouteOptions_roundtrip(self, boolean):
        self.roundtrip = boolean
        if not boolean:
            self.tripOptions_puntinici.setEnabled(False)
            self.tripOptions_puntinici.setChecked(True)
            self.tripOptions_puntfinal.setEnabled(False)
            self.tripOptions_puntfinal.setChecked(True)
        else:
            self.tripOptions_puntinici.setEnabled(True)
            self.tripOptions_puntfinal.setEnabled(True)

    def setRouteOptions_source(self, boolean):
        self.source = boolean

    def setRouteOptions_destination(self, boolean):
        self.destination = boolean

    def __init__(self, pare):
        # def getIndicacions(girs):
        #     descripcions = []
        #     for gir in girs:
        #         descripcions.append(gir.descripcio)
        #     return descripcions

        def calcularRuta():
            self.canvas.unsetMapTool(self.tool)
            self.getPoint = 0

            self.ruta.hideRoute()
            # self.ruta.ocultarPuntsGir()
            self.ruta = QvMultiruta(self.pointUI.getPoints())
            self.ruta.setRouteOptions(self.roundtrip, self.source, self.destination)
            self.ruta.getRoute()
            self.ruta.printRoute(self.canvas)

            # self.indicacioBox.clear()
            # self.lblDistancia.setText("")
            # self.lblDurada.setText("")

            if (self.ruta.routeOK == False):
                print("error calculant la ruta")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error calculant la ruta")
                msg.setInformativeText("La ruta no s'ha pogut calcular. Provi amb uns altres punts i asseguri's que el seu ordinador està connectat a la xarxa interna.")
                msg.setWindowTitle("Error")
                msg.exec_()
                self.lblDistancia.setText("Distancia: No s'ha pogut obtenir")
                self.lblDurada.setText("Durada: No s'ha pogut obtenir")
                # self.layoutInfo.removeWidget(self.lblDistancia)
                # self.layoutInfo.removeWidget(self.lblDurada)
                
            else:
                # Mostra distancia i durada de la ruta
                # getDistanciaDurada()
                # Incialitzem layout per a mostrar descripcio de la ruta i els seus botons
                # getIndicacionsDeRuta()
                pass

                    
        def preparacioUI():
            def UIrouteOptions():
                self.routeOptionsLayout = QVBoxLayout()

                typeofRoute_layout = QHBoxLayout()

                tripOptions_groupbox = QGroupBox("Opcions de ruta òptima")
                tripOptions_layout = QHBoxLayout()
                tripOptions_groupbox.setLayout(tripOptions_layout)

                self.tripOptions_circular = QCheckBox("Ruta circular")
                self.tripOptions_circular.stateChanged.connect(lambda:self.setRouteOptions_roundtrip(self.tripOptions_circular.isChecked()))

                self.tripOptions_puntinici = QCheckBox("Punt de sortida fixat")
                self.tripOptions_puntinici.setToolTip("El primer punt de la llista serà el punt de sortida de la ruta")
                self.tripOptions_puntinici.stateChanged.connect(lambda:self.setRouteOptions_source(self.tripOptions_puntinici.isChecked()))

                self.tripOptions_puntfinal = QCheckBox("Punt d'arribada fixat")
                self.tripOptions_puntfinal.setToolTip("L'últim punt de la llista serà el punt de sortida de la ruta")
                self.tripOptions_puntfinal.stateChanged.connect(lambda:self.setRouteOptions_destination(self.tripOptions_puntfinal.isChecked()))

                tripOptions_layout.addWidget(self.tripOptions_circular)
                tripOptions_layout.addWidget(self.tripOptions_puntinici)
                tripOptions_layout.addWidget(self.tripOptions_puntfinal)

                self.routeOptionsLayout.addWidget(tripOptions_groupbox)

                #defualt values
                self.tripOptions_circular.setChecked(False)
                self.tripOptions_puntinici.setEnabled(False)
                self.tripOptions_puntinici.setChecked(True)
                self.tripOptions_puntfinal.setEnabled(False)
                self.tripOptions_puntfinal.setChecked(True)


            QWidget.__init__(self)

            if isinstance(pare, QgsMapCanvas):
                self.canvas = pare
            else: 
                self.canvas = pare.canvas
            
            lay = QVBoxLayout()
            self.setLayout(lay)

            self.pointLayout = QVBoxLayout()

            self.pointUI = PointUI(self.pointLayout,self)
            self.pointUI.addItem("Punt inici")
            self.pointUI.addItem("Punt final")

            UIrouteOptions()
            lay.addLayout(self.routeOptionsLayout)
            lay.addLayout(self.pointLayout)

            calcRouteButton = QPushButton()
            calcRouteButton.pressed.connect(calcularRuta)
            calcRouteButton.setText("Calcular ruta")
            lay.addWidget(calcRouteButton)

        preparacioUI()
        # self.initMarkers()
        self.tool = PointTool(self.canvas, self)

    def eventComboBox(self, index):
        self.canvas.setCenter(self.pGirs[int(index.row())].coord)
        self.canvas.zoomScale(1000)
        self.canvas.refresh()
    
    # def goNext(self):
    #     if(self.index != None):
    #         if(int(self.index) < self.indicacioBox.count()-1):
    #             self.index += 1
    #             self.canvas.setCenter(self.pGirs[self.index].coord)
    #             self.indicacioBox.setCurrentIndex(self.index)
    #             self.canvas.zoomScale(1000)
    #             self.canvas.refresh()

    # def goPrev(self):
    #     if(self.index != None):
    #         if(int(self.index) > 0):
    #             self.index -= 1
    #             self.canvas.setCenter(self.pGirs[self.index].coord)
    #             self.indicacioBox.setCurrentIndex(self.index)
    #             self.canvas.zoomScale(1000)
    #             self.canvas.refresh()

    # def initMarkers(self):
    #     self.mStart = QgsVertexMarker(self.canvas)
    #     self.mStart.setColor(QColor(255, 0, 0)) #(R,G,B)
    #     self.mStart.setIconSize(12)
    #     self.mStart.setIconType(QgsVertexMarker.ICON_CROSS)
    #     self.mStart.setPenWidth(3)

    #     self.mEnd = QgsVertexMarker(self.canvas)
    #     self.mEnd.setColor(QColor(0, 0, 255)) #(R,G,B)
    #     self.mEnd.setIconSize(12)
    #     self.mEnd.setIconType(QgsVertexMarker.ICON_CROSS)
    #     self.mEnd.setPenWidth(3)

    def hideEvent(self,event):
        super().hideEvent(event)
        self.canvas.unsetMapTool(self.tool)
        self.ruta.hideRoute()
        self.pointUI.resetUI()

    def showEvent(self,event):
        super().showEvent(event)
        self.getPoint = 0
        # self.resize(self.minimumSizeHint())

if __name__ == "__main__":
    from qgis.gui import  QgsLayerTreeMapCanvasBridge
    from moduls.QvLlegenda import QvLlegenda
    from qgis.gui import QgsMapCanvas
    from qgis.core import QgsProject
    from qgis.core.contextmanagers import qgisapp

    projecteInicial = 'MapesOffline/qVista default map.qgs'

    with qgisapp() as app:
        win = QMainWindow()
        # canvas = QvCanvas(llistaBotons=llistaBotons, posicioBotonera = 'SE', botoneraHoritzontal = True)
        canvas = QgsMapCanvas()
        win.setCentralWidget(canvas)
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        bridge = QgsLayerTreeMapCanvasBridge(root,canvas)

        # leyenda = QvLlegenda(canvas, tablaAtributos)
        qvEinaRuta = EinaMultiruta(canvas)
        dwEC = QDockWidget()
        dwEC.setWidget(qvEinaRuta)
        win.addDockWidget(Qt.LeftDockWidgetArea, dwEC)
        win.show()
        project.read(projecteInicial)      
            
            