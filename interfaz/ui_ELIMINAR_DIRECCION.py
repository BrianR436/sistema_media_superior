# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ELIMINAR_DIRECCIONebgtPr.ui'
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

class Ui_Form_ELIMINAR_DIRECCION(object):
    def setupUi(self, Form_ELIMINAR_DIRECCION):
        if not Form_ELIMINAR_DIRECCION.objectName():
            Form_ELIMINAR_DIRECCION.setObjectName(u"Form_ELIMINAR_DIRECCION")
        Form_ELIMINAR_DIRECCION.resize(912, 563)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ELIMINAR_DIRECCION.setWindowIcon(icon)
        Form_ELIMINAR_DIRECCION.setStyleSheet(u"QWidget\n"
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
        self.insertar = QPushButton(Form_ELIMINAR_DIRECCION)
        self.insertar.setObjectName(u"insertar")
        self.insertar.setGeometry(QRect(320, 60, 131, 41))
        self.insertar.setIcon(icon)
        self.insertar.setIconSize(QSize(20, 20))
        self.groupBox = QGroupBox(Form_ELIMINAR_DIRECCION)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 110, 891, 411))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tabla = QTableWidget(self.groupBox)
        if (self.tabla.columnCount() < 6):
            self.tabla.setColumnCount(6)
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
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(0, 0, 891, 411))
        self.tabla.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tabla.horizontalHeader().setDefaultSectionSize(155)
        self.label = QLabel(Form_ELIMINAR_DIRECCION)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 291, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.curp = QLineEdit(Form_ELIMINAR_DIRECCION)
        self.curp.setObjectName(u"curp")
        self.curp.setGeometry(QRect(10, 70, 221, 31))
        self.label_34 = QLabel(Form_ELIMINAR_DIRECCION)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(360, 10, 211, 31))

        self.retranslateUi(Form_ELIMINAR_DIRECCION)

        QMetaObject.connectSlotsByName(Form_ELIMINAR_DIRECCION)
    # setupUi

    def retranslateUi(self, Form_ELIMINAR_DIRECCION):
        Form_ELIMINAR_DIRECCION.setWindowTitle(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"ELIMINAR DIRECCION", None))
        self.insertar.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"ELIMINAR", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"ID", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"ESTADO", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"COLONIA", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"ALCALDIA", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"CODIGO POSTAL", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"CALLE", None));
        self.label.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"INGRESA EL ID DE LA DIRECCION A ELIMINAR:", None))
        self.label_34.setText(QCoreApplication.translate("Form_ELIMINAR_DIRECCION", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ELIMINAR DIRECCI\u00d3N</span></p><p><br/></p></body></html>", None))
    # retranslateUi

