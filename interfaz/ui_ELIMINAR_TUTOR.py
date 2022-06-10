# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ELIMINAR_TUTORMKpUyr.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import resources_rc_rc

class Ui_Form_ELIMINAR_TUTOR(object):
    def setupUi(self, Form_ELIMINAR_TUTOR):
        if not Form_ELIMINAR_TUTOR.objectName():
            Form_ELIMINAR_TUTOR.setObjectName(u"Form_ELIMINAR_TUTOR")
        Form_ELIMINAR_TUTOR.resize(912, 422)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_ELIMINAR_TUTOR.setWindowIcon(icon)
        Form_ELIMINAR_TUTOR.setStyleSheet(u"QWidget\n"
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
        self.eliminar = QPushButton(Form_ELIMINAR_TUTOR)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(770, 380, 131, 31))
        self.eliminar.setIcon(icon)
        self.eliminar.setIconSize(QSize(20, 20))
        self.label_27 = QLabel(Form_ELIMINAR_TUTOR)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(410, 30, 51, 31))
        self.layoutWidget_2 = QWidget(Form_ELIMINAR_TUTOR)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(230, 70, 413, 51))
        self.gridLayout_9 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.layoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_28.setFont(font)

        self.gridLayout_9.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_29 = QLabel(self.layoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

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
        self.label_30.setFont(font)

        self.gridLayout_9.addWidget(self.label_30, 0, 1, 1, 1)

        self.groupBox = QGroupBox(Form_ELIMINAR_TUTOR)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 130, 891, 231))
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        font1 = QFont()
        font1.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
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
        self.label_33 = QLabel(Form_ELIMINAR_TUTOR)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(360, 0, 161, 31))

        self.retranslateUi(Form_ELIMINAR_TUTOR)

        QMetaObject.connectSlotsByName(Form_ELIMINAR_TUTOR)
    # setupUi

    def retranslateUi(self, Form_ELIMINAR_TUTOR):
        Form_ELIMINAR_TUTOR.setWindowTitle(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"ELIMINAR TUTOR", None))
        self.eliminar.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"ELIMINAR", None))
        self.label_27.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Tutor</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"Nombre(s)", None))
        self.label_29.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"Apellido Materno", None))
        self.nombre_2.setText("")
        self.apellido_pat_tutor.setText("")
        self.apellido_mat_tutor.setText("")
        self.label_30.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"Apellido Paterno", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"APELLIDO PATERNO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"APELLIDO MATERNO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"SEXO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"COLONIA", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"CODIGO POSTAL", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"CALLE", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"NO.EXTERIOR", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"NO.INTERIOR", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"ALCALDIA", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"ESTADO", None));
        self.label_33.setText(QCoreApplication.translate("Form_ELIMINAR_TUTOR", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">ELIMINAR TUTOR</span></p><p><br/></p></body></html>", None))
    # retranslateUi

