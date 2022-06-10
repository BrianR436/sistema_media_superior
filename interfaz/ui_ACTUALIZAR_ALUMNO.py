# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ACTUALIZAR_ALUMNOEummrz.ui'
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

class Ui_Form_ACTUALIZAR_ALUMNO(object):
    def setupUi(self, Form_ACTUALIZAR_ALUMNO):
        if not Form_ACTUALIZAR_ALUMNO.objectName():
            Form_ACTUALIZAR_ALUMNO.setObjectName(u"Form_ACTUALIZAR_ALUMNO")
        Form_ACTUALIZAR_ALUMNO.resize(912, 823)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-actualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ACTUALIZAR_ALUMNO.setWindowIcon(icon)
        Form_ACTUALIZAR_ALUMNO.setToolTipDuration(-1)
        Form_ACTUALIZAR_ALUMNO.setStyleSheet(u"QWidget\n"
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
        self.actualizar = QPushButton(Form_ACTUALIZAR_ALUMNO)
        self.actualizar.setObjectName(u"actualizar")
        self.actualizar.setGeometry(QRect(770, 780, 131, 31))
        self.actualizar.setIcon(icon)
        self.actualizar.setIconSize(QSize(20, 20))
        self.label_16 = QLabel(Form_ACTUALIZAR_ALUMNO)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(390, 40, 141, 31))
        self.label_19 = QLabel(Form_ACTUALIZAR_ALUMNO)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(420, 300, 91, 31))
        self.layoutWidget = QWidget(Form_ACTUALIZAR_ALUMNO)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 868, 221))
        self.gridLayout_7 = QGridLayout(self.layoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fecha_na = QLineEdit(self.layoutWidget)
        self.fecha_na.setObjectName(u"fecha_na")

        self.gridLayout_2.addWidget(self.fecha_na, 1, 1, 1, 1)

        self.fecha_ins = QLineEdit(self.layoutWidget)
        self.fecha_ins.setObjectName(u"fecha_ins")

        self.gridLayout_2.addWidget(self.fecha_ins, 1, 2, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setBold(True)
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 0, 3, 1, 1)

        self.curp = QLineEdit(self.layoutWidget)
        self.curp.setObjectName(u"curp")

        self.gridLayout_2.addWidget(self.curp, 1, 3, 1, 1)

        self.sexo = QComboBox(self.layoutWidget)
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.sexo.setObjectName(u"sexo")

        self.gridLayout_2.addWidget(self.sexo, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.nombre = QLineEdit(self.layoutWidget)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 1, 0, 1, 1)

        self.apellido_pat = QLineEdit(self.layoutWidget)
        self.apellido_pat.setObjectName(u"apellido_pat")

        self.gridLayout.addWidget(self.apellido_pat, 1, 1, 1, 1)

        self.apellido_mat = QLineEdit(self.layoutWidget)
        self.apellido_mat.setObjectName(u"apellido_mat")

        self.gridLayout.addWidget(self.apellido_mat, 1, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_3.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_3.addWidget(self.label_11, 0, 3, 1, 1)

        self.grado = QComboBox(self.layoutWidget)
        self.grado.addItem("")
        self.grado.addItem("")
        self.grado.addItem("")
        self.grado.addItem("")
        self.grado.addItem("")
        self.grado.addItem("")
        self.grado.addItem("")
        self.grado.setObjectName(u"grado")

        self.gridLayout_3.addWidget(self.grado, 1, 0, 1, 1)

        self.inscripcion = QComboBox(self.layoutWidget)
        self.inscripcion.addItem("")
        self.inscripcion.addItem("")
        self.inscripcion.setObjectName(u"inscripcion")

        self.gridLayout_3.addWidget(self.inscripcion, 1, 1, 1, 1)

        self.beca = QComboBox(self.layoutWidget)
        self.beca.addItem("")
        self.beca.addItem("")
        self.beca.setObjectName(u"beca")

        self.gridLayout_3.addWidget(self.beca, 1, 2, 1, 1)

        self.sangre = QComboBox(self.layoutWidget)
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.addItem("")
        self.sangre.setObjectName(u"sangre")

        self.gridLayout_3.addWidget(self.sangre, 1, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.seguro = QComboBox(self.layoutWidget)
        self.seguro.addItem("")
        self.seguro.addItem("")
        self.seguro.setObjectName(u"seguro")

        self.gridLayout_4.addWidget(self.seguro, 1, 0, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.carrera = QComboBox(self.layoutWidget)
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.addItem("")
        self.carrera.setObjectName(u"carrera")

        self.gridLayout_4.addWidget(self.carrera, 1, 5, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_4.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)

        self.cronica = QComboBox(self.layoutWidget)
        self.cronica.addItem("")
        self.cronica.addItem("")
        self.cronica.setObjectName(u"cronica")

        self.gridLayout_4.addWidget(self.cronica, 1, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_4.addWidget(self.label_15, 0, 3, 1, 1)

        self.discapacidad = QComboBox(self.layoutWidget)
        self.discapacidad.addItem("")
        self.discapacidad.addItem("")
        self.discapacidad.setObjectName(u"discapacidad")

        self.gridLayout_4.addWidget(self.discapacidad, 1, 1, 1, 1)

        self.NSS = QLineEdit(self.layoutWidget)
        self.NSS.setObjectName(u"NSS")

        self.gridLayout_4.addWidget(self.NSS, 1, 3, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_4.addWidget(self.label_17, 0, 5, 1, 1)

        self.CCT = QLineEdit(self.layoutWidget)
        self.CCT.setObjectName(u"CCT")

        self.gridLayout_4.addWidget(self.CCT, 1, 4, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_4.addWidget(self.label_18, 0, 4, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.layoutWidget1 = QWidget(Form_ACTUALIZAR_ALUMNO)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(120, 325, 691, 111))
        self.gridLayout_8 = QGridLayout(self.layoutWidget1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_8.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_8.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_8.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1)

        self.calle = QLineEdit(self.layoutWidget1)
        self.calle.setObjectName(u"calle")

        self.gridLayout_8.addWidget(self.calle, 1, 2, 1, 1)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_8.addWidget(self.label_23, 0, 3, 1, 1)

        self.CP = QLineEdit(self.layoutWidget1)
        self.CP.setObjectName(u"CP")

        self.gridLayout_8.addWidget(self.CP, 1, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)

        self.interior = QLineEdit(self.layoutWidget1)
        self.interior.setObjectName(u"interior")

        self.gridLayout_8.addWidget(self.interior, 1, 4, 1, 1)

        self.colonia = QLineEdit(self.layoutWidget1)
        self.colonia.setObjectName(u"colonia")

        self.gridLayout_8.addWidget(self.colonia, 1, 0, 1, 1)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

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

        self.label_27 = QLabel(Form_ACTUALIZAR_ALUMNO)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(440, 430, 51, 31))
        self.layoutWidget_2 = QWidget(Form_ACTUALIZAR_ALUMNO)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(210, 470, 413, 51))
        self.gridLayout_9 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.layoutWidget_2)
        self.label_28.setObjectName(u"label_28")
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

        self.layoutWidget2 = QWidget(Form_ACTUALIZAR_ALUMNO)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(630, 470, 72, 51))
        self.gridLayout_10 = QGridLayout(self.layoutWidget2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.layoutWidget2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_10.addWidget(self.label_31, 0, 0, 1, 1)

        self.sexo_2 = QComboBox(self.layoutWidget2)
        self.sexo_2.addItem("")
        self.sexo_2.addItem("")
        self.sexo_2.setObjectName(u"sexo_2")

        self.gridLayout_10.addWidget(self.sexo_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Form_ACTUALIZAR_ALUMNO)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 540, 891, 231))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 25):
            self.tableWidget.setColumnCount(25)
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
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 891, 231))
        self.tableWidget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.label_32 = QLabel(Form_ACTUALIZAR_ALUMNO)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 20, 283, 16))
        self.label_32.setFont(font1)
        self.curp_nuevo = QLineEdit(Form_ACTUALIZAR_ALUMNO)
        self.curp_nuevo.setObjectName(u"curp_nuevo")
        self.curp_nuevo.setGeometry(QRect(10, 41, 283, 31))
        self.label_33 = QLabel(Form_ACTUALIZAR_ALUMNO)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(360, 0, 211, 31))

        self.retranslateUi(Form_ACTUALIZAR_ALUMNO)

        QMetaObject.connectSlotsByName(Form_ACTUALIZAR_ALUMNO)
    # setupUi

    def retranslateUi(self, Form_ACTUALIZAR_ALUMNO):
        Form_ACTUALIZAR_ALUMNO.setWindowTitle(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ACTUALIZAR ALUMNO", None))
#if QT_CONFIG(tooltip)
        Form_ACTUALIZAR_ALUMNO.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Form_ACTUALIZAR_ALUMNO.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.actualizar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actualizar.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.actualizar.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ACTUALIZAR", None))
        self.label_16.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Datos generales</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Direcci\u00f3n</span></p></body></html>", None))
        self.fecha_na.setText("")
        self.fecha_ins.setText("")
        self.label_6.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Fecha de inscripci\u00f3n(DD/MM/YYYY)", None))
        self.label_4.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Sexo", None))
        self.label_5.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Fecha de nacimiento(DD/MM/YYYY)", None))
        self.label_7.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CURP", None))
        self.curp.setText("")
        self.sexo.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"H", None))
        self.sexo.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"M", None))

        self.label.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Nombre(s)", None))
        self.label_3.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Apellido Materno", None))
        self.nombre.setText("")
        self.apellido_pat.setText("")
        self.apellido_mat.setText("")
        self.label_2.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Apellido Paterno", None))
        self.label_8.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Grado academico", None))
        self.label_9.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"\u00bfEsta inscrito?", None))
        self.label_10.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"\u00bfEs becado?", None))
        self.label_11.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Tipo de sangre", None))
        self.grado.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"PRIMERO", None))
        self.grado.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"SEGUNDO", None))
        self.grado.setItemText(2, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"TERCERO", None))
        self.grado.setItemText(3, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CUARTO", None))
        self.grado.setItemText(4, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"QUINTO", None))
        self.grado.setItemText(5, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"SEXTO", None))
        self.grado.setItemText(6, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"SEPTIMO", None))

        self.inscripcion.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No", None))
        self.inscripcion.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Si", None))

        self.beca.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No", None))
        self.beca.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Si", None))

        self.sangre.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"A+", None))
        self.sangre.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"A-", None))
        self.sangre.setItemText(2, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"B+", None))
        self.sangre.setItemText(3, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"B-", None))
        self.sangre.setItemText(4, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"AB+", None))
        self.sangre.setItemText(5, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"AB-", None))
        self.sangre.setItemText(6, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"O+", None))
        self.sangre.setItemText(7, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"O-", None))

        self.seguro.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No", None))
        self.seguro.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Si", None))

        self.label_12.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"\u00bfSu seguro esta activo?", None))
        self.carrera.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ENFERMERIA", None))
        self.carrera.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"NUTRICI\u00d3N", None))
        self.carrera.setItemText(2, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"LABORATORIO CLINICO", None))
        self.carrera.setItemText(3, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"MECANICA AUTOMOTRIZ", None))
        self.carrera.setItemText(4, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"PROGRAMACI\u00d3N WEB", None))
        self.carrera.setItemText(5, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ELECTRICISTA", None))
        self.carrera.setItemText(6, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"MECANICO ELECTRICO", None))
        self.carrera.setItemText(7, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"TURISMO", None))
        self.carrera.setItemText(8, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"DIBUJO INDUSTRIAL", None))
        self.carrera.setItemText(9, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"TRABAJO SOCIAL", None))
        self.carrera.setItemText(10, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"GASTRONOMIA", None))
        self.carrera.setItemText(11, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"SISTEMAS COMPUTACIONALES", None))
        self.carrera.setItemText(12, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ADMINISTRACI\u00d3N CONTABLE", None))
        self.carrera.setItemText(13, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"REHABILITACION CLINICA", None))
        self.carrera.setItemText(14, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"DISE\u00d1O DE IMAGEN", None))
        self.carrera.setItemText(15, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"INGLES", None))
        self.carrera.setItemText(16, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ACTIVIDAD FISICA Y DEPORTE", None))
        self.carrera.setItemText(17, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"DISE\u00d1O GRAFICO", None))
        self.carrera.setItemText(18, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"DIBUJO TECNICO", None))
        self.carrera.setItemText(19, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"LABORATORIO DENTAL", None))

        self.label_14.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"\u00bfEnfermedad cronica?", None))
        self.label_13.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"\u00bfDiscapacidad?", None))
        self.cronica.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No", None))
        self.cronica.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Si", None))

        self.label_15.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"N\u00famero de seguridad social", None))
        self.discapacidad.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No", None))
        self.discapacidad.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Si", None))

        self.NSS.setText("")
        self.label_17.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Carrera", None))
        self.CCT.setText("")
        self.label_18.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Ingrese el CCT de la escuela", None))
        self.label_21.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Codigo Postal", None))
        self.label_25.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Alcadia o Municipio", None))
        self.label_24.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No. Interior", None))
        self.label_22.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Calle", None))
        self.calle.setText("")
        self.label_23.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"No. Exterior", None))
        self.CP.setText("")
        self.label_20.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Colonia", None))
        self.interior.setText("")
        self.colonia.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Estado", None))
        self.exterior.setText("")
        self.alcaldia.setText("")
        self.estado.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ESTADO DE MEXICO", None))
        self.estado.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CIUDAD DE MEXICO", None))

        self.label_27.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Tutor</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Nombre(s)", None))
        self.label_29.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Apellido Materno", None))
        self.nombre_2.setText("")
        self.apellido_pat_tutor.setText("")
        self.apellido_mat_tutor.setText("")
        self.label_30.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Apellido Paterno", None))
        self.label_31.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Sexo", None))
        self.sexo_2.setItemText(0, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"H", None))
        self.sexo_2.setItemText(1, QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"M", None))

        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"SEXO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"FECHA DE NACIMIENTO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"FECHA DE INSCRIPCI\u00d3N", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CURP", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"GRADO ACADEMICO", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CARRERA", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"INSCRITO", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"BECADO", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"SEGURO", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"TIPO DE SANGRE", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"DISCAPACIDAD", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ENFERMEDADES CRONICAS", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"NUMERO DE SEGURO SOCIAL", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ESTADO", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"COLONIA", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"ALCALDIA", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CODIGO POSTAL", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"CALLE", None));
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"PLANTEL", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"NOMBRE TUTOR", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"APELLIDO PATERNO TUTOR", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"APELLIDO MATERNO TUTOR", None));
        self.label_32.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"Ingrese el curp:", None))
#if QT_CONFIG(tooltip)
        self.curp_nuevo.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.curp_nuevo.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.curp_nuevo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.curp_nuevo.setText("")
        self.label_33.setText(QCoreApplication.translate("Form_ACTUALIZAR_ALUMNO", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ACTUALIZAR ALUMNO</span></p><p><br/></p></body></html>", None))
    # retranslateUi

