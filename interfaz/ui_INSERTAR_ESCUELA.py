# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'INSERTAR_ESCUELAwwwKGt.ui'
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

class Ui_Form_INSERTAR_ESCUELA(object):
    def setupUi(self, Form_INSERTAR_ESCUELA):
        if not Form_INSERTAR_ESCUELA.objectName():
            Form_INSERTAR_ESCUELA.setObjectName(u"Form_INSERTAR_ESCUELA")
        Form_INSERTAR_ESCUELA.resize(916, 730)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_INSERTAR_ESCUELA.setWindowIcon(icon)
        Form_INSERTAR_ESCUELA.setStyleSheet(u"QWidget\n"
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
        self.insertar = QPushButton(Form_INSERTAR_ESCUELA)
        self.insertar.setObjectName(u"insertar")
        self.insertar.setGeometry(QRect(770, 660, 131, 31))
        self.insertar.setIcon(icon)
        self.insertar.setIconSize(QSize(20, 20))
        self.label_16 = QLabel(Form_INSERTAR_ESCUELA)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 40, 141, 31))
        self.label_19 = QLabel(Form_INSERTAR_ESCUELA)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(400, 260, 91, 31))
        self.layoutWidget = QWidget(Form_INSERTAR_ESCUELA)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 290, 871, 111))
        self.gridLayout_8 = QGridLayout(self.layoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        font = QFont()
        font.setBold(True)
        self.label_21.setFont(font)

        self.gridLayout_8.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_8.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_24 = QLabel(self.layoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_8.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1)

        self.calle = QLineEdit(self.layoutWidget)
        self.calle.setObjectName(u"calle")

        self.gridLayout_8.addWidget(self.calle, 1, 2, 1, 1)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_8.addWidget(self.label_23, 0, 3, 1, 1)

        self.CP = QLineEdit(self.layoutWidget)
        self.CP.setObjectName(u"CP")

        self.gridLayout_8.addWidget(self.CP, 1, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)

        self.interior = QLineEdit(self.layoutWidget)
        self.interior.setObjectName(u"interior")

        self.gridLayout_8.addWidget(self.interior, 1, 4, 1, 1)

        self.colonia = QLineEdit(self.layoutWidget)
        self.colonia.setObjectName(u"colonia")

        self.gridLayout_8.addWidget(self.colonia, 1, 0, 1, 1)

        self.label_26 = QLabel(self.layoutWidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.gridLayout_8.addWidget(self.label_26, 2, 1, 1, 1)

        self.exterior = QLineEdit(self.layoutWidget)
        self.exterior.setObjectName(u"exterior")

        self.gridLayout_8.addWidget(self.exterior, 1, 3, 1, 1)

        self.alcaldia = QLineEdit(self.layoutWidget)
        self.alcaldia.setObjectName(u"alcaldia")

        self.gridLayout_8.addWidget(self.alcaldia, 3, 0, 1, 1)

        self.estado = QComboBox(self.layoutWidget)
        self.estado.addItem("")
        self.estado.addItem("")
        self.estado.setObjectName(u"estado")

        self.gridLayout_8.addWidget(self.estado, 3, 1, 1, 1)

        self.groupBox = QGroupBox(Form_INSERTAR_ESCUELA)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 420, 891, 231))
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
        self.label_33 = QLabel(Form_INSERTAR_ESCUELA)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(350, 10, 191, 31))
        self.widget = QWidget(Form_INSERTAR_ESCUELA)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(23, 83, 871, 171))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.CCT = QLineEdit(self.widget)
        self.CCT.setObjectName(u"CCT")

        self.gridLayout.addWidget(self.CCT, 1, 0, 1, 1)

        self.plantel = QLineEdit(self.widget)
        self.plantel.setObjectName(u"plantel")

        self.gridLayout.addWidget(self.plantel, 1, 1, 1, 1)

        self.telefono = QLineEdit(self.widget)
        self.telefono.setObjectName(u"telefono")

        self.gridLayout.addWidget(self.telefono, 1, 2, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.web = QLineEdit(self.widget)
        self.web.setObjectName(u"web")

        self.gridLayout.addWidget(self.web, 3, 0, 1, 1)

        self.correo = QLineEdit(self.widget)
        self.correo.setObjectName(u"correo")

        self.gridLayout.addWidget(self.correo, 3, 1, 1, 1)

        self.dominio = QComboBox(self.widget)
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

        self.gridLayout.addWidget(self.dominio, 3, 2, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.institucion = QComboBox(self.widget)
        self.institucion.addItem("")
        self.institucion.addItem("")
        self.institucion.addItem("")
        self.institucion.addItem("")
        self.institucion.setObjectName(u"institucion")

        self.gridLayout.addWidget(self.institucion, 5, 0, 1, 3)


        self.retranslateUi(Form_INSERTAR_ESCUELA)

        QMetaObject.connectSlotsByName(Form_INSERTAR_ESCUELA)
    # setupUi

    def retranslateUi(self, Form_INSERTAR_ESCUELA):
        Form_INSERTAR_ESCUELA.setWindowTitle(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"INSERTAR ESCUELA", None))
        self.insertar.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"INSERTAR", None))
        self.label_16.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Datos generales</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Direcci\u00f3n</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"Codigo Postal", None))
        self.label_25.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"Alcadia o Municipio", None))
        self.label_24.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"No. Interior", None))
        self.label_22.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"Calle", None))
        self.calle.setText("")
        self.label_23.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"No. Exterior", None))
        self.CP.setText("")
        self.label_20.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"Colonia", None))
        self.interior.setText("")
        self.colonia.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"Estado", None))
        self.exterior.setText("")
        self.alcaldia.setText("")
        self.estado.setItemText(0, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"ESTADO DE MEXICO", None))
        self.estado.setItemText(1, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CIUDAD DE MEXICO", None))

        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CCT", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"INSTITUCI\u00d3N", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"PLANTEL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"TELEFONO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"WEB", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CORREO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"DOMINIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"COLONIA", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CODIGO POSTAL", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CALLE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"NO.INTERIOR", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"NO.EXTERIOR", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"ALCALDIA", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"ESTADO", None));
        self.label_33.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">INSERTAR ESCUELA</span></p><p><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CCT", None))
        self.label_2.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"PLANTEL", None))
        self.label_3.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"TELEFONO", None))
        self.CCT.setText("")
        self.plantel.setText("")
        self.telefono.setText("")
        self.label_5.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"SITIO WEB", None))
        self.label_6.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CORREO", None))
        self.label_7.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"DOMINIO                                                                            ", None))
        self.web.setText("")
        self.correo.setText("")
        self.dominio.setItemText(0, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@conalepmex.edu.mx", None))
        self.dominio.setItemText(1, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@bachilleres.edu.mx", None))
        self.dominio.setItemText(2, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@gmail.com", None))
        self.dominio.setItemText(3, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@hotmail.com", None))
        self.dominio.setItemText(4, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@comunidad.unam.mx ", None))
        self.dominio.setItemText(5, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@bachilleres.edu.mx", None))
        self.dominio.setItemText(6, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@outlook.com", None))
        self.dominio.setItemText(7, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@live.com", None))
        self.dominio.setItemText(8, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@IPN.MX", None))
        self.dominio.setItemText(9, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"@enp.unam.mx", None))

        self.label_8.setText(QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"INSTITUCI\u00d3N", None))
        self.institucion.setItemText(0, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"INSTITUTO POLIT\u00c9CNICO NACIONAL", None))
        self.institucion.setItemText(1, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"UNIVERSIDAD NACIONAL AUT\u00d3NOMA DE M\u00c9XICO", None))
        self.institucion.setItemText(2, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"COLEGIO DE BACHILLERES", None))
        self.institucion.setItemText(3, QCoreApplication.translate("Form_INSERTAR_ESCUELA", u"CONALEP", None))

    # retranslateUi

