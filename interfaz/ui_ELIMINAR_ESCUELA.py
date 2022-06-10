# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ELIMINAR_ESCUELAHpmLGm.ui'
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

class Ui_Form_ELIMINAR_ESCUELA(object):
    def setupUi(self, Form_ELIMINAR_ESCUELA):
        if not Form_ELIMINAR_ESCUELA.objectName():
            Form_ELIMINAR_ESCUELA.setObjectName(u"Form_ELIMINAR_ESCUELA")
        Form_ELIMINAR_ESCUELA.resize(912, 386)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ELIMINAR_ESCUELA.setWindowIcon(icon)
        Form_ELIMINAR_ESCUELA.setStyleSheet(u"QWidget\n"
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
        self.eliminar = QPushButton(Form_ELIMINAR_ESCUELA)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(270, 50, 131, 41))
        self.eliminar.setIcon(icon)
        self.eliminar.setIconSize(QSize(20, 20))
        self.label_16 = QLabel(Form_ELIMINAR_ESCUELA)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 0, 181, 31))
        self.groupBox = QGroupBox(Form_ELIMINAR_ESCUELA)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 100, 891, 231))
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
        self.label = QLabel(Form_ELIMINAR_ESCUELA)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 33, 261, 16))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.CCT = QLineEdit(Form_ELIMINAR_ESCUELA)
        self.CCT.setObjectName(u"CCT")
        self.CCT.setGeometry(QRect(13, 55, 251, 31))

        self.retranslateUi(Form_ELIMINAR_ESCUELA)

        QMetaObject.connectSlotsByName(Form_ELIMINAR_ESCUELA)
    # setupUi

    def retranslateUi(self, Form_ELIMINAR_ESCUELA):
        Form_ELIMINAR_ESCUELA.setWindowTitle(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"ELIMINAR ESCUELA", None))
        self.eliminar.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"ELIMINAR", None))
        self.label_16.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ELIMINAR ESCUELA</span></p><p><br/></p></body></html>", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"CCT", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"INSTITUCI\u00d3N", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"PLANTEL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"TELEFONO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"WEB", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"CORREO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"DOMINIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"COLONIA", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"CODIGO POSTAL", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"CALLE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"NO.INTERIOR", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"NO.EXTERIOR", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"ALCALDIA", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"ESTADO", None));
        self.label.setText(QCoreApplication.translate("Form_ELIMINAR_ESCUELA", u"INGRESE EL CCT DE LA ESCUELA A ELIMINAR:", None))
        self.CCT.setText("")
    # retranslateUi

