# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ACTUALIZAR_ESCUELAYeiWFa.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
import resources_rc_rc

class Ui_Form_ACTUALIZAR_ESCUELA(object):
    def setupUi(self, Form_ACTUALIZAR_ESCUELA):
        if not Form_ACTUALIZAR_ESCUELA.objectName():
            Form_ACTUALIZAR_ESCUELA.setObjectName(u"Form_ACTUALIZAR_ESCUELA")
        Form_ACTUALIZAR_ESCUELA.resize(911, 713)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-actualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ACTUALIZAR_ESCUELA.setWindowIcon(icon)
        Form_ACTUALIZAR_ESCUELA.setStyleSheet(u"QWidget\n"
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
"}\n"
"")
        self.actualizar = QPushButton(Form_ACTUALIZAR_ESCUELA)
        self.actualizar.setObjectName(u"actualizar")
        self.actualizar.setGeometry(QRect(770, 650, 131, 31))
        self.actualizar.setIcon(icon)
        self.actualizar.setIconSize(QSize(20, 20))
        self.label_16 = QLabel(Form_ACTUALIZAR_ESCUELA)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 30, 141, 31))
        self.label_19 = QLabel(Form_ACTUALIZAR_ESCUELA)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(390, 250, 91, 31))
        self.layoutWidget = QWidget(Form_ACTUALIZAR_ESCUELA)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 868, 171))
        self.gridLayout_7 = QGridLayout(self.layoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.telefono = QLineEdit(self.layoutWidget)
        self.telefono.setObjectName(u"telefono")

        self.gridLayout.addWidget(self.telefono, 1, 2, 1, 1)

        self.CCT = QLineEdit(self.layoutWidget)
        self.CCT.setObjectName(u"CCT")

        self.gridLayout.addWidget(self.CCT, 1, 0, 1, 1)

        self.plantel = QLineEdit(self.layoutWidget)
        self.plantel.setObjectName(u"plantel")

        self.gridLayout.addWidget(self.plantel, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setBold(True)
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.web = QLineEdit(self.layoutWidget)
        self.web.setObjectName(u"web")

        self.gridLayout_2.addWidget(self.web, 2, 0, 1, 1)

        self.correo = QLineEdit(self.layoutWidget)
        self.correo.setObjectName(u"correo")

        self.gridLayout_2.addWidget(self.correo, 2, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)

        self.dominio = QComboBox(self.layoutWidget)
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.addItem("")
        self.dominio.setObjectName(u"dominio")

        self.gridLayout_2.addWidget(self.dominio, 2, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.institucion = QComboBox(self.layoutWidget)
        self.institucion.addItem("")
        self.institucion.addItem("")
        self.institucion.addItem("")
        self.institucion.addItem("")
        self.institucion.setObjectName(u"institucion")

        self.gridLayout_3.addWidget(self.institucion, 1, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.layoutWidget1 = QWidget(Form_ACTUALIZAR_ESCUELA)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 280, 871, 111))
        self.gridLayout_8 = QGridLayout(self.layoutWidget1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.gridLayout_8.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_8.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_8.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1)

        self.calle = QLineEdit(self.layoutWidget1)
        self.calle.setObjectName(u"calle")

        self.gridLayout_8.addWidget(self.calle, 1, 2, 1, 1)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_8.addWidget(self.label_23, 0, 3, 1, 1)

        self.CP = QLineEdit(self.layoutWidget1)
        self.CP.setObjectName(u"CP")

        self.gridLayout_8.addWidget(self.CP, 1, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)

        self.interior = QLineEdit(self.layoutWidget1)
        self.interior.setObjectName(u"interior")

        self.gridLayout_8.addWidget(self.interior, 1, 4, 1, 1)

        self.colonia = QLineEdit(self.layoutWidget1)
        self.colonia.setObjectName(u"colonia")

        self.gridLayout_8.addWidget(self.colonia, 1, 0, 1, 1)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_8.addWidget(self.label_26, 2, 1, 1, 1)

        self.exterior = QLineEdit(self.layoutWidget1)
        self.exterior.setObjectName(u"exterior")

        self.gridLayout_8.addWidget(self.exterior, 1, 3, 1, 1)

        self.alcaldia = QLineEdit(self.layoutWidget1)
        self.alcaldia.setObjectName(u"alcaldia")

        self.gridLayout_8.addWidget(self.alcaldia, 3, 0, 1, 1)

        self.estado = QComboBox(self.layoutWidget1)
        self.estado.addItem("")
        self.estado.addItem("")
        self.estado.setObjectName(u"estado")

        self.gridLayout_8.addWidget(self.estado, 3, 1, 1, 1)

        self.groupBox = QGroupBox(Form_ACTUALIZAR_ESCUELA)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 410, 891, 231))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 14):
            self.tableWidget.setColumnCount(14)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 891, 231))
        self.tableWidget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.label_17 = QLabel(Form_ACTUALIZAR_ESCUELA)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(340, 0, 201, 31))

        self.retranslateUi(Form_ACTUALIZAR_ESCUELA)

        QMetaObject.connectSlotsByName(Form_ACTUALIZAR_ESCUELA)
    # setupUi

    def retranslateUi(self, Form_ACTUALIZAR_ESCUELA):
        Form_ACTUALIZAR_ESCUELA.setWindowTitle(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u" ACTUALIZAR ESCUELA", None))
        self.actualizar.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"ACTUALIZAR", None))
        self.label_16.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Datos generales</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Direcci\u00f3n</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"INGRESE EL CCT DE LA ESCUELA A ACTUALIZAR", None))
        self.telefono.setText("")
        self.CCT.setText("")
        self.plantel.setText("")
        self.label_2.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"PLANTEL", None))
        self.label_3.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"TELEFONO", None))
        self.label_7.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"DOMINIO                                                                            ", None))
        self.label_5.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"SITIO WEB", None))
        self.web.setText("")
        self.correo.setText("")
        self.label_6.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CORREO", None))
        self.dominio.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@conalepmex.edu.mx", None))
        self.dominio.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@bachilleres.edu.mx", None))
        self.dominio.setItemText(2, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@gmail.com", None))
        self.dominio.setItemText(3, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@hotmail.com", None))
        self.dominio.setItemText(4, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@comunidad.unam.mx ", None))
        self.dominio.setItemText(5, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@bachilleres.edu.mx", None))
        self.dominio.setItemText(6, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@outlook.com", None))
        self.dominio.setItemText(7, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@live.com", None))
        self.dominio.setItemText(8, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@IPN.MX", None))
        self.dominio.setItemText(9, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"@enp.unam.mx", None))

        self.institucion.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"INSTITUTO POLIT\u00c9CNICO NACIONAL", None))
        self.institucion.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"UNIVERSIDAD NACIONAL AUT\u00d3NOMA DE M\u00c9XICO", None))
        self.institucion.setItemText(2, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"COLEGIO DE BACHILLERES", None))
        self.institucion.setItemText(3, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CONALEP", None))

        self.label_8.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"INSTITUCI\u00d3N", None))
        self.label_21.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"Codigo Postal", None))
        self.label_25.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"Alcadia o Municipio", None))
        self.label_24.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"No. Interior", None))
        self.label_22.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"Calle", None))
        self.calle.setText("")
        self.label_23.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"No. Exterior", None))
        self.CP.setText("")
        self.label_20.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"Colonia", None))
        self.interior.setText("")
        self.colonia.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"Estado", None))
        self.exterior.setText("")
        self.alcaldia.setText("")
        self.estado.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"ESTADO DE MEXICO", None))
        self.estado.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CIUDAD DE MEXICO", None))

        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CCT", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"INSTITUCI\u00d3N", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"PLANTEL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"TELEFONO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"WEB", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CORREO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"DOMINIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"COLONIA", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CODIGO POSTAL", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"CALLE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"NO.INTERIOR", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"NO.EXTERIOR", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"ALCALDIA", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"ESTADO", None));
        self.label_17.setText(QCoreApplication.translate("Form_ACTUALIZAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ACTUALIZAR ESCUELA</span></p></body></html>", None))
    # retranslateUi

