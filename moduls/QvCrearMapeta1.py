# https://doc.qt.io/qt-5/qwidget.html#grab

import math
import os.path
from qgis.PyQt.QtGui import QPixmap
from qgis.core import QgsRectangle,   QgsProject, QgsPointXY, QgsGeometry
from qgis.PyQt.QtCore import QUrl
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from qgis.gui import QgsMapTool, QgsRubberBand
from qgis.core.contextmanagers import qgisapp
from PyQt5.QtCore import QModelIndex, Qt, QRect, QPoint, QTimer, QSize, QObject, pyqtSignal, QEvent

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QDockWidget, QTreeView,\
    QAction, QVBoxLayout, QGridLayout, QSplitter
from PyQt5.QtWidgets import  QHBoxLayout ,QAbstractItemView, QLabel, QWidget, QLineEdit,\
     QPushButton, QSpinBox, QFileDialog, QSpacerItem,QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QBrush
from moduls.QvPushButton import QvPushButton

projecteInicial=r'D:\tmp\alella.qgs'
projecteInicial=r'mapesOffline/corbera.qgs'
projecteInicial='mapesOffline/qVista default map.qgs'


    # def clickable(widget):
    #     '''
    #     Gestiona 
    #     '''
    #     class Filter(QObject):
    #         """ Clase para filtrar
    #         Recibe un QObject """
        
    #         clicked = pyqtSignal()
    #         # def __init__(self,app):
    #         #     super().__init__()

    #         def eventFilter(self, obj, event):
    #             if obj == widget:
    #                 evento= event.type()
    #                 if "Busco a apartir del eventon su constante":
    #                     if evento== 2:
    #                         print(evento,"QEvent.MouseButtonPress")
    #                     elif evento==3:
    #                         print(evento,"QEvent.MouseButtonRelease")
    #                     elif evento==5:
    #                         # print(evento,"QEvent.MouseMove") 
    #                         pass    
    #                     elif evento==6:
    #                         print(evento,"QEvent.KeyPress")   
    #                     elif evento==8:
    #                         print(evento,"QEvent.FocusIn")                        
    #                     elif evento==9:
    #                         print(evento,"QEvent.FocusOut")                        
    #                     elif evento==10:
    #                         # print(evento,"QEvent.Enter" ) 
    #                         pass     
    #                     elif evento==11:
    #                         # print(evento,"QEvent.Leave")
    #                         pass
    #                     elif evento==12:
    #                         pass
    #                         # print(evento,"QEvent.Paint")
    #                     elif evento==13:
    #                         print(evento,"QEvent.Move")
    #                     elif evento==14:
    #                         print(evento,"QEvent.Resize")
    #                     elif evento==17:
    #                         print(evento,"QEvent.Show")
    #                     elif evento==18:
    #                         print(evento,"QEvent.Hide")
    #                     elif evento==21:
    #                         print(evento,"QEvent.ParentChange")
    #                     elif evento==23:
    #                         print(evento,"QEvent.FocusAboutToChange")                        
    #                     elif evento==24:
    #                         # print(evento,"QEvent.WindowActivate")
    #                         pass
    #                     elif evento==25:
    #                         # print(evento,"QEvent.WindowDeactivate")
    #                         pass
    #                     elif evento==26:
    #                         print(evento,"QEvent.ShowToParent")
    #                     elif evento==43:
    #                         print(evento,"QEvent.MetaCall")
    #                     elif evento==51:
    #                         print(evento,"QEvent.ShortcutOverride")
    #                     elif evento==68:
    #                         print(evento,"QEvent.ChildAdded")
    #                     elif evento==71:
    #                         print(evento,"QEvent.ChildRemoved")
    #                     elif evento==74:
    #                         print(evento,"QEvent.PolishRequest")
    #                     elif evento==75:
    #                         print(evento,"QEvent.Polish")
    #                     elif evento==78:
    #                         print(evento,"QEvent.UpdateLater")
    #                     elif evento==110:
    #                         # print(evento,"QEvent.ToolTip")
    #                         pass
    #                     elif evento==183:
    #                         print(evento,"QEvent.CursorChange")
    #                     elif evento==207:
    #                         print(evento,"QEvent.InputMethodQuery")
    #                     #     print(evento,"QEvent.DynamicPropertiChange")                        
    #                     else:
    #                         print(evento,"???????")
    
    #                 """Eventos propios del mouse """
    #                 # if event.type() == QEvent.Move:
    #                 if event.type() == QEvent.MouseButtonPress:
    #                 # if event.type() == QEvent.MouseButtonDblClick:
    #                 # if event.type() == QEvent.MouseButtonRelease:
                        
    #                     if obj.rect().contains(event.pos()):   # si las coordenadas del mouse estan dentro del objeto
    #                         self.clicked.emit()
    #                         # The developer can opt for .emit(obj) to get the object within the slot.
    #                         return True

    #             return False   # Tanto si no es obj como si no esta dentro...

    #     # Creamos un filtro pasandole el objeto
    #     filter = Filter(widget)

    #     # Al objeto le instalamos el filtro
    #     widget.installEventFilter(filter)
    #     return filter.clicked



