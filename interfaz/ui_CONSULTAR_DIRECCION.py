# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CONSULTAR_DIRECCIONLUegqd.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc_rc

class Ui_Form_CONSULTAR_DIRECCION(object):
    def setupUi(self, Form_CONSULTAR_DIRECCION):
        if not Form_CONSULTAR_DIRECCION.objectName():
            Form_CONSULTAR_DIRECCION.setObjectName(u"Form_CONSULTAR_DIRECCION")
        Form_CONSULTAR_DIRECCION.resize(912, 343)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_CONSULTAR_DIRECCION.setWindowIcon(icon)
        Form_CONSULTAR_DIRECCION.setStyleSheet(u"QWidget\n"
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
"QGroupBox\n"
"{\n"
"	background-color:#1E343F;\n"
"	color:#ffffff;\n"
"	border-color:#000000;\n"
"}")
        self.consultar = QPushButton(Form_CONSULTAR_DIRECCION)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(770, 268, 131, 31))
        self.consultar.setIcon(icon)
        self.consultar.setIconSize(QSize(20, 20))
        self.groupBox = QGroupBox(Form_CONSULTAR_DIRECCION)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 128, 891, 121))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tabla = QTableWidget(self.groupBox)
        if (self.tabla.columnCount() < 8):
            self.tabla.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(0, 0, 891, 121))
        self.tabla.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tabla.horizontalHeader().setDefaultSectionSize(155)
        self.label = QLabel(Form_CONSULTAR_DIRECCION)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 40, 360, 18))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.curp = QLineEdit(Form_CONSULTAR_DIRECCION)
        self.curp.setObjectName(u"curp")
        self.curp.setGeometry(QRect(70, 64, 361, 31))
        self.ID = QLineEdit(Form_CONSULTAR_DIRECCION)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(490, 64, 331, 31))
        self.label_2 = QLabel(Form_CONSULTAR_DIRECCION)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 100, 333, 18))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form_CONSULTAR_DIRECCION)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 40, 206, 18))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form_CONSULTAR_DIRECCION)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 10, 191, 21))
        self.label_4.setFont(font)

        self.retranslateUi(Form_CONSULTAR_DIRECCION)

        QMetaObject.connectSlotsByName(Form_CONSULTAR_DIRECCION)
    # setupUi

    def retranslateUi(self, Form_CONSULTAR_DIRECCION):
        Form_CONSULTAR_DIRECCION.setWindowTitle(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"CONSULTAR DIRECCION", None))
        self.consultar.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"CONSULTAR", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"ID", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"COLONIA", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"CODIGO POSTAL", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"CALLE", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"NO.EXTERIOR", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"NO.INTERIOR", None));
        ___qtablewidgetitem6 = self.tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"ESTADO", None));
        ___qtablewidgetitem7 = self.tabla.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"ALCALDIA", None));
        self.label.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"INGRESA EL CURP DEL ALUMNO PARA VER LA DIRECCION:", None))
        self.label_2.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"<html><head/><body><p><span style=\" font-weight:400; text-decoration: underline;\">SI CONOCE EL ID DE LA DIRECCION USE ESTA OPCION</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"INGRESE EL ID DE LA DIRECCION:", None))
        self.label_4.setText(QCoreApplication.translate("Form_CONSULTAR_DIRECCION", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">CONSULTAR DIRECCI\u00d3N</span></p></body></html>", None))
    # retranslateUi

