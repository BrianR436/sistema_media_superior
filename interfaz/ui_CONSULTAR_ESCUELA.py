# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CONSULTAR_ESCUELAakNjMK.ui'
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

class Ui_Form_CONSULTAR_ESCUELA(object):
    def setupUi(self, Form_CONSULTAR_ESCUELA):
        if not Form_CONSULTAR_ESCUELA.objectName():
            Form_CONSULTAR_ESCUELA.setObjectName(u"Form_CONSULTAR_ESCUELA")
        Form_CONSULTAR_ESCUELA.resize(912, 503)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_CONSULTAR_ESCUELA.setWindowIcon(icon)
        Form_CONSULTAR_ESCUELA.setStyleSheet(u"QWidget\n"
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
        self.consultar = QPushButton(Form_CONSULTAR_ESCUELA)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(770, 460, 131, 31))
        self.consultar.setIcon(icon)
        self.consultar.setIconSize(QSize(20, 20))
        self.label_16 = QLabel(Form_CONSULTAR_ESCUELA)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 70, 141, 31))
        self.groupBox = QGroupBox(Form_CONSULTAR_ESCUELA)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 110, 891, 131))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 891, 131))
        self.tableWidget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.label_17 = QLabel(Form_CONSULTAR_ESCUELA)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(400, 270, 91, 31))
        self.groupBox_2 = QGroupBox(Form_CONSULTAR_ESCUELA)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 310, 891, 141))
        self.groupBox_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.direccion = QTableWidget(self.groupBox_2)
        if (self.direccion.columnCount() < 7):
            self.direccion.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.direccion.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.direccion.setObjectName(u"direccion")
        self.direccion.setGeometry(QRect(0, 0, 891, 141))
        self.direccion.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.direccion.horizontalHeader().setDefaultSectionSize(155)
        self.label = QLabel(Form_CONSULTAR_ESCUELA)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 131, 16))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.CCT = QLineEdit(Form_CONSULTAR_ESCUELA)
        self.CCT.setObjectName(u"CCT")
        self.CCT.setGeometry(QRect(10, 71, 133, 31))
        self.label_18 = QLabel(Form_CONSULTAR_ESCUELA)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(340, 0, 201, 31))

        self.retranslateUi(Form_CONSULTAR_ESCUELA)

        QMetaObject.connectSlotsByName(Form_CONSULTAR_ESCUELA)
    # setupUi

    def retranslateUi(self, Form_CONSULTAR_ESCUELA):
        Form_CONSULTAR_ESCUELA.setWindowTitle(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"CONSULTAR ESCUELA", None))
        self.consultar.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"CONSULTAR", None))
        self.label_16.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Datos generales</span></p></body></html>", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"CCT", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"INSTITUCI\u00d3N", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"PLANTEL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"TELEFONO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"WEB", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"CORREO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"DOMINIO", None));
        self.label_17.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Direcci\u00f3n</span></p></body></html>", None))
        self.groupBox_2.setTitle("")
        ___qtablewidgetitem7 = self.direccion.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"COLONIA", None));
        ___qtablewidgetitem8 = self.direccion.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"CODIGO POSTAL", None));
        ___qtablewidgetitem9 = self.direccion.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"CALLE", None));
        ___qtablewidgetitem10 = self.direccion.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"NO. INTERIOR", None));
        ___qtablewidgetitem11 = self.direccion.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"NO. EXTERIOR", None));
        ___qtablewidgetitem12 = self.direccion.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"ALCALDIA", None));
        ___qtablewidgetitem13 = self.direccion.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"ESTADO", None));
        self.label.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"INGRESE EL CCT:", None))
        self.CCT.setText("")
        self.label_18.setText(QCoreApplication.translate("Form_CONSULTAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">CONSULTAR ESCUELA</span></p></body></html>", None))
    # retranslateUi

