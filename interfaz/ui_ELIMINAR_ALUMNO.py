# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ELIMINAR_ALUMNObymEkm.ui'
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

class Ui_Form1(object):
    def setupUi(self, Form1):
        if not Form1.objectName():
            Form1.setObjectName(u"Form1")
        Form1.resize(912, 575)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form1.setWindowIcon(icon)
        Form1.setStyleSheet(u"QWidget\n"
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
        self.insertar = QPushButton(Form1)
        self.insertar.setObjectName(u"insertar")
        self.insertar.setGeometry(QRect(210, 67, 111, 31))
        self.insertar.setIcon(icon)
        self.insertar.setIconSize(QSize(20, 20))
        self.groupBox = QGroupBox(Form1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 120, 891, 411))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tablaeliminar = QTableWidget(self.groupBox)
        if (self.tablaeliminar.columnCount() < 25):
            self.tablaeliminar.setColumnCount(25)
        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tablaeliminar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tablaeliminar.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        self.tablaeliminar.setObjectName(u"tablaeliminar")
        self.tablaeliminar.setGeometry(QRect(0, 0, 891, 411))
        self.tablaeliminar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tablaeliminar.horizontalHeader().setDefaultSectionSize(155)
        self.label = QLabel(Form1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 41, 151, 18))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.curp = QLineEdit(Form1)
        self.curp.setObjectName(u"curp")
        self.curp.setGeometry(QRect(11, 65, 191, 31))
        self.label_2 = QLabel(Form1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 10, 181, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_2.setFont(font2)

        self.retranslateUi(Form1)

        QMetaObject.connectSlotsByName(Form1)
    # setupUi

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(QCoreApplication.translate("Form1", u"ELIMNAR ALUMNO", None))
        self.insertar.setText(QCoreApplication.translate("Form1", u"ELIMINAR", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tablaeliminar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form1", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.tablaeliminar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form1", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem2 = self.tablaeliminar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form1", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem3 = self.tablaeliminar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form1", u"SEXO", None));
        ___qtablewidgetitem4 = self.tablaeliminar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form1", u"FECHA DE NACIMIENTO", None));
        ___qtablewidgetitem5 = self.tablaeliminar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form1", u"FECHA DE INSCRIPCI\u00d3N", None));
        ___qtablewidgetitem6 = self.tablaeliminar.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form1", u"CURP", None));
        ___qtablewidgetitem7 = self.tablaeliminar.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form1", u"GRADO ACADEMICO", None));
        ___qtablewidgetitem8 = self.tablaeliminar.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form1", u"CARRERA", None));
        ___qtablewidgetitem9 = self.tablaeliminar.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form1", u"INSCRITO", None));
        ___qtablewidgetitem10 = self.tablaeliminar.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form1", u"BECADO", None));
        ___qtablewidgetitem11 = self.tablaeliminar.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form1", u"SEGURO", None));
        ___qtablewidgetitem12 = self.tablaeliminar.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form1", u"TIPO DE SANGRE", None));
        ___qtablewidgetitem13 = self.tablaeliminar.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form1", u"DISCAPACIDAD", None));
        ___qtablewidgetitem14 = self.tablaeliminar.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form1", u"ENFERMEDADES CRONICAS", None));
        ___qtablewidgetitem15 = self.tablaeliminar.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form1", u"NUMERO DE SEGURO SOCIAL", None));
        ___qtablewidgetitem16 = self.tablaeliminar.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form1", u"ESTADO", None));
        ___qtablewidgetitem17 = self.tablaeliminar.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form1", u"COLONIA", None));
        ___qtablewidgetitem18 = self.tablaeliminar.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form1", u"ALCALDIA", None));
        ___qtablewidgetitem19 = self.tablaeliminar.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form1", u"CODIGO POSTAL", None));
        ___qtablewidgetitem20 = self.tablaeliminar.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form1", u"CALLE", None));
        ___qtablewidgetitem21 = self.tablaeliminar.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form1", u"PLANTEL", None));
        ___qtablewidgetitem22 = self.tablaeliminar.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form1", u"NOMBRE TUTOR", None));
        ___qtablewidgetitem23 = self.tablaeliminar.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form1", u"APELLIDO PATERNO TUTOR", None));
        ___qtablewidgetitem24 = self.tablaeliminar.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form1", u"APELLIDO MATERNO TUTOR", None));
        self.label.setText(QCoreApplication.translate("Form1", u"INGRESE EL CURP:                    ", None))
        self.label_2.setText(QCoreApplication.translate("Form1", u"ELIMINAR ALUMNO", None))
    # retranslateUi

