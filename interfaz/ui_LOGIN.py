# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LOGINhDfKsZ.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import resources_rc_rc

class Ui_Form_LOGIN(object):
    def setupUi(self, Form_LOGIN):
        if not Form_LOGIN.objectName():
            Form_LOGIN.setObjectName(u"Form_LOGIN")
        Form_LOGIN.resize(314, 223)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/boton-actualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_LOGIN.setWindowIcon(icon)
        Form_LOGIN.setToolTipDuration(-1)
        Form_LOGIN.setStyleSheet(u"QWidget\n"
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
        self.conectar = QPushButton(Form_LOGIN)
        self.conectar.setObjectName(u"conectar")
        self.conectar.setGeometry(QRect(200, 180, 101, 31))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/recursos/iniciar-sesion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conectar.setIcon(icon1)
        self.conectar.setIconSize(QSize(20, 20))
        self.usuario = QLineEdit(Form_LOGIN)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(20, 100, 281, 22))
        self.label = QLabel(Form_LOGIN)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 121, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form_LOGIN)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 151, 16))
        self.label_2.setFont(font)
        self.contrasenia = QLineEdit(Form_LOGIN)
        self.contrasenia.setObjectName(u"contrasenia")
        self.contrasenia.setGeometry(QRect(20, 150, 281, 22))
        self.label_3 = QLabel(Form_LOGIN)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 10, 61, 61))
        self.label_3.setStyleSheet(u"border-image: url(:/iconos/recursos/usuario.png);")

        self.retranslateUi(Form_LOGIN)

        QMetaObject.connectSlotsByName(Form_LOGIN)
    # setupUi

    def retranslateUi(self, Form_LOGIN):
        Form_LOGIN.setWindowTitle(QCoreApplication.translate("Form_LOGIN", u"LOGIN", None))
#if QT_CONFIG(tooltip)
        Form_LOGIN.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Form_LOGIN.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.conectar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.conectar.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.conectar.setText(QCoreApplication.translate("Form_LOGIN", u"CONECTAR", None))
        self.label.setText(QCoreApplication.translate("Form_LOGIN", u"INGRESE EL USUARIO:", None))
        self.label_2.setText(QCoreApplication.translate("Form_LOGIN", u"INGRESE LA CONTRASE\u00d1A:", None))
        self.label_3.setText("")
    # retranslateUi

