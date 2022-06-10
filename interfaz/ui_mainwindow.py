# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowgdGZzJ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import resources_rc_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(556, 341)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/conocimiento.png", QSize(), QIcon.Normal, QIcon.Off)
        mainwindow.setWindowIcon(icon)
        mainwindow.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color:#1E343F;\n"
"	color:#ffffff;\n"
"	border-color:#000000;\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color:#046799;\n"
"	color:#FFFFFF;\n"
"	border-color:#000000;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"	background-color:#034263;\n"
"	color:#FFFFFF;\n"
"	border-color:#000000;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	background-color:#635303;\n"
"	color:#FFFFFF;\n"
"	border-color:#000000;\n"
"}\n"
"QMenu\n"
"{\n"
"	background-color:#046799;\n"
"	color:#FFFFFF;\n"
"	border-color:#000000;\n"
"}")
        self.actionINSERTAR = QAction(mainwindow)
        self.actionINSERTAR.setObjectName(u"actionINSERTAR")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/recursos/boton-agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionINSERTAR.setIcon(icon1)
        self.actionELIMINAR = QAction(mainwindow)
        self.actionELIMINAR.setObjectName(u"actionELIMINAR")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/recursos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionELIMINAR.setIcon(icon2)
        self.actionACTUALIZAR = QAction(mainwindow)
        self.actionACTUALIZAR.setObjectName(u"actionACTUALIZAR")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/recursos/boton-actualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionACTUALIZAR.setIcon(icon3)
        self.actionCONSULTAR = QAction(mainwindow)
        self.actionCONSULTAR.setObjectName(u"actionCONSULTAR")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/recursos/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCONSULTAR.setIcon(icon4)
        self.actionINSERTAR_2 = QAction(mainwindow)
        self.actionINSERTAR_2.setObjectName(u"actionINSERTAR_2")
        self.actionINSERTAR_2.setIcon(icon1)
        self.actionELIMINAR_2 = QAction(mainwindow)
        self.actionELIMINAR_2.setObjectName(u"actionELIMINAR_2")
        self.actionELIMINAR_2.setIcon(icon2)
        self.actionACTUALIZAR_2 = QAction(mainwindow)
        self.actionACTUALIZAR_2.setObjectName(u"actionACTUALIZAR_2")
        self.actionACTUALIZAR_2.setIcon(icon3)
        self.actionCONSULTAR_2 = QAction(mainwindow)
        self.actionCONSULTAR_2.setObjectName(u"actionCONSULTAR_2")
        self.actionCONSULTAR_2.setIcon(icon4)
        self.actionINSERTAR_3 = QAction(mainwindow)
        self.actionINSERTAR_3.setObjectName(u"actionINSERTAR_3")
        self.actionINSERTAR_3.setIcon(icon1)
        self.actionELIMINAR_3 = QAction(mainwindow)
        self.actionELIMINAR_3.setObjectName(u"actionELIMINAR_3")
        self.actionELIMINAR_3.setIcon(icon2)
        self.actionACTUALIZAR_3 = QAction(mainwindow)
        self.actionACTUALIZAR_3.setObjectName(u"actionACTUALIZAR_3")
        self.actionACTUALIZAR_3.setIcon(icon3)
        self.actionCONSULTAR_3 = QAction(mainwindow)
        self.actionCONSULTAR_3.setObjectName(u"actionCONSULTAR_3")
        self.actionCONSULTAR_3.setIcon(icon4)
        self.actionINSERTAR_4 = QAction(mainwindow)
        self.actionINSERTAR_4.setObjectName(u"actionINSERTAR_4")
        self.actionINSERTAR_4.setIcon(icon1)
        self.actionELIMINAR_4 = QAction(mainwindow)
        self.actionELIMINAR_4.setObjectName(u"actionELIMINAR_4")
        self.actionELIMINAR_4.setIcon(icon2)
        self.actionACTUALIZAR_4 = QAction(mainwindow)
        self.actionACTUALIZAR_4.setObjectName(u"actionACTUALIZAR_4")
        self.actionACTUALIZAR_4.setIcon(icon3)
        self.actionCONSULTAR_4 = QAction(mainwindow)
        self.actionCONSULTAR_4.setObjectName(u"actionCONSULTAR_4")
        self.actionCONSULTAR_4.setIcon(icon4)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 531, 201))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.actualizar_d = QPushButton(self.layoutWidget)
        self.actualizar_d.setObjectName(u"actualizar_d")
        self.actualizar_d.setIcon(icon3)

        self.gridLayout.addWidget(self.actualizar_d, 3, 2, 1, 1)

        self.eliminar_d = QPushButton(self.layoutWidget)
        self.eliminar_d.setObjectName(u"eliminar_d")
        self.eliminar_d.setIcon(icon2)

        self.gridLayout.addWidget(self.eliminar_d, 2, 2, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 13pt \"Unispace\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.insertar_a = QPushButton(self.layoutWidget)
        self.insertar_a.setObjectName(u"insertar_a")
        self.insertar_a.setIcon(icon1)

        self.gridLayout.addWidget(self.insertar_a, 1, 0, 1, 1)

        self.eliminar_a = QPushButton(self.layoutWidget)
        self.eliminar_a.setObjectName(u"eliminar_a")
        self.eliminar_a.setIcon(icon2)

        self.gridLayout.addWidget(self.eliminar_a, 2, 0, 1, 1)

        self.eliminar_t = QPushButton(self.layoutWidget)
        self.eliminar_t.setObjectName(u"eliminar_t")
        self.eliminar_t.setIcon(icon2)

        self.gridLayout.addWidget(self.eliminar_t, 2, 3, 1, 1)

        self.insertar_e = QPushButton(self.layoutWidget)
        self.insertar_e.setObjectName(u"insertar_e")
        self.insertar_e.setIcon(icon1)

        self.gridLayout.addWidget(self.insertar_e, 1, 1, 1, 1)

        self.consultar_d = QPushButton(self.layoutWidget)
        self.consultar_d.setObjectName(u"consultar_d")
        self.consultar_d.setIcon(icon4)

        self.gridLayout.addWidget(self.consultar_d, 4, 2, 1, 1)

        self.consultar_a = QPushButton(self.layoutWidget)
        self.consultar_a.setObjectName(u"consultar_a")
        self.consultar_a.setIcon(icon4)

        self.gridLayout.addWidget(self.consultar_a, 4, 0, 1, 1)

        self.eliminar_e = QPushButton(self.layoutWidget)
        self.eliminar_e.setObjectName(u"eliminar_e")
        self.eliminar_e.setIcon(icon2)

        self.gridLayout.addWidget(self.eliminar_e, 2, 1, 1, 1)

        self.actualizar_t = QPushButton(self.layoutWidget)
        self.actualizar_t.setObjectName(u"actualizar_t")
        self.actualizar_t.setIcon(icon3)

        self.gridLayout.addWidget(self.actualizar_t, 3, 3, 1, 1)

        self.consultar_t = QPushButton(self.layoutWidget)
        self.consultar_t.setObjectName(u"consultar_t")
        self.consultar_t.setIcon(icon4)

        self.gridLayout.addWidget(self.consultar_t, 4, 3, 1, 1)

        self.actualizar_e = QPushButton(self.layoutWidget)
        self.actualizar_e.setObjectName(u"actualizar_e")
        self.actualizar_e.setIcon(icon3)

        self.gridLayout.addWidget(self.actualizar_e, 3, 1, 1, 1)

        self.insertar_t = QPushButton(self.layoutWidget)
        self.insertar_t.setObjectName(u"insertar_t")
        self.insertar_t.setIcon(icon1)

        self.gridLayout.addWidget(self.insertar_t, 1, 3, 1, 1)

        self.insertar_d = QPushButton(self.layoutWidget)
        self.insertar_d.setObjectName(u"insertar_d")
        self.insertar_d.setIcon(icon1)

        self.gridLayout.addWidget(self.insertar_d, 1, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 13pt \"Unispace\";")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 13pt \"Unispace\";")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 13pt \"Unispace\";")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.actualizar_a = QPushButton(self.layoutWidget)
        self.actualizar_a.setObjectName(u"actualizar_a")
        self.actualizar_a.setIcon(icon3)

        self.gridLayout.addWidget(self.actualizar_a, 3, 0, 1, 1)

        self.consultar_e = QPushButton(self.layoutWidget)
        self.consultar_e.setObjectName(u"consultar_e")
        self.consultar_e.setIcon(icon4)

        self.gridLayout.addWidget(self.consultar_e, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 531, 41))
        self.label_5.setStyleSheet(u"font: 700 13pt \"Unispace\";")
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName(u"statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(mainwindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 556, 22))
        self.menuTABLAS = QMenu(self.menubar)
        self.menuTABLAS.setObjectName(u"menuTABLAS")
        self.menuALUMNO = QMenu(self.menuTABLAS)
        self.menuALUMNO.setObjectName(u"menuALUMNO")
        self.menuESCUELA = QMenu(self.menuTABLAS)
        self.menuESCUELA.setObjectName(u"menuESCUELA")
        self.menuTUTOR = QMenu(self.menuTABLAS)
        self.menuTUTOR.setObjectName(u"menuTUTOR")
        self.menuDIRECCI_N = QMenu(self.menuTABLAS)
        self.menuDIRECCI_N.setObjectName(u"menuDIRECCI_N")
        mainwindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuTABLAS.menuAction())
        self.menuTABLAS.addAction(self.menuALUMNO.menuAction())
        self.menuTABLAS.addAction(self.menuESCUELA.menuAction())
        self.menuTABLAS.addAction(self.menuTUTOR.menuAction())
        self.menuTABLAS.addAction(self.menuDIRECCI_N.menuAction())
        self.menuALUMNO.addAction(self.actionINSERTAR)
        self.menuALUMNO.addAction(self.actionELIMINAR)
        self.menuALUMNO.addAction(self.actionACTUALIZAR)
        self.menuALUMNO.addAction(self.actionCONSULTAR)
        self.menuESCUELA.addAction(self.actionINSERTAR_2)
        self.menuESCUELA.addAction(self.actionELIMINAR_2)
        self.menuESCUELA.addAction(self.actionACTUALIZAR_2)
        self.menuESCUELA.addAction(self.actionCONSULTAR_2)
        self.menuTUTOR.addAction(self.actionINSERTAR_3)
        self.menuTUTOR.addAction(self.actionELIMINAR_3)
        self.menuTUTOR.addAction(self.actionACTUALIZAR_3)
        self.menuTUTOR.addAction(self.actionCONSULTAR_3)
        self.menuDIRECCI_N.addAction(self.actionINSERTAR_4)
        self.menuDIRECCI_N.addAction(self.actionELIMINAR_4)
        self.menuDIRECCI_N.addAction(self.actionACTUALIZAR_4)
        self.menuDIRECCI_N.addAction(self.actionCONSULTAR_4)

        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"ESCUELAS MEDIA SUPERIOR", None))
        self.actionINSERTAR.setText(QCoreApplication.translate("mainwindow", u"INSERTAR", None))
        self.actionELIMINAR.setText(QCoreApplication.translate("mainwindow", u"ELIMINAR", None))
        self.actionACTUALIZAR.setText(QCoreApplication.translate("mainwindow", u"ACTUALIZAR", None))
        self.actionCONSULTAR.setText(QCoreApplication.translate("mainwindow", u"CONSULTAR", None))
        self.actionINSERTAR_2.setText(QCoreApplication.translate("mainwindow", u"INSERTAR", None))
        self.actionELIMINAR_2.setText(QCoreApplication.translate("mainwindow", u"ELIMINAR", None))
        self.actionACTUALIZAR_2.setText(QCoreApplication.translate("mainwindow", u"ACTUALIZAR", None))
        self.actionCONSULTAR_2.setText(QCoreApplication.translate("mainwindow", u"CONSULTAR", None))
        self.actionINSERTAR_3.setText(QCoreApplication.translate("mainwindow", u"INSERTAR", None))
        self.actionELIMINAR_3.setText(QCoreApplication.translate("mainwindow", u"ELIMINAR", None))
        self.actionACTUALIZAR_3.setText(QCoreApplication.translate("mainwindow", u"ACTUALIZAR", None))
        self.actionCONSULTAR_3.setText(QCoreApplication.translate("mainwindow", u"CONSULTAR", None))
        self.actionINSERTAR_4.setText(QCoreApplication.translate("mainwindow", u"INSERTAR", None))
        self.actionELIMINAR_4.setText(QCoreApplication.translate("mainwindow", u"ELIMINAR", None))
        self.actionACTUALIZAR_4.setText(QCoreApplication.translate("mainwindow", u"ACTUALIZAR", None))
        self.actionCONSULTAR_4.setText(QCoreApplication.translate("mainwindow", u"CONSULTAR", None))
        self.actualizar_d.setText(QCoreApplication.translate("mainwindow", u"Actualizar", None))
        self.eliminar_d.setText(QCoreApplication.translate("mainwindow", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p align=\"center\">ALUMNO</p></body></html>", None))
        self.insertar_a.setText(QCoreApplication.translate("mainwindow", u"Insertar", None))
        self.eliminar_a.setText(QCoreApplication.translate("mainwindow", u"Eliminar", None))
        self.eliminar_t.setText(QCoreApplication.translate("mainwindow", u"Eliminar", None))
        self.insertar_e.setText(QCoreApplication.translate("mainwindow", u"Insertar", None))
        self.consultar_d.setText(QCoreApplication.translate("mainwindow", u"Consultar", None))
        self.consultar_a.setText(QCoreApplication.translate("mainwindow", u"Consultar", None))
        self.eliminar_e.setText(QCoreApplication.translate("mainwindow", u"Eliminar", None))
        self.actualizar_t.setText(QCoreApplication.translate("mainwindow", u"Actualizar", None))
        self.consultar_t.setText(QCoreApplication.translate("mainwindow", u"Consultar", None))
        self.actualizar_e.setText(QCoreApplication.translate("mainwindow", u"Actualizar", None))
        self.insertar_t.setText(QCoreApplication.translate("mainwindow", u"Insertar", None))
        self.insertar_d.setText(QCoreApplication.translate("mainwindow", u"Insertar", None))
        self.label_2.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p align=\"center\">ESCUELA</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p align=\"center\">TUTOR</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p align=\"center\">DIRECCI\u00d3N</p></body></html>", None))
        self.actualizar_a.setText(QCoreApplication.translate("mainwindow", u"Actualizar", None))
        self.consultar_e.setText(QCoreApplication.translate("mainwindow", u"Consultar", None))
        self.label_5.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p align=\"center\">ESCUELAS MEDIA SUPERIOR</p></body></html>", None))
        self.menuTABLAS.setTitle(QCoreApplication.translate("mainwindow", u"TABLAS", None))
        self.menuALUMNO.setTitle(QCoreApplication.translate("mainwindow", u"ALUMNO", None))
        self.menuESCUELA.setTitle(QCoreApplication.translate("mainwindow", u"ESCUELA", None))
        self.menuTUTOR.setTitle(QCoreApplication.translate("mainwindow", u"TUTOR", None))
        self.menuDIRECCI_N.setTitle(QCoreApplication.translate("mainwindow", u"DIRECCI\u00d3N", None))
    # retranslateUi

