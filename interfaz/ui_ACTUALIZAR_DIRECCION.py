# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ACTUALIZAR_DIRECCIONxykkkm.ui'
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

class Ui_Form_ACTUALIZAR_DIRECCION(object):
    def setupUi(self, Form_ACTUALIZAR_DIRECCION):
        if not Form_ACTUALIZAR_DIRECCION.objectName():
            Form_ACTUALIZAR_DIRECCION.setObjectName(u"Form_ACTUALIZAR_DIRECCION")
        Form_ACTUALIZAR_DIRECCION.resize(916, 516)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-actualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ACTUALIZAR_DIRECCION.setWindowIcon(icon)
        Form_ACTUALIZAR_DIRECCION.setStyleSheet(u"QWidget\n"
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
        self.insertar = QPushButton(Form_ACTUALIZAR_DIRECCION)
        self.insertar.setObjectName(u"insertar")
        self.insertar.setGeometry(QRect(730, 470, 131, 31))
        self.insertar.setIcon(icon)
        self.insertar.setIconSize(QSize(20, 20))
        self.label_19 = QLabel(Form_ACTUALIZAR_DIRECCION)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(380, 0, 231, 31))
        self.layoutWidget = QWidget(Form_ACTUALIZAR_DIRECCION)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 80, 701, 121))
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

        self.groupBox = QGroupBox(Form_ACTUALIZAR_DIRECCION)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 220, 801, 231))
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
        self.tabla.setGeometry(QRect(0, 0, 801, 231))
        self.tabla.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tabla.horizontalHeader().setDefaultSectionSize(155)
        self.label_27 = QLabel(Form_ACTUALIZAR_DIRECCION)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(90, 20, 271, 16))
        self.label_27.setFont(font)
        self.ID_DIRECCION = QLineEdit(Form_ACTUALIZAR_DIRECCION)
        self.ID_DIRECCION.setObjectName(u"ID_DIRECCION")
        self.ID_DIRECCION.setGeometry(QRect(90, 40, 151, 31))

        self.retranslateUi(Form_ACTUALIZAR_DIRECCION)

        QMetaObject.connectSlotsByName(Form_ACTUALIZAR_DIRECCION)
    # setupUi

    def retranslateUi(self, Form_ACTUALIZAR_DIRECCION):
        Form_ACTUALIZAR_DIRECCION.setWindowTitle(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"ACTUALIZAR DIRECCION", None))
        self.insertar.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"ACTUALIZAR", None))
        self.label_19.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ACTUALIZAR DIRECCI\u00d3N</span></p><p><br/></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"Codigo Postal", None))
        self.label_25.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"Alcadia o Municipio", None))
        self.label_24.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"No. Interior", None))
        self.label_22.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"Calle", None))
        self.calle.setText("")
        self.label_23.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"No. Exterior", None))
        self.CP.setText("")
        self.label_20.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"Colonia", None))
        self.interior.setText("")
        self.colonia.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"Estado", None))
        self.exterior.setText("")
        self.alcaldia.setText("")
        self.estado.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"ESTADO DE MEXICO", None))
        self.estado.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"CIUDAD DE MEXICO", None))

        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"ID", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"ESTADO", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"COLONIA", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"ALCALDIA", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"CODIGO POSTAL", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"CALLE", None));
        ___qtablewidgetitem6 = self.tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"NO.EXTERIOR", None));
        ___qtablewidgetitem7 = self.tabla.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"NO.INTERIOR", None));
        self.label_27.setText(QCoreApplication.translate("Form_ACTUALIZAR_DIRECCION", u"INSERTE EL ID DE LA DIRECCION A ACTUALIZAR:", None))
    # retranslateUi