class QvColocacionCirculo(QgsMapTool):
    """ Dibuixa un cercle i selecciona els elements."""
    def __init__(self, canvas,   numeroSegmentsCercle, parent,lado):
        '''
        '''
        self.canvas = canvas
        self.parent= parent
        self.lado= lado
        
        QgsMapTool.__init__(self, self.canvas)
        self.clickable(self.canvas).connect(self.showText1)
        # clickable(self).connect(self.showText1)
        self.status = 0
        self.numeroSegmentsCercle = numeroSegmentsCercle

        self.rubberband=QgsRubberBand(self.canvas,True)
        self.rubberband.setColor( QColor("Blue") )
        self.rubberband.setWidth(1)
        self.rubberband.setIconSize(10)
        # self.overlap = False
        # self.radio  =0

    def clickable(self,widget):
        '''
        Gestiona 
        '''
        class Filter(QObject):
            """ Clase para filtrar
            Recibe un QObject """
        
            clicked = pyqtSignal()
            # def __init__(self,app):
            #     super().__init__()

            def eventFilter(self, obj, event):
                if obj == widget:
                    evento= event.type()
                    if "Busco a apartir del eventon su constante":
                        if evento== 2:
                            print(evento,"QEvent.MouseButtonPress")
                        elif evento==3:
                            print(evento,"QEvent.MouseButtonRelease")
                        elif evento==5:
                            # print(evento,"QEvent.MouseMove") 
                            pass    
                        elif evento==6:
                            print(evento,"QEvent.KeyPress")   
                        elif evento==8:
                            print(evento,"QEvent.FocusIn")                        
                        elif evento==9:
                            print(evento,"QEvent.FocusOut")  
                            # self.parent().saveAsImage("mapesOffline/temporal9.png")                      
                        elif evento==10:
                            # print(evento,"QEvent.Enter" ) 
                            pass     
                        elif evento==11:
                            # print(evento,"QEvent.Leave")
                            pass
                        elif evento==12:
                            pass
                            # print(evento,"QEvent.Paint")
                        elif evento==13:
                            print(evento,"QEvent.Move")
                        elif evento==14:
                            print(evento,"QEvent.Resize")
                        elif evento==17:
                            print(evento,"QEvent.Show")
                        elif evento==18:
                            print(evento,"QEvent.Hide")
                        elif evento==21:
                            print(evento,"QEvent.ParentChange")
                        elif evento==23:
                            print(evento,"QEvent.FocusAboutToChange")   
                            self.parent().saveAsImage("mapesOffline/temporal23.png")                     
                        elif evento==24:
                            # print(evento,"QEvent.WindowActivate")
                            pass
                        elif evento==25:
                            # print(evento,"QEvent.WindowDeactivate")
                            pass
                        elif evento==26:
                            print(evento,"QEvent.ShowToParent")
                        elif evento==43:
                            print(evento,"QEvent.MetaCall")
                        elif evento==51:
                            print(evento,"QEvent.ShortcutOverride")
                        elif evento==68:
                            print(evento,"QEvent.ChildAdded")
                        elif evento==71:
                            print(evento,"QEvent.ChildRemoved")
                        elif evento==74:
                            print(evento,"QEvent.PolishRequest")
                        elif evento==75:
                            print(evento,"QEvent.Polish")
                        elif evento==78:
                            print(evento,"QEvent.UpdateLater")
                        elif evento==110:
                            # print(evento,"QEvent.ToolTip")
                            pass
                        elif evento==183:
                            print(evento,"QEvent.CursorChange")
                        elif evento==207:
                            print(evento,"QEvent.InputMethodQuery")
                        #     print(evento,"QEvent.DynamicPropertiChange")                        
                        else:
                            print(evento,"???????")
    
                    """Eventos propios del mouse """
                    # if event.type() == QEvent.Move:
                    if event.type() == QEvent.MouseButtonPress:
                    # if event.type() == QEvent.MouseButtonDblClick:
                    # if event.type() == QEvent.MouseButtonRelease:
                        
                        if obj.rect().contains(event.pos()):   # si las coordenadas del mouse estan dentro del objeto
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False   # Tanto si no es obj como si no esta dentro...

        # Creamos un filtro pasandole el objeto
        filter = Filter(widget)

        # Al objeto le instalamos el filtro
        widget.installEventFilter(filter)
        return filter.clicked



    def canvasPressEvent(self,e):
        '''
        Data en canvas. Segun boton iz o derecho se que es modo win o no....
        Guardo el centro
        '''

        self.parent.label.setPixmap(QPixmap())
        try:
            self.rubberband.reset(True)
        except:
            pass  

        # self.canvas.saveAsImage("mapesOffline/temporal1.png")    
        self.canvas.refresh()
        self.status = 1   #Estamos pintando circulo!!
        # self.centre  centro del circulo
        self.centre = self.toMapCoordinates(e.pos())
        self.centroEnPantalla= e.pos()
        return
    def canvasMoveEvent(self,e):
        '''
          Hay que pintar dinamicamente el circulo
        '''        
        if self.status == 0:  # si no estoy en modo pintar circulo, no continuo
            return

        # guardo punto pantalla
        self.final=e.pos()
        # punto pantalla a mundo
        cp = self.toMapCoordinates(e.pos())

        # establezco color de rubberband
        self.rubberband.setColor(QColor("blue"))

        # dibujo el circulo
        self.rbcircle(self.rubberband, self.centre, cp, self.numeroSegmentsCercle)
        # r = math.sqrt(self.centre.sqrDist(cp))
    def rbcircle(self, rb,center,edgePoint,segments):
        '''
        Calculo circulo y lo cargo en rubberband
        '''
        rd = math.sqrt(center.sqrDist(edgePoint))
        self.radio = rd

        rb.reset(True )
        pi =3.1416
        llistaPunts=[]
        theta = 1*(2.0 * pi/segments)
        rb.addPoint(QgsPointXY(center.x()+1*math.cos(theta), center.y()+1*math.sin(theta)))
        for itheta in range(segments+1):
            theta = itheta*(2.0 * pi/segments)
            rb.addPoint(QgsPointXY(center.x()+rd*math.cos(theta),center.y()+rd*math.sin(theta)))
    def hacer1(self):
        if self.status == 0:
            return

        # Calculo datos para el recorte
        self.xcM= self.centre.x();             self.ycM= self.centre.y()           # Punto centro circulo Mundo
        self.xcP= self.centroEnPantalla.x();   self.ycP= self.centroEnPantalla.y() # Punto centro circulo Pantalla
        self.xrP= self.final.x();              self.yrP= self.final.y()            # Punto radio Pantalla
        self.rM= self.radio   

        # Calculo rango del circulo
        xmin= self.xcM - self.rM; ymin= self.ycM - self.rM
        xmax= self.xcM + self.rM; ymax= self.ycM + self.rM

        # Se lo paso al canvas para hacer zoom a esa zona
        self.rang = QgsRectangle(xmin, ymin, xmax, ymax)
        # self.canvas.setExtent(rang)
        print("extent")
        self.canvas.setExtent(self.rang)
        print("fin_extent")

        # def posaExtent():
        #     self.canvas.setExtent(rang)
        #     try:
        #         self.canvas.mapCanvasRefreshed.disconnect(posaExtent)
        #         print("si desconecto")
        #     except:
        #         print("no desconecto")
        

        # posaExtent()
        # self.canvas.mapCanvasRefreshed.connect(posaExtent)
        self.canvas.refresh()
        QTimer.singleShot(0, self.saveCanvas)
        pass
        

        
        # comprobacion
        # rect= self.canvas.extent()
        # self.canvas.setExtent(rect)
        # self.canvas.refresh()



        # El canvas a un pixmap....
        # He modificado la extension del canvas, pero guarda el canvas con la anterior extension!!!
        # No tengo el beneficio de aproximarme 
    def saveCanvas(self):
        print("saveAs")
        self.canvas.saveAsImage("mapesOffline/temporal.png") 
        print("finsaveAs")
        # self.pixmap=self.canvas.grab(QRect(QPoint(0,0),QSize(-1,-1)))
        self.hacer3()
    def saveCanvas1(self):
        print("saveAs")
        self.canvas.saveAsImage("mapesOffline/temporal.png") 
        print("finsaveAs")
        # self.pixmap=self.canvas.grab(QRect(QPoint(0,0),QSize(-1,-1)))
        self.hacer4()
    def hacer4(self):      
        self.pixmap = QPixmap("mapesOffline/temporal.png")  

        # self.pixmap=self.canvas.grab() # no acaba de ir bien, me carga en pixmap tambien el circulo pintado

        # tamaño del pixmap
        hp= self.pixmap.height()                                         # alto imagen 
        wp= self.pixmap.width()                                          # ancho imagen salvada
        # radio. 
        if hp < wp:
            self.rP= hp/2
        else:
            self.rP= wp/2

        self.xcP = wp/2
        self.ycP = hp/2
        # self.rP = math.sqrt(math.pow((self.xcP-self.xrP), 2) + math.pow((self.ycP-self.yrP), 2))  # radio pantalla
        pcX= self.xcP - self.rP ; pcY= self.ycP - self.rP                                    # punto inicio crop
        self.an= 2* self.rP;      self.al= self.an                            # an, ancho para crop   al, alto para crop
        escala= self.rP /self.rM                                                   # escala, como relacion de radiopantalla a radiomundo
        pmin= QPoint();   pmin.setX(pcX); pmin.setY(pcY+self.al);       self.Pmin = self.toMapCoordinates(pmin)
        pmax= QPoint();   pmax.setX(pcX+self.an); pmax.setY(pcY);       self.Pmax = self.toMapCoordinates(pmax)        

        # calculo area de recorte para hacer el crop 
        rect= QRect(pcX, pcY, self.an, self.al)
        # hago crop
        cropped_pixmap = self.pixmap.copy(rect) 
        
        # escalo el pixmap al tamaño que quiero
        self.scaled_pixmap = cropped_pixmap.scaled(self.parent.lado, self.parent.lado, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # de pixmap a image
        image=QImage(self.scaled_pixmap.toImage())
        image = image.convertToFormat(QImage.Format_ARGB32)

        # preparo imagen de salida transparente y del tamaño del de entrada....
        out_img = QImage(image.width(), image.width(), QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        # Create a texture brush and paint a circle with the original image onto
        # the output image: Chapeau!!
        brush = QBrush(image)        # Create texture brush
        painter = QPainter(out_img)  # Paint the output image
        painter.setBrush(brush)      # Use the image texture brush
        # painter.setPen(Qt.NoPen)     # Don't draw an outline
        pen= QPen(QColor(121,144,155),  1, Qt.SolidLine)    #qVista claro         
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
        painter.drawEllipse(0, 0, image.width(), image.width())  # Actually draw the circle
        painter.end()                # We are done (segfault if you forget this)

        # de out_img a pixmap
        self.scaled_pixmap = QPixmap.fromImage(out_img)

        # muestro ese pixmap en label...
        self.parent.label.setPixmap(self.scaled_pixmap)
        # self.parent.label1.setPixmap(cropped_pixmap)
        # self.parent.label2.setPixmap(self.pixmap)
        # self.parent.label3.setPixmap(self.scaled_pixmap)        

        #  muestro datos de georeferenciacion
        literal= "xmin,ymin=" + str(round(self.Pmin.x(),3)) +"  "+ str(round(self.Pmin.y(),3))
        self.parent.xmin_ymin.setText(literal)
        literal= "xmax,ymax=" + str(round(self.Pmax.x(),3)) +"  "+ str(round(self.Pmax.y(),3))
        self.parent.xmax_ymax.setText(literal)

 
        try:
            self.reset()
        except:
            pass       
    def hacer3(self):      
        self.pixmap = QPixmap("mapesOffline/temporal.png")  
   


        # self.pixmap=self.canvas.grab() # no acaba de ir bien, me carga en pixmap tambien el circulo pintado

        # tamaño del pixmap
        hp= self.pixmap.height()                                         # alto imagen 
        wp= self.pixmap.width()                                          # ancho imagen salvada
        
        self.rP = math.sqrt(math.pow((self.xcP-self.xrP), 2) + math.pow((self.ycP-self.yrP), 2))  # radio pantalla
        pcX= self.xcP - self.rP ; pcY= self.ycP - self.rP                                    # punto inicio crop
        self.an= 2* self.rP;      self.al= self.an                            # an, ancho para crop   al, alto para crop
        escala= self.rP /self.rM                                                   # escala, como relacion de radiopantalla a radiomundo
        pmin= QPoint();   pmin.setX(pcX); pmin.setY(pcY+self.al);       self.Pmin = self.toMapCoordinates(pmin)
        pmax= QPoint();   pmax.setX(pcX+self.an); pmax.setY(pcY);       self.Pmax = self.toMapCoordinates(pmax)        

        # calculo area de recorte para hacer el crop 
        rect= QRect(pcX, pcY, self.an, self.al)
        # hago crop
        cropped_pixmap = self.pixmap.copy(rect) 
        
        # escalo el pixmap al tamaño que quiero
        self.scaled_pixmap = cropped_pixmap.scaled(self.parent.lado, self.parent.lado, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # de pixmap a image
        image=QImage(self.scaled_pixmap.toImage())
        image = image.convertToFormat(QImage.Format_ARGB32)

        # preparo imagen de salida transparente y del tamaño del de entrada....
        out_img = QImage(image.width(), image.width(), QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        # Create a texture brush and paint a circle with the original image onto
        # the output image: Chapeau!!
        brush = QBrush(image)        # Create texture brush
        painter = QPainter(out_img)  # Paint the output image
        painter.setBrush(brush)      # Use the image texture brush
        # painter.setPen(Qt.NoPen)     # Don't draw an outline
        pen= QPen(QColor(121,144,155),  1, Qt.SolidLine)    #qVista claro         
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
        painter.drawEllipse(0, 0, image.width(), image.width())  # Actually draw the circle
        painter.end()                # We are done (segfault if you forget this)

        # de out_img a pixmap
        self.scaled_pixmap = QPixmap.fromImage(out_img)

        # muestro ese pixmap en label...
        # self.parent.label.setPixmap(self.scaled_pixmap)
       

        #  muestro datos de georeferenciacion
        literal= "xmin,ymin=" + str(round(self.Pmin.x(),3)) +"  "+ str(round(self.Pmin.y(),3))
        self.parent.xmin_ymin.setText(literal)
        literal= "xmax,ymax=" + str(round(self.Pmax.x(),3)) +"  "+ str(round(self.Pmax.y(),3))
        self.parent.xmax_ymax.setText(literal)

 
        try:
            self.reset()
        except:
            pass       
    def canvasReleaseEvent(self,e):
        '''
        Damos por dibujado el circulo al dejar de presionar el boton
        '''
        self.hacer1()
        #detectar señal de canvas refrescado y ejecutar saveCanvas
        # self.saveCanvas()  # salva
    def reset(self):
        '''
        '''
        self.status = 0
        self.rb.reset( True )
    def deactivate(self):
        '''
        '''
        pass
        # self.emit(SIGNAL("deactivated()"))
    def showText1(self):
        print ("Canvas clicked")
        # print ("Label 1 clicked")



class QvCrearMapetaConBotones(QWidget):
    '''
    Pongo botones para:\n
      Poner un circulo con ruberband\n
      Guardar la ruberband
    '''
    def __init__(self, canvas):
        '''
        '''
        self.canvas=canvas
        QWidget.__init__(self)
        self.existeCirculo=False        
        #defino botones y las funciones de su click
        self.botoponerCirculo = QvPushButton("Poner circulo")
        self.botoponerCirculo.clicked.connect(self.ponerCirculo)
        self.botoConfirmar = QvPushButton("Confirmar")
        self.botoConfirmar.clicked.connect(self.confirmar)



        self.botoSalvar =  QvPushButton('Salvar')  
        self.botoSalvar.clicked.connect(self.Salvar)
        self.label = QLabel(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)

        self.xmax_ymax = QLabel(" ",self)
        self.xmin_ymin = QLabel(" ",self)

        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(50, 600)
        self.spinBox.setSingleStep(20)
        self.spinBox.setValue(200)
        self.lado=self.spinBox.value()
        self.spinBox.valueChanged.connect(self.tamanyoLadoCirculo)

        self.layGcrearMapeta = QGridLayout(self)
        self.layGcrearMapeta.setSpacing(1)
        self.layGcrearMapeta.setVerticalSpacing(1)
        self.layGcrearMapeta.addWidget(self.botoponerCirculo,0,0,Qt.AlignTop)
        self.layGcrearMapeta.addWidget(self.botoConfirmar,0,1,Qt.AlignTop)
        self.layGcrearMapeta.addWidget(self.botoSalvar,1,0,Qt.AlignTop)
        self.layGcrearMapeta.addWidget(self.xmax_ymax,2,0,Qt.AlignTop)
        self.layGcrearMapeta.addWidget(self.xmin_ymin,3,0,Qt.AlignTop)
        self.layGcrearMapeta.addWidget(self.spinBox,4,0,Qt.AlignTop)
        self.layGcrearMapeta.addWidget(self.label,5,0,Qt.AlignBottom)
        self.layGcrearMapeta.addWidget(self.label1,6,0,Qt.AlignBottom)
        self.layGcrearMapeta.addWidget(self.label2,7,0,Qt.AlignBottom)
        self.layGcrearMapeta.addWidget(self.label3,8,0,Qt.AlignBottom)
    def tamanyoLadoCirculo(self):
        '''
        lado me gusta mas que spinB...value
        '''
        self.lado= self.spinBox.value() 
    def confirmar(self):
        self.colocoCirculo.saveCanvas1()
    def ponerCirculo(self):
        '''
        Dibujo circulo, dinamicamente
        '''
        self.label.setPixmap(QPixmap())
        numeroSegmentsCercle=360
        lado=self.lado
        if not self.existeCirculo:
            self.colocoCirculo= QvColocacionCirculo(self.canvas,  numeroSegmentsCercle,self,lado)
            self.existeCirculo=True
            self.canvas.setMapTool(self.colocoCirculo)
    def Salvar(self):
        '''
        Escribo PNG y PGW
        '''        
        dialegObertura=QFileDialog()
        dialegObertura.setDirectoryUrl(QUrl("mapesOffline/"))
        self.fileName,_ = dialegObertura.getSaveFileName(self, 'Guardar mapeta', '', 'PNG(*.png)')
        if self.fileName:
            # Guardo el pixmap como png
            self.colocoCirculo.scaled_pixmap.save(self.fileName)
            # Calculo info para el PQW
            # rango mundo x e y
            xdist = self.colocoCirculo.Pmax.x()- self.colocoCirculo.Pmin.x()   
            ydist = self.colocoCirculo.Pmax.y()- self.colocoCirculo.Pmin.y() 

            # ancho y alto de la imagen
            iheight = self.colocoCirculo.scaled_pixmap.height() 
            iwidth =  self.colocoCirculo.scaled_pixmap.width()  

            # Preparo nombre del PGW
            split_nombre=os.path.splitext(self.fileName)
            filenamePgw=split_nombre[0]+".pgw"

            # Escribo PGW
            wld =open(filenamePgw, "w")   
            wld.writelines("%s\n" % (xdist/iwidth))
            wld.writelines("0.0\n")
            wld.writelines("0.0\n")
            wld.writelines("%s\n" % (ydist/iheight))
            wld.writelines("%s\n" % self.colocoCirculo.Pmin.x())
            wld.writelines("%s\n" % self.colocoCirculo.Pmin.y())
            wld.close

            # region ejemplo de lectura de un PGW
            # wld =open(filenamePgw, "r")   
            # A=float(wld.readlines(1)[0])
            # D=float(wld.readlines(2)[0])
            # B=float(wld.readlines(3)[0])
            # E=float(wld.readlines(4)[0])
            # C=float(wld.readlines(5)[0])
            # F=float(wld.readlines(6)[0])
            # wld.close
            # x=iwidth
            # y=iheight


            # x1= A*x + B*y + C
            # y1 =D*x + E*y + F
            # print("xy=",C,",",F)
            # print("xy=",x1,",",y1)
            # pass
            # endregion     
            # 
            #        
    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


    def closeEvent(self,event):
        # Borrar "mapesOffline/temporal.png"
        if os.path.exists("mapesOffline/temporal.png"):
            os.remove("mapesOffline/temporal.png")
        else:
            print("The file does not exist")
            
        if os.path.exists("mapesOffline/temporal.pgw"):
            os.remove("mapesOffline/temporal.pgw")
        else:
            print("The file does not exist")            





# Demo d'ús quan es crida el fitxer de la classe per separat
if __name__ == "__main__":
    
    with qgisapp() as app:
        # Canvas, projecte i bridge
        canvas=QgsMapCanvas()
        project=QgsProject().instance()
        root=project.layerTreeRoot()
        bridge=QgsLayerTreeMapCanvasBridge(root,canvas)

        # llegim un projecte de demo
        project.read(projecteInicial)
        # windowTest = QMainWindow()
        windowTest = MyWindow()

        # Posem el canvas com a element central
        windowTest.setCentralWidget(canvas)

        # Instanciamos la classe QvcrearMapetaConBotones
        crearMapetaConBotones = QvCrearMapetaConBotones(canvas)
        crearMapetaConBotones.show()

        """
        Amb aquesta linia:
        crearMapeta.show()
        es veuria el widget suelto, separat del canvas.
        Les següents línies mostren com integrar el widget 'crearMapeta' com a dockWidget.
        """
        # Creem un dockWdget i definim les característiques
        dwcrearMapeta = QDockWidget( "CrearMapeta", windowTest )
        dwcrearMapeta.setContextMenuPolicy(Qt.PreventContextMenu)
        dwcrearMapeta.setAllowedAreas( Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea )
        dwcrearMapeta.setContentsMargins ( 1, 1, 1, 1 )
        
        # # # AÑADIMOS  nuestra instancia al dockwidget
        dwcrearMapeta.setWidget(crearMapetaConBotones)

        # # Coloquem el dockWidget al costat esquerra de la finestra
        windowTest.addDockWidget( Qt.LeftDockWidgetArea, dwcrearMapeta)

        # # Fem visible el dockWidget
        dwcrearMapeta.show()  #atencion

        # Fem visible la finestra principal
        canvas.show()
        windowTest.show()



        