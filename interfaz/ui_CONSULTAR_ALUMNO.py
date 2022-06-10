# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CONSULTAR_ALUMNOKPCDkE.ui'
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

class Ui_Form_CONSULTAR_ALUMNO(object):
    def setupUi(self, Form_CONSULTAR_ALUMNO):
        if not Form_CONSULTAR_ALUMNO.objectName():
            Form_CONSULTAR_ALUMNO.setObjectName(u"Form_CONSULTAR_ALUMNO")
        Form_CONSULTAR_ALUMNO.resize(1110, 741)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_CONSULTAR_ALUMNO.setWindowIcon(icon)
        Form_CONSULTAR_ALUMNO.setStyleSheet(u"QWidget\n"
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
        self.consultar = QPushButton(Form_CONSULTAR_ALUMNO)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(950, 690, 131, 31))
        self.consultar.setIcon(icon)
        self.consultar.setIconSize(QSize(20, 20))
        self.groupBox = QGroupBox(Form_CONSULTAR_ALUMNO)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 110, 1061, 151))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.DATOS = QTableWidget(self.groupBox)
        if (self.DATOS.columnCount() < 12):
            self.DATOS.setColumnCount(12)
        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.DATOS.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.DATOS.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.DATOS.setObjectName(u"DATOS")
        self.DATOS.setGeometry(QRect(0, 0, 1061, 151))
        self.DATOS.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.DATOS.horizontalHeader().setDefaultSectionSize(155)
        self.label = QLabel(Form_CONSULTAR_ALUMNO)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 111, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.curp = QLineEdit(Form_CONSULTAR_ALUMNO)
        self.curp.setObjectName(u"curp")
        self.curp.setGeometry(QRect(10, 70, 221, 31))
        self.groupBox_2 = QGroupBox(Form_CONSULTAR_ALUMNO)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(370, 300, 331, 151))
        self.groupBox_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.CALIFICACION = QTableWidget(self.groupBox_2)
        if (self.CALIFICACION.columnCount() < 2):
            self.CALIFICACION.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.CALIFICACION.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.CALIFICACION.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        self.CALIFICACION.setObjectName(u"CALIFICACION")
        self.CALIFICACION.setGeometry(QRect(0, 0, 331, 151))
        self.CALIFICACION.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.CALIFICACION.horizontalHeader().setDefaultSectionSize(155)
        self.label_2 = QLabel(Form_CONSULTAR_ALUMNO)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 65, 181, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(Form_CONSULTAR_ALUMNO)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 270, 141, 21))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(Form_CONSULTAR_ALUMNO)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 260, 161, 21))
        self.label_4.setFont(font2)
        self.groupBox_3 = QGroupBox(Form_CONSULTAR_ALUMNO)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 300, 331, 151))
        self.groupBox_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.MEDICOS = QTableWidget(self.groupBox_3)
        if (self.MEDICOS.columnCount() < 5):
            self.MEDICOS.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.MEDICOS.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.MEDICOS.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.MEDICOS.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.MEDICOS.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.MEDICOS.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.MEDICOS.setObjectName(u"MEDICOS")
        self.MEDICOS.setGeometry(QRect(0, 0, 331, 151))
        self.MEDICOS.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.MEDICOS.horizontalHeader().setDefaultSectionSize(155)
        self.groupBox_4 = QGroupBox(Form_CONSULTAR_ALUMNO)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(730, 300, 331, 151))
        self.groupBox_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.TUTOR = QTableWidget(self.groupBox_4)
        if (self.TUTOR.columnCount() < 3):
            self.TUTOR.setColumnCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.TUTOR.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        self.TUTOR.setObjectName(u"TUTOR")
        self.TUTOR.setGeometry(QRect(0, 0, 331, 151))
        self.TUTOR.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.TUTOR.horizontalHeader().setDefaultSectionSize(155)
        self.label_5 = QLabel(Form_CONSULTAR_ALUMNO)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(870, 270, 71, 21))
        self.label_5.setFont(font2)
        self.groupBox_5 = QGroupBox(Form_CONSULTAR_ALUMNO)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(60, 510, 971, 151))
        self.groupBox_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.DIRECCION = QTableWidget(self.groupBox_5)
        if (self.DIRECCION.columnCount() < 7):
            self.DIRECCION.setColumnCount(7)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.DIRECCION.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        self.DIRECCION.setObjectName(u"DIRECCION")
        self.DIRECCION.setGeometry(QRect(0, 0, 971, 151))
        self.DIRECCION.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.DIRECCION.horizontalHeader().setDefaultSectionSize(155)
        self.label_6 = QLabel(Form_CONSULTAR_ALUMNO)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(460, 470, 111, 31))
        self.label_6.setFont(font2)
        self.label_7 = QLabel(Form_CONSULTAR_ALUMNO)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 10, 211, 31))
        self.label_7.setFont(font2)

        self.retranslateUi(Form_CONSULTAR_ALUMNO)

        QMetaObject.connectSlotsByName(Form_CONSULTAR_ALUMNO)
    # setupUi

    def retranslateUi(self, Form_CONSULTAR_ALUMNO):
        Form_CONSULTAR_ALUMNO.setWindowTitle(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CONSULTAR ALUMNO", None))
        self.consultar.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CONSULTAR", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.DATOS.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.DATOS.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem2 = self.DATOS.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem3 = self.DATOS.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"SEXO", None));
        ___qtablewidgetitem4 = self.DATOS.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"FECHA DE NACIMIENTO", None));
        ___qtablewidgetitem5 = self.DATOS.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"FECHA DE INSCRIPCI\u00d3N", None));
        ___qtablewidgetitem6 = self.DATOS.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CURP", None));
        ___qtablewidgetitem7 = self.DATOS.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"GRADO ACADEMICO", None));
        ___qtablewidgetitem8 = self.DATOS.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CARRERA", None));
        ___qtablewidgetitem9 = self.DATOS.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"INSCRITO", None));
        ___qtablewidgetitem10 = self.DATOS.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"BECADO", None));
        ___qtablewidgetitem11 = self.DATOS.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"PLANTEL", None));
        self.label.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"INGRESE EL CURP:", None))
        self.groupBox_2.setTitle("")
        ___qtablewidgetitem12 = self.CALIFICACION.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"MATERIA", None));
        ___qtablewidgetitem13 = self.CALIFICACION.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CALIFICACION", None));
        self.label_2.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"DATOS GENERALES", None))
        self.label_3.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CALIFICACI\u00d3N", None))
        self.label_4.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"DATOS MEDICOS", None))
        self.groupBox_3.setTitle("")
        ___qtablewidgetitem14 = self.MEDICOS.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"NSS", None));
        ___qtablewidgetitem15 = self.MEDICOS.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"SEGURO", None));
        ___qtablewidgetitem16 = self.MEDICOS.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"TIPO DE SANGRE", None));
        ___qtablewidgetitem17 = self.MEDICOS.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"ENFERMEDADES", None));
        ___qtablewidgetitem18 = self.MEDICOS.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"DISCAPACIDAD", None));
        self.groupBox_4.setTitle("")
        ___qtablewidgetitem19 = self.TUTOR.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"NOMBRE", None));
        ___qtablewidgetitem20 = self.TUTOR.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem21 = self.TUTOR.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"APELLIDO MATERNO", None));
        self.label_5.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"TUTOR", None))
        self.groupBox_5.setTitle("")
        ___qtablewidgetitem22 = self.DIRECCION.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"ESTADO", None));
        ___qtablewidgetitem23 = self.DIRECCION.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"COLONIA", None));
        ___qtablewidgetitem24 = self.DIRECCION.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"ALCALDIA", None));
        ___qtablewidgetitem25 = self.DIRECCION.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CODIGO POSTAL", None));
        ___qtablewidgetitem26 = self.DIRECCION.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CALLE", None));
        ___qtablewidgetitem27 = self.DIRECCION.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"NO.EXTERIOR", None));
        ___qtablewidgetitem28 = self.DIRECCION.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"NO.INTERIOR", None));
        self.label_6.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"DIRECCI\u00d3N", None))
        self.label_7.setText(QCoreApplication.translate("Form_CONSULTAR_ALUMNO", u"CONSULTAR ALUMNO", None))
    # retranslateUi

