# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CONSULTAR_TUTORlGZyeO.ui'
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

class Ui_Form_CONSULTAR_TUTOR(object):
    def setupUi(self, Form_CONSULTAR_TUTOR):
        if not Form_CONSULTAR_TUTOR.objectName():
            Form_CONSULTAR_TUTOR.setObjectName(u"Form_CONSULTAR_TUTOR")
        Form_CONSULTAR_TUTOR.resize(809, 545)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_CONSULTAR_TUTOR.setWindowIcon(icon)
        Form_CONSULTAR_TUTOR.setStyleSheet(u"QWidget\n"
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
        self.consultar = QPushButton(Form_CONSULTAR_TUTOR)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(20, 240, 221, 61))
        self.consultar.setIcon(icon)
        self.consultar.setIconSize(QSize(20, 20))
        self.groupBox = QGroupBox(Form_CONSULTAR_TUTOR)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(310, 235, 481, 131))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.DATOS = QTableWidget(self.groupBox)
        if (self.DATOS.columnCount() < 3):
            self.DATOS.setColumnCount(3)
        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.DATOS.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.DATOS.setObjectName(u"DATOS")
        self.DATOS.setGeometry(QRect(0, 0, 481, 131))
        self.DATOS.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.DATOS.horizontalHeader().setDefaultSectionSize(155)
        self.label = QLabel(Form_CONSULTAR_TUTOR)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 211, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.nombre = QLineEdit(Form_CONSULTAR_TUTOR)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(20, 80, 221, 31))
        self.label_2 = QLabel(Form_CONSULTAR_TUTOR)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 200, 111, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.groupBox_4 = QGroupBox(Form_CONSULTAR_TUTOR)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(310, 70, 481, 131))
        self.groupBox_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.TUTOR = QTableWidget(self.groupBox_4)
        if (self.TUTOR.columnCount() < 4):
            self.TUTOR.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.TUTOR.setObjectName(u"TUTOR")
        self.TUTOR.setGeometry(QRect(0, 0, 481, 131))
        self.TUTOR.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.TUTOR.horizontalHeader().setDefaultSectionSize(155)
        self.label_5 = QLabel(Form_CONSULTAR_TUTOR)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 40, 71, 21))
        self.label_5.setFont(font2)
        self.groupBox_5 = QGroupBox(Form_CONSULTAR_TUTOR)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(310, 400, 481, 131))
        self.groupBox_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.DIRECCION = QTableWidget(self.groupBox_5)
        if (self.DIRECCION.columnCount() < 7):
            self.DIRECCION.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.DIRECCION.setObjectName(u"DIRECCION")
        self.DIRECCION.setGeometry(QRect(0, 0, 481, 131))
        self.DIRECCION.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.DIRECCION.horizontalHeader().setDefaultSectionSize(155)
        self.label_6 = QLabel(Form_CONSULTAR_TUTOR)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 370, 111, 31))
        self.label_6.setFont(font2)
        self.label_3 = QLabel(Form_CONSULTAR_TUTOR)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 211, 16))
        self.label_3.setFont(font1)
        self.apellido_pat = QLineEdit(Form_CONSULTAR_TUTOR)
        self.apellido_pat.setObjectName(u"apellido_pat")
        self.apellido_pat.setGeometry(QRect(20, 140, 221, 31))
        self.apellido_materno = QLineEdit(Form_CONSULTAR_TUTOR)
        self.apellido_materno.setObjectName(u"apellido_materno")
        self.apellido_materno.setGeometry(QRect(20, 200, 221, 31))
        self.label_4 = QLabel(Form_CONSULTAR_TUTOR)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 211, 16))
        self.label_4.setFont(font1)
        self.label_7 = QLabel(Form_CONSULTAR_TUTOR)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 0, 191, 21))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_7.setFont(font3)

        self.retranslateUi(Form_CONSULTAR_TUTOR)

        QMetaObject.connectSlotsByName(Form_CONSULTAR_TUTOR)
    # setupUi

    def retranslateUi(self, Form_CONSULTAR_TUTOR):
        Form_CONSULTAR_TUTOR.setWindowTitle(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"CONSULTAR TUTOR", None))
        self.consultar.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"CONSULTAR", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.DATOS.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.DATOS.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem2 = self.DATOS.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"APELLIDO MATERNO", None));
        self.label.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"INGRESE EL NOMBRE:", None))
        self.label_2.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"TUTORADO", None))
        self.groupBox_4.setTitle("")
        ___qtablewidgetitem3 = self.TUTOR.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"NOMBRE", None));
        ___qtablewidgetitem4 = self.TUTOR.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem5 = self.TUTOR.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem6 = self.TUTOR.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"SEXO", None));
        self.label_5.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"TUTOR", None))
        self.groupBox_5.setTitle("")
        ___qtablewidgetitem7 = self.DIRECCION.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"ESTADO", None));
        ___qtablewidgetitem8 = self.DIRECCION.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"COLONIA", None));
        ___qtablewidgetitem9 = self.DIRECCION.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"ALCALDIA", None));
        ___qtablewidgetitem10 = self.DIRECCION.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"CODIGO POSTAL", None));
        ___qtablewidgetitem11 = self.DIRECCION.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"CALLE", None));
        ___qtablewidgetitem12 = self.DIRECCION.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"NO.EXTERIOR", None));
        ___qtablewidgetitem13 = self.DIRECCION.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"NO.INTERIOR", None));
        self.label_6.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"DIRECCI\u00d3N", None))
        self.label_3.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"APELLIDO PATERNO:", None))
        self.apellido_pat.setText("")
        self.apellido_materno.setText("")
        self.label_4.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"APELLIDO MATERNO:", None))
        self.label_7.setText(QCoreApplication.translate("Form_CONSULTAR_TUTOR", u"CONSULTAR TUTOR", None))
    # retranslateUi

