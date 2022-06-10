# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'INSERTAR_TUTORfsvlkW.ui'
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

class Ui_Form_INSERTAR_TUTOR(object):
    def setupUi(self, Form_INSERTAR_TUTOR):
        if not Form_INSERTAR_TUTOR.objectName():
            Form_INSERTAR_TUTOR.setObjectName(u"Form_INSERTAR_TUTOR")
        Form_INSERTAR_TUTOR.resize(912, 631)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_INSERTAR_TUTOR.setWindowIcon(icon)
        Form_INSERTAR_TUTOR.setStyleSheet(u"QWidget\n"
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
        self.insertar = QPushButton(Form_INSERTAR_TUTOR)
        self.insertar.setObjectName(u"insertar")
        self.insertar.setGeometry(QRect(800, 580, 101, 31))
        self.insertar.setIcon(icon)
        self.insertar.setIconSize(QSize(20, 20))
        self.label_19 = QLabel(Form_INSERTAR_TUTOR)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(410, 140, 91, 31))
        self.layoutWidget = QWidget(Form_INSERTAR_TUTOR)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 180, 691, 124))
        self.gridLayout_8 = QGridLayout(self.layoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        font = QFont()
        font.setBold(True)
        self.label_22.setFont(font)

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_8.addWidget(self.label_23, 0, 3, 1, 1)

        self.CP = QLineEdit(self.layoutWidget)
        self.CP.setObjectName(u"CP")

        self.gridLayout_8.addWidget(self.CP, 1, 1, 1, 1)

        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_8.addWidget(self.label_25, 2, 0, 1, 1)

        self.interior = QLineEdit(self.layoutWidget)
        self.interior.setObjectName(u"interior")

        self.gridLayout_8.addWidget(self.interior, 1, 4, 1, 1)

        self.colonia = QLineEdit(self.layoutWidget)
        self.colonia.setObjectName(u"colonia")

        self.gridLayout_8.addWidget(self.colonia, 1, 0, 1, 1)

        self.alcaldia = QLineEdit(self.layoutWidget)
        self.alcaldia.setObjectName(u"alcaldia")

        self.gridLayout_8.addWidget(self.alcaldia, 3, 0, 1, 1)

        self.label_26 = QLabel(self.layoutWidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.gridLayout_8.addWidget(self.label_26, 2, 1, 1, 1)

        self.calle = QLineEdit(self.layoutWidget)
        self.calle.setObjectName(u"calle")

        self.gridLayout_8.addWidget(self.calle, 1, 2, 1, 1)

        self.label_24 = QLabel(self.layoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_8.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_8.addWidget(self.label_21, 0, 1, 1, 1)

        self.exterior = QLineEdit(self.layoutWidget)
        self.exterior.setObjectName(u"exterior")

        self.gridLayout_8.addWidget(self.exterior, 1, 3, 1, 1)

        self.estado = QComboBox(self.layoutWidget)
        self.estado.addItem("")
        self.estado.addItem("")
        self.estado.setObjectName(u"estado")

        self.gridLayout_8.addWidget(self.estado, 3, 1, 1, 1)

        self.label_27 = QLabel(Form_INSERTAR_TUTOR)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(420, 40, 51, 31))
        self.layoutWidget_2 = QWidget(Form_INSERTAR_TUTOR)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(200, 80, 413, 51))
        self.gridLayout_9 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.layoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label_28.setFont(font1)

        self.gridLayout_9.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_29 = QLabel(self.layoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout_9.addWidget(self.label_29, 0, 2, 1, 1)

        self.nombre_2 = QLineEdit(self.layoutWidget_2)
        self.nombre_2.setObjectName(u"nombre_2")

        self.gridLayout_9.addWidget(self.nombre_2, 1, 0, 1, 1)

        self.apellido_pat_tutor = QLineEdit(self.layoutWidget_2)
        self.apellido_pat_tutor.setObjectName(u"apellido_pat_tutor")

        self.gridLayout_9.addWidget(self.apellido_pat_tutor, 1, 1, 1, 1)

        self.apellido_mat_tutor = QLineEdit(self.layoutWidget_2)
        self.apellido_mat_tutor.setObjectName(u"apellido_mat_tutor")

        self.gridLayout_9.addWidget(self.apellido_mat_tutor, 1, 2, 1, 1)

        self.label_30 = QLabel(self.layoutWidget_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout_9.addWidget(self.label_30, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(Form_INSERTAR_TUTOR)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(620, 80, 72, 51))
        self.gridLayout_10 = QGridLayout(self.layoutWidget1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.layoutWidget1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_10.addWidget(self.label_31, 0, 0, 1, 1)

        self.sexo_2 = QComboBox(self.layoutWidget1)
        self.sexo_2.addItem("")
        self.sexo_2.addItem("")
        self.sexo_2.setObjectName(u"sexo_2")

        self.gridLayout_10.addWidget(self.sexo_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Form_INSERTAR_TUTOR)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 340, 891, 231))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        font2 = QFont()
        font2.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 891, 231))
        self.tableWidget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.label_33 = QLabel(Form_INSERTAR_TUTOR)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(370, 10, 161, 31))

        self.retranslateUi(Form_INSERTAR_TUTOR)

        QMetaObject.connectSlotsByName(Form_INSERTAR_TUTOR)
    # setupUi

    def retranslateUi(self, Form_INSERTAR_TUTOR):
        Form_INSERTAR_TUTOR.setWindowTitle(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"INSERTAR TUTOR", None))
        self.insertar.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"INSERTAR", None))
        self.label_19.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Direcci\u00f3n</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Calle", None))
        self.label_23.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"No. Exterior", None))
        self.CP.setText("")
        self.label_25.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Alcadia o Municipio", None))
        self.interior.setText("")
        self.colonia.setText("")
        self.alcaldia.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Estado", None))
        self.calle.setText("")
        self.label_24.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"No. Interior", None))
        self.label_20.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Colonia", None))
        self.label_21.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Codigo Postal", None))
        self.exterior.setText("")
        self.estado.setItemText(0, QCoreApplication.translate("Form_INSERTAR_TUTOR", u"ESTADO DE MEXICO", None))
        self.estado.setItemText(1, QCoreApplication.translate("Form_INSERTAR_TUTOR", u"CIUDAD DE MEXICO", None))

        self.label_27.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Tutor</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Nombre(s)", None))
        self.label_29.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Apellido Materno", None))
        self.nombre_2.setText("")
        self.apellido_pat_tutor.setText("")
        self.apellido_mat_tutor.setText("")
        self.label_30.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Apellido Paterno", None))
        self.label_31.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"Sexo", None))
        self.sexo_2.setItemText(0, QCoreApplication.translate("Form_INSERTAR_TUTOR", u"H", None))
        self.sexo_2.setItemText(1, QCoreApplication.translate("Form_INSERTAR_TUTOR", u"M", None))

        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"SEXO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"COLONIA", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"CODIGO POSTAL", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"CALLE", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"NO.EXTERIOR", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"NO.INTERIOR", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"ALCALDIA", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"ESTADO", None));
        self.label_33.setText(QCoreApplication.translate("Form_INSERTAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">INSERTAR TUTOR</span></p><p><br/></p></body></html>", None))
    # retranslateUi

