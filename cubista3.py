# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CuBista3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_11.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_11.setStyleSheet("background-color:#465A63;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setLineWidth(0)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setLineWidth(0)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setStyleSheet("background-color: #79909B;\n"
"color: #FFFFFF")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setLineWidth(0)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setContentsMargins(10, 1, 1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leTitolProjecte = QtWidgets.QLineEdit(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.leTitolProjecte.setFont(font)
        self.leTitolProjecte.setStyleSheet("background-color: #F9F9F9 transparent;\n"
"    color: #38474F;\n"
"    margin: 0px;\n"
"    border: 0px;")
        self.leTitolProjecte.setObjectName("leTitolProjecte")
        self.horizontalLayout_4.addWidget(self.leTitolProjecte)
        self.lblTitolProjecte = QtWidgets.QPushButton(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitolProjecte.sizePolicy().hasHeightForWidth())
        self.lblTitolProjecte.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lblTitolProjecte.setFont(font)
        self.lblTitolProjecte.setStyleSheet("background-color: #F9F9F9 transparent;\n"
"color: white;\n"
"margin: 0px;\n"
"border: 0px;\n"
"text-align: left;")
        self.lblTitolProjecte.setObjectName("lblTitolProjecte")
        self.horizontalLayout_4.addWidget(self.lblTitolProjecte)
        self.botoMetadades = QtWidgets.QPushButton(self.frame_15)
        self.botoMetadades.setText("")
        self.botoMetadades.setObjectName("botoMetadades")
        self.horizontalLayout_4.addWidget(self.botoMetadades)
        self.botoVeureLlegenda = QtWidgets.QPushButton(self.frame_15)
        self.botoVeureLlegenda.setMinimumSize(QtCore.QSize(24, 24))
        self.botoVeureLlegenda.setStyleSheet("")
        self.botoVeureLlegenda.setText("")
        self.botoVeureLlegenda.setObjectName("botoVeureLlegenda")
        self.horizontalLayout_4.addWidget(self.botoVeureLlegenda)
        self.botoMapeta = QtWidgets.QPushButton(self.frame_15)
        self.botoMapeta.setText("")
        self.botoMapeta.setObjectName("botoMapeta")
        self.horizontalLayout_4.addWidget(self.botoMapeta)
        self.botoObrirQGis = QtWidgets.QPushButton(self.frame_15)
        self.botoObrirQGis.setMinimumSize(QtCore.QSize(24, 24))
        self.botoObrirQGis.setStyleSheet("")
        self.botoObrirQGis.setText("")
        self.botoObrirQGis.setObjectName("botoObrirQGis")
        self.horizontalLayout_4.addWidget(self.botoObrirQGis, 0, QtCore.Qt.AlignRight)
        self.botoDesarProjecte = QtWidgets.QPushButton(self.frame_15)
        self.botoDesarProjecte.setMinimumSize(QtCore.QSize(24, 0))
        self.botoDesarProjecte.setStyleSheet("")
        self.botoDesarProjecte.setText("")
        self.botoDesarProjecte.setObjectName("botoDesarProjecte")
        self.horizontalLayout_4.addWidget(self.botoDesarProjecte)
        self.botoFavorits = QtWidgets.QPushButton(self.frame_15)
        self.botoFavorits.setText("")
        self.botoFavorits.setObjectName("botoFavorits")
        self.horizontalLayout_4.addWidget(self.botoFavorits)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.horizontalLayout.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        self.frame_13.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_13.setStyleSheet("background-color: #465A63;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setLineWidth(0)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout.addWidget(self.frame_13)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_16 = QtWidgets.QFrame(self.frame_9)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setLineWidth(0)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameLlegenda = QtWidgets.QFrame(self.frame_16)
        self.frameLlegenda.setMinimumSize(QtCore.QSize(250, 0))
        self.frameLlegenda.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frameLlegenda.setStyleSheet("background-color: #DDDDDD")
        self.frameLlegenda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameLlegenda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLlegenda.setLineWidth(0)
        self.frameLlegenda.setObjectName("frameLlegenda")
        self.horizontalLayout_2.addWidget(self.frameLlegenda)
        self.frameCentral = QtWidgets.QFrame(self.frame_16)
        self.frameCentral.setStyleSheet("")
        self.frameCentral.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameCentral.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameCentral.setLineWidth(0)
        self.frameCentral.setObjectName("frameCentral")
        self.horizontalLayout_2.addWidget(self.frameCentral)
        self.frame_19 = QtWidgets.QFrame(self.frame_16)
        self.frame_19.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_19.setStyleSheet("background-color: #DDDDDD\n"
"")
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setLineWidth(0)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lytBotoneraLateral = QtWidgets.QVBoxLayout()
        self.lytBotoneraLateral.setContentsMargins(8, 8, 8, 8)
        self.lytBotoneraLateral.setSpacing(10)
        self.lytBotoneraLateral.setObjectName("lytBotoneraLateral")
        self.gridLayout.addLayout(self.lytBotoneraLateral, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_19)
        self.frameCentral.raise_()
        self.frameLlegenda.raise_()
        self.frame_19.raise_()
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_2 = QtWidgets.QFrame(self.frame_9)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 2))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frame_2.setStyleSheet("background-color: #DDDDDD")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 34))
        self.menubar.setMinimumSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 106, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 88, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 35, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 47, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 35, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 106, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 88, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 35, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 47, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 35, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 106, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 88, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 35, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 47, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 71, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.menubar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(56, 71, 79);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitolProjecte.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#38474f;\">Feu clic per canviar el títol del projecte</span></p></body></html>"))
        self.lblTitolProjecte.setText(_translate("MainWindow", "Qualificacions urbanístiques i suspensions"))
        self.botoVeureLlegenda.setToolTip(_translate("MainWindow", "<html><head/><body><p>Veure i ocultar llegenda</p></body></html>"))
        self.botoMapeta.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mostrar i ocultar mapeta</p></body></html>"))
        self.botoObrirQGis.setToolTip(_translate("MainWindow", "<html><head/><body><p>Obrir projecte en QGis</p></body></html>"))
        self.botoDesarProjecte.setToolTip(_translate("MainWindow", "<html><head/><body><p>Desar projecte</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

