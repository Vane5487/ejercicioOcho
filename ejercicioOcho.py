# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejercicioOcho.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(807, 603)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.Clientes = QtWidgets.QWidget()
        self.Clientes.setObjectName("Clientes")
        self.lineDNI = QtWidgets.QLineEdit(self.Clientes)
        self.lineDNI.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.lineDNI.setObjectName("lineDNI")
        self.lineNome = QtWidgets.QLineEdit(self.Clientes)
        self.lineNome.setGeometry(QtCore.QRect(450, 210, 251, 20))
        self.lineNome.setObjectName("lineNome")
        self.lblDNI = QtWidgets.QLabel(self.Clientes)
        self.lblDNI.setGeometry(QtCore.QRect(60, 150, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.lineApelidos_2 = QtWidgets.QLineEdit(self.Clientes)
        self.lineApelidos_2.setGeometry(QtCore.QRect(130, 270, 251, 21))
        self.lineApelidos_2.setObjectName("lineApelidos_2")
        self.lineCalendar = QtWidgets.QLineEdit(self.Clientes)
        self.lineCalendar.setGeometry(QtCore.QRect(360, 150, 151, 20))
        self.lineCalendar.setObjectName("lineCalendar")
        self.lblNome = QtWidgets.QLabel(self.Clientes)
        self.lblNome.setEnabled(True)
        self.lblNome.setGeometry(QtCore.QRect(400, 210, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.lineApelidos = QtWidgets.QLineEdit(self.Clientes)
        self.lineApelidos.setGeometry(QtCore.QRect(130, 210, 251, 21))
        self.lineApelidos.setObjectName("lineApelidos")
        self.line_2 = QtWidgets.QFrame(self.Clientes)
        self.line_2.setGeometry(QtCore.QRect(60, 80, 641, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.Clientes)
        self.label_2.setGeometry(QtCore.QRect(400, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Clientes)
        self.label.setGeometry(QtCore.QRect(60, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnSalir = QtWidgets.QPushButton(self.Clientes)
        self.btnSalir.setGeometry(QtCore.QRect(430, 430, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        self.lblApelido = QtWidgets.QLabel(self.Clientes)
        self.lblApelido.setGeometry(QtCore.QRect(60, 210, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblApelido.setFont(font)
        self.lblApelido.setObjectName("lblApelido")
        self.lblSexo = QtWidgets.QLabel(self.Clientes)
        self.lblSexo.setGeometry(QtCore.QRect(60, 330, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.btnCalendar = QtWidgets.QPushButton(self.Clientes)
        self.btnCalendar.setGeometry(QtCore.QRect(520, 150, 21, 21))
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setObjectName("btnCalendar")
        self.label_4 = QtWidgets.QLabel(self.Clientes)
        self.label_4.setGeometry(QtCore.QRect(320, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cmbProv = QtWidgets.QComboBox(self.Clientes)
        self.cmbProv.setGeometry(QtCore.QRect(470, 270, 231, 22))
        self.cmbProv.setObjectName("cmbProv")
        self.layoutWidget = QtWidgets.QWidget(self.Clientes)
        self.layoutWidget.setGeometry(QtCore.QRect(480, 330, 223, 19))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horlayPago = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horlayPago.setContentsMargins(0, 0, 0, 0)
        self.horlayPago.setObjectName("horlayPago")
        self.cbEfectivo = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbEfectivo.setObjectName("cbEfectivo")
        self.horlayPago.addWidget(self.cbEfectivo)
        self.cbTarjeta = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbTarjeta.setObjectName("cbTarjeta")
        self.horlayPago.addWidget(self.cbTarjeta)
        self.cbTransferencia = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbTransferencia.setObjectName("cbTransferencia")
        self.horlayPago.addWidget(self.cbTransferencia)
        self.line = QtWidgets.QFrame(self.Clientes)
        self.line.setGeometry(QtCore.QRect(60, 400, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnAceptar = QtWidgets.QPushButton(self.Clientes)
        self.btnAceptar.setGeometry(QtCore.QRect(270, 430, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblVal = QtWidgets.QLabel(self.Clientes)
        self.lblVal.setGeometry(QtCore.QRect(250, 150, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)
        self.lblVal.setFont(font)
        self.lblVal.setText("")
        self.lblVal.setObjectName("lblVal")
        self.lblCalendar = QtWidgets.QLabel(self.Clientes)
        self.lblCalendar.setGeometry(QtCore.QRect(280, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCalendar.setFont(font)
        self.lblCalendar.setObjectName("lblCalendar")
        self.lblPago = QtWidgets.QLabel(self.Clientes)
        self.lblPago.setGeometry(QtCore.QRect(360, 330, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setMouseTracking(False)
        self.lblPago.setTabletTracking(False)
        self.lblPago.setObjectName("lblPago")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Clientes)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 330, 146, 19))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horlaySex = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horlaySex.setContentsMargins(0, 0, 0, 0)
        self.horlaySex.setObjectName("horlaySex")
        self.rbtRemenino = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbtRemenino.setObjectName("rbtRemenino")
        self.horlaySex.addWidget(self.rbtRemenino)
        self.rbtMasculino = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbtMasculino.setObjectName("rbtMasculino")
        self.horlaySex.addWidget(self.rbtMasculino)
        self.tabWidget.addTab(self.Clientes, "")
        self.Facturacion = QtWidgets.QWidget()
        self.Facturacion.setObjectName("Facturacion")
        self.tabWidget.addTab(self.Facturacion, "")
        self.Productos = QtWidgets.QWidget()
        self.Productos.setObjectName("Productos")
        self.tabWidget.addTab(self.Productos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.lblNome.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Provincia:"))
        self.label.setText(_translate("MainWindow", "Direcci??n:"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblApelido.setText(_translate("MainWindow", "Apelidos:"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo:"))
        self.label_4.setText(_translate("MainWindow", "XESTION CLIENTES"))
        self.cbEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.cbTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.cbTransferencia.setText(_translate("MainWindow", "Transferencia"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.lblCalendar.setText(_translate("MainWindow", "Fecha Alta:"))
        self.lblPago.setText(_translate("MainWindow", "M??todos de Pago:"))
        self.rbtRemenino.setText(_translate("MainWindow", "Femenino"))
        self.rbtMasculino.setText(_translate("MainWindow", "Masculino"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Clientes), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Facturacion), _translate("MainWindow", "Facturaci??n"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Productos), _translate("MainWindow", "Productos"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+S"))
