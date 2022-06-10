# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ACTUALIZAR_TUTORKtfwpv.ui'
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

class Ui_Form_ACTUALIZAR_TUTOR(object):
    def setupUi(self, Form_ACTUALIZAR_TUTOR):
        if not Form_ACTUALIZAR_TUTOR.objectName():
            Form_ACTUALIZAR_TUTOR.setObjectName(u"Form_ACTUALIZAR_TUTOR")
        Form_ACTUALIZAR_TUTOR.resize(912, 622)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-actualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ACTUALIZAR_TUTOR.setWindowIcon(icon)
        Form_ACTUALIZAR_TUTOR.setStyleSheet(u"QWidget\n"
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
        self.actualizar = QPushButton(Form_ACTUALIZAR_TUTOR)
        self.actualizar.setObjectName(u"actualizar")
        self.actualizar.setGeometry(QRect(770, 560, 131, 31))
        self.actualizar.setIcon(icon)
        self.actualizar.setIconSize(QSize(20, 20))
        self.label_19 = QLabel(Form_ACTUALIZAR_TUTOR)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(410, 130, 91, 31))
        self.layoutWidget = QWidget(Form_ACTUALIZAR_TUTOR)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 170, 691, 131))
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

        self.label_27 = QLabel(Form_ACTUALIZAR_TUTOR)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(420, 30, 51, 31))
        self.layoutWidget1 = QWidget(Form_ACTUALIZAR_TUTOR)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(690, 70, 72, 61))
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

        self.groupBox = QGroupBox(Form_ACTUALIZAR_TUTOR)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 320, 891, 231))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setKerning(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 891, 231))
        self.tableWidget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.label_33 = QLabel(Form_ACTUALIZAR_TUTOR)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(360, 0, 191, 31))
        self.layoutWidget2 = QWidget(Form_ACTUALIZAR_TUTOR)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(110, 70, 554, 61))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.layoutWidget2)
        self.label_32.setObjectName(u"label_32")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.label_32.setFont(font2)

        self.gridLayout.addWidget(self.label_32, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_28 = QLabel(self.layoutWidget2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.gridLayout_9.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_29 = QLabel(self.layoutWidget2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.gridLayout_9.addWidget(self.label_29, 0, 2, 1, 1)

        self.nombre_2 = QLineEdit(self.layoutWidget2)
        self.nombre_2.setObjectName(u"nombre_2")

        self.gridLayout_9.addWidget(self.nombre_2, 1, 0, 1, 1)

        self.apellido_pat_tutor = QLineEdit(self.layoutWidget2)
        self.apellido_pat_tutor.setObjectName(u"apellido_pat_tutor")

        self.gridLayout_9.addWidget(self.apellido_pat_tutor, 1, 1, 1, 1)

        self.apellido_mat_tutor = QLineEdit(self.layoutWidget2)
        self.apellido_mat_tutor.setObjectName(u"apellido_mat_tutor")

        self.gridLayout_9.addWidget(self.apellido_mat_tutor, 1, 2, 1, 1)

        self.label_30 = QLabel(self.layoutWidget2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_9.addWidget(self.label_30, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_9, 0, 1, 2, 1)

        self.ID_TUTOR = QLineEdit(self.layoutWidget2)
        self.ID_TUTOR.setObjectName(u"ID_TUTOR")

        self.gridLayout.addWidget(self.ID_TUTOR, 1, 0, 1, 1)


        self.retranslateUi(Form_ACTUALIZAR_TUTOR)

        QMetaObject.connectSlotsByName(Form_ACTUALIZAR_TUTOR)
    # setupUi

    def retranslateUi(self, Form_ACTUALIZAR_TUTOR):
        Form_ACTUALIZAR_TUTOR.setWindowTitle(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"ACTUALIZAR TUTOR", None))
        self.actualizar.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"ACTUALIZAR", None))
        self.label_19.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Direcci\u00f3n</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Calle", None))
        self.label_23.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"No. Exterior", None))
        self.CP.setText("")
        self.label_25.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Alcadia o Municipio", None))
        self.interior.setText("")
        self.colonia.setText("")
        self.alcaldia.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Estado", None))
        self.calle.setText("")
        self.label_24.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"No. Interior", None))
        self.label_20.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Colonia", None))
        self.label_21.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Codigo Postal", None))
        self.exterior.setText("")
        self.estado.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"ESTADO DE MEXICO", None))
        self.estado.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"CIUDAD DE MEXICO", None))

        self.label_27.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Tutor</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Sexo", None))
        self.sexo_2.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"H", None))
        self.sexo_2.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"M", None))

        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"NOMBRE", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"SEXO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"COLONIA", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"CODIGO POSTAL", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"CALLE", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"NO.EXTERIOR", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"NO.INTERIOR", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"ALCALDIA", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"ESTADO", None));
        self.label_33.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ACTUALIZAR TUTOR</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Ingrese el ID del tutor", None))
        self.label_28.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Nombre(s)", None))
        self.label_29.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Apellido Materno", None))
        self.nombre_2.setText("")
        self.apellido_pat_tutor.setText("")
        self.apellido_mat_tutor.setText("")
        self.label_30.setText(QCoreApplication.translate("Form_ACTUALIZAR_TUTOR", u"Apellido Paterno", None))
        self.ID_TUTOR.setText("")
    # retranslateUi

