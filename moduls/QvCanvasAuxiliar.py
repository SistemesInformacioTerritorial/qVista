from moduls.QvImports import *
from moduls.QvCanvas import QvCanvas
from moduls.QvConstants import QvConstants

class QvCanvasAuxiliar(QvCanvas):
    def __init__(self, canvas, *args, temaInicial = None, sincronitzaExtensio=False, sincronitzaZoom=False, sincronitzaCentre=False, volemCombo=True, **kwargs):
        """Canvas auxiliar, pensat per afegir funcionalitats al QvCanvas.

        Permet rebre tots els arguments que rebi QvCanvas, més uns quants extra

        Args:
            canvas (QgsMapCanvas): Canvas principal
            temaInicial (str, optional): Nom del tema inicial, si n'hi ha. Defaults to None
            sincronitzaExtensio (bool, optional): [description]. Defaults to False.
            sincronitzaZoom (bool, optional): [description]. Defaults to False.
            sincronitzaCentre (bool, optional): [description]. Defaults to False.
            volemCombo (bool, optional): Indica si volem que hi hagi una combobox per canviar de tema. Defaults to True
        """
        super().__init__(*args, **kwargs)
        self.canvas = canvas
        self.sincronitzaExtensio = sincronitzaExtensio
        self.sincronitzaZoom = sincronitzaZoom
        self.sincronitzaCentre = sincronitzaCentre
        self.botons()
        if volemCombo:
            self.preparaCbTemes(temaInicial)
        self.setupSincronia()
    
    def preparaCbTemes(self, temaInicial):
        self.temes = QgsProject.instance().mapThemeCollection().mapThemes()
        if len(self.temes)>0:
            self.cbTemes = QComboBox()
            self.cbTemes.addItem('Tema per defecte')
            self.cbTemes.addItems(self.temes)
            self.cbTemes.currentIndexChanged.connect(self.canviTema)
            self.layoutBotoneraMapa.insertWidget(0,self.cbTemes)

            if temaInicial in self.temes:
                self.cbTemes.setCurrentIndex(self.temes.index(temaInicial)+1)
    
    def botons(self):
        self.bSincronia = self._botoMapa(os.path.join(imatgesDir,'sync.png'))
        self.bSincronia.setToolTip('Pantalla completa (F11)')
        self.layoutBotoneraMapa.insertWidget(0,self.bSincronia)
        self.bSincronia.setCursor(QvConstants.cursorFletxa()) 
        self.bSincronia.setCheckable(False)

        # Definició del menú desplegable
        menuBoto = QMenu(':D')
        grup = QActionGroup(menuBoto)
        self.actSincExt = menuBoto.addAction('Sincronitza extensió')
        self.actSincZoom = menuBoto.addAction('Sincronitza zoom')
        self.actSincCentre = menuBoto.addAction('Sincronitza centre')

        grup.addAction(self.actSincExt)
        grup.addAction(self.actSincZoom)
        grup.addAction(self.actSincCentre)

        self.actSincExt.setCheckable(True)
        self.actSincExt.setChecked(False)
        self.actSincZoom.setCheckable(True)
        self.actSincZoom.setChecked(False)
        self.actSincCentre.setCheckable(True)
        self.actSincCentre.setChecked(False)

        self.actSincExt.triggered.connect(self.swapSincronies)
        self.actSincZoom.triggered.connect(self.swapSincronies)
        self.actSincCentre.triggered.connect(self.swapSincronies)

        self.bSincronia.setMenu(menuBoto)

    def canviTema(self, i):
        if i==0:
            self.setTheme('')
        else:
            self.setTheme(self.temes[i-1])
            
    def sincronitzaExtensio(self, canv: QgsMapCanvas):
        """Sincronitza els paràmetre implícit amb el canvas passat com a paràmetre

        Args:
            canv (QgsMapCanvas): [description]
        """
        def sync():
            canv.setExtent(self.extent())
            canv.refresh()
        canv.extentsChanged.connect(sync)
    
    def setupSincronia(self):
        self.canvas.extentsChanged.connect(self.syncExtensio)
        self.canvas.scaleChanged.connect(self.syncZoom)
        self.canvas.extentsChanged.connect(self.syncCentre)

        self.extentsChanged.connect(self.syncExtensioOut)
        self.scaleChanged.connect(self.syncZoomOut)
        self.extentsChanged.connect(self.syncCentreOut)
    
    def syncExtensio(self):
        if self.sincronitzaExtensio and not self.hasFocus():
            self.setExtent(self.canvas.extent())
            self.refresh()
    def syncZoom(self):
        if self.sincronitzaZoom and not self.hasFocus():
            centre = self.center()
            self.setExtent(self.canvas.extent())
            self.setCenter(centre)
            self.refresh()
    def syncCentre(self):
        if self.sincronitzaCentre and not self.hasFocus():
            self.setCenter(self.canvas.center())
            self.refresh()
    
    def syncExtensioOut(self):
        if self.sincronitzaExtensio and self.hasFocus():
            self.canvas.setExtent(self.extent())
            self.canvas.refresh()
    def syncZoomOut(self):
        if self.sincronitzaZoom and self.hasFocus():
            centre = self.canvas.center()
            self.canvas.setExtent(self.extent())
            self.canvas.setCenter(centre)
            self.canvas.refresh()
    def syncCentreOut(self):
        if self.sincronitzaCentre and self.hasFocus():
            self.canvas.setCenter(self.center())
            self.canvas.refresh()

    def swapSincronies(self):
        self.swapSincroniaExtensio(self.actSincExt.isChecked())
        self.swapSincroniaZoom(self.actSincZoom.isChecked())
        self.swapSincroniaCentre(self.actSincCentre.isChecked())
    
    def swapSincroniaExtensio(self,check):
        self.sincronitzaExtensio = check
    
    def swapSincroniaZoom(self,check):
        self.sincronitzaZoom = check
    
    def swapSincroniaCentre(self,check):
        self.sincronitzaCentre = check