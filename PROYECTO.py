
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox, QTableWidget, QTableWidgetItem, QMdiArea,QMdiSubWindow
from interfaz.ui_mainwindow import Ui_mainwindow
from interfaz.ui_INSERTAR_ALUMNO import Ui_Form
from interfaz.ui_ELIMINAR_ALUMNO import Ui_Form1
from interfaz.ui_ACTUALIZAR_ALUMNO import Ui_Form_ACTUALIZAR_ALUMNO
from interfaz.ui_CONSULTAR_ALUMNO import Ui_Form_CONSULTAR_ALUMNO
from interfaz.ui_INSERTAR_DIRECCION import Ui_Form_INSERTAR_DIRECCION
from interfaz.ui_ELIMINAR_DIRECCION import Ui_Form_ELIMINAR_DIRECCION
from interfaz.ui_ACTUALIZAR_DIRECCION import Ui_Form_ACTUALIZAR_DIRECCION
from interfaz.ui_CONSULTAR_DIRECCION import Ui_Form_CONSULTAR_DIRECCION
from interfaz.ui_INSERTAR_TUTOR import Ui_Form_INSERTAR_TUTOR
from interfaz.ui_ELIMINAR_TUTOR import Ui_Form_ELIMINAR_TUTOR
from interfaz.ui_ACTUALIZAR_TUTOR import Ui_Form_ACTUALIZAR_TUTOR
from interfaz.ui_CONSULTAR_TUTOR import Ui_Form_CONSULTAR_TUTOR
from interfaz.ui_INSERTAR_ESCUELA import Ui_Form_INSERTAR_ESCUELA
from interfaz.ui_ELIMINAR_ESCUELA import Ui_Form_ELIMINAR_ESCUELA
from interfaz.ui_ACTUALIZAR_ESCUELA import Ui_Form_ACTUALIZAR_ESCUELA
from interfaz.ui_CONSULTAR_ESCUELA import Ui_Form_CONSULTAR_ESCUELA
from qt_material import apply_stylesheet
import sys

import cx_Oracle
try:
    connection = cx_Oracle.connect(
    user = 'USR_ADMIN',
    password = 'CULHUACAN_38',
    dsn = 'localhost:1521/XEPDB1',
    encoding = 'UTF-8'
    )
    print(connection.version)
except Exception as ex:
    print(ex)

class MainWindow(QMainWindow,Ui_mainwindow,Ui_Form,Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #DISPARADORES PARA ALUMNO
        self.actionINSERTAR.triggered.connect(self.abrir_INSERTAR_ALUMNO)
        self.insertar_a.clicked.connect(self.abrir_INSERTAR_ALUMNO)
        self.actionELIMINAR.triggered.connect(self.abrir_ELIMINAR_ALUMNO)
        self.eliminar_a.clicked.connect(self.abrir_ELIMINAR_ALUMNO)
        self.actionACTUALIZAR.triggered.connect(self.abrir_ACTUALIZAR_ALUMNO)
        self.actualizar_a.clicked.connect(self.abrir_ACTUALIZAR_ALUMNO)
        self.actionCONSULTAR.triggered.connect(self.abrir_CONSULTAR_ALUMNO)
        self.consultar_a.clicked.connect(self.abrir_CONSULTAR_ALUMNO)
        #DISPARADORES PARA DIRECCION
        self.actionINSERTAR_4.triggered.connect(self.abrir_INSERTAR_DIRECCION)
        self.insertar_d.clicked.connect(self.abrir_INSERTAR_DIRECCION)
        self.actionELIMINAR_4.triggered.connect(self.abrir_ELIMINAR_DIRECCION)
        self.eliminar_d.clicked.connect(self.abrir_ELIMINAR_DIRECCION)
        self.actionACTUALIZAR_4.triggered.connect(self.abrir_ACTUALIZAR_DIRECCION)
        self.actualizar_d.clicked.connect(self.abrir_ACTUALIZAR_DIRECCION)
        self.actionCONSULTAR_4.triggered.connect(self.abrir_CONSULTAR_DIRECCION)
        self.consultar_d.clicked.connect(self.abrir_CONSULTAR_DIRECCION)
        #DISPARADORES PARA TUTOR
        self.actionINSERTAR_2.triggered.connect(self.abrir_INSERTAR_TUTOR)
        self.insertar_t.clicked.connect(self.abrir_INSERTAR_TUTOR)
        self.actionELIMINAR_2.triggered.connect(self.abrir_INSERTAR_TUTOR)
        self.eliminar_t.clicked.connect(self.abrir_ELIMINAR_TUTOR)
        self.actionACTUALIZAR_2.triggered.connect(self.abrir_ACTUALIZAR_TUTOR)
        self.actualizar_t.clicked.connect(self.abrir_ACTUALIZAR_TUTOR)
        self.actionCONSULTAR_2.triggered.connect(self.abrir_CONSULTAR_TUTOR)
        self.consultar_t.clicked.connect(self.abrir_CONSULTAR_TUTOR)
        #DISPARADORES PARA ESCUELA
        self.actionINSERTAR_3.triggered.connect(self.abrir_INSERTAR_ESCUELA)
        self.insertar_e.clicked.connect(self.abrir_INSERTAR_ESCUELA)
        self.actionELIMINAR_3.triggered.connect(self.abrir_ELIMINAR_ESCUELA)
        self.eliminar_e.clicked.connect(self.abrir_ELIMINAR_ESCUELA)
        self.actionACTUALIZAR_3.triggered.connect(self.abrir_ACTUALIZAR_ESCUELA)
        self.actualizar_e.clicked.connect(self.abrir_ACTUALIZAR_ESCUELA)
        self.actionCONSULTAR_3.triggered.connect(self.abrir_CONSULTAR_ESCUELA)
        self.consultar_e.clicked.connect(self.abrir_CONSULTAR_ESCUELA)


    def abrir_INSERTAR_ALUMNO (self):
        self.ventana = QMainWindow()
        self.IS = Ui_Form()
        self.IS.setupUi(self.ventana)
        self.ventana.show()
        self.mostrar_ALUMNO()
        self.IS.insertar.clicked.connect(self.insertar_ALUMNO)
        
    def abrir_ELIMINAR_ALUMNO (self):
        self.ventana = QMainWindow()
        self.EL = Ui_Form1()
        self.EL.setupUi(self.ventana)
        self.ventana.show()
        self.mostrar_ALUMNO_E()
        self.EL.insertar.clicked.connect(self.eliminar_ALUMNO)

    def abrir_ACTUALIZAR_ALUMNO (self):
        self.ventana = QMainWindow()
        self.IS = Ui_Form_ACTUALIZAR_ALUMNO()
        self.IS.setupUi(self.ventana)
        self.ventana.show()
        self.mostrar_ALUMNO()
        self.IS.actualizar.clicked.connect(self.actualizar_ALUMNO)    
     
    def abrir_CONSULTAR_ALUMNO(self):
        self.ventana = QMainWindow()
        self.CO = Ui_Form_CONSULTAR_ALUMNO()
        self.CO.setupUi(self.ventana)
        self.ventana.show()
        self.CO.consultar.clicked.connect(self.consultar_ALUMNO) 

    def abrir_INSERTAR_DIRECCION(self):
        self.ventana = QMainWindow()
        self.ID = Ui_Form_INSERTAR_DIRECCION()
        self.ID.setupUi(self.ventana)
        self.ventana.show()
        self.ID.insertar.clicked.connect(self.insertar_DIRECCION)
        self.mostrar_DIRECCION()

    def abrir_ELIMINAR_DIRECCION(self):
        self.ventana = QMainWindow()
        self.ED = Ui_Form_ELIMINAR_DIRECCION()
        self.ED.setupUi(self.ventana)
        self.ventana.show()
        self.ED.insertar.clicked.connect(self.eliminar_DIRECCION)
        self.mostrar_DIRECCION_ELIMINAR()
    
    def abrir_ACTUALIZAR_DIRECCION(self):
        self.ventana = QMainWindow()
        self.ED = Ui_Form_ACTUALIZAR_DIRECCION()
        self.ED.setupUi(self.ventana)
        self.ventana.show()
        self.ED.insertar.clicked.connect(self.actualizar_DIRECCION)
        self.mostrar_DIRECCION_ELIMINAR()
    
    def abrir_CONSULTAR_DIRECCION(self):
        self.ventana = QMainWindow()
        self.CD = Ui_Form_CONSULTAR_DIRECCION()
        self.CD.setupUi(self.ventana)
        self.ventana.show()
        self.CD.consultar.clicked.connect(self.consultar_DIRECCION)      

    def abrir_INSERTAR_TUTOR(self):
        self.ventana = QMainWindow()
        self.IT = Ui_Form_INSERTAR_TUTOR()
        self.IT.setupUi(self.ventana)
        self.ventana.show()
        self.IT.insertar.clicked.connect(self.insertar_TUTOR)
        self.mostrar_TUTOR()

    def abrir_ELIMINAR_TUTOR(self):
        self.ventana = QMainWindow()
        self.IT = Ui_Form_ELIMINAR_TUTOR()
        self.IT.setupUi(self.ventana)
        self.ventana.show()
        self.IT.eliminar.clicked.connect(self.eliminar_TUTOR)
        self.mostrar_TUTOR() 
    
    def abrir_ACTUALIZAR_TUTOR(self):
        self.ventana = QMainWindow()
        self.AT = Ui_Form_ACTUALIZAR_TUTOR()
        self.AT.setupUi(self.ventana)
        self.ventana.show()
        self.AT.actualizar.clicked.connect(self.actualizar_TUTOR)
        self.mostrar_TUTOR_a() 
    
    def abrir_CONSULTAR_TUTOR(self):
        self.ventana = QMainWindow()
        self.CT = Ui_Form_CONSULTAR_TUTOR()
        self.CT.setupUi(self.ventana)
        self.ventana.show()
        self.CT.consultar.clicked.connect(self.consultar_TUTOR) 

    def abrir_INSERTAR_ESCUELA(self):
        self.ventana = QMainWindow()
        self.IE = Ui_Form_INSERTAR_ESCUELA()
        self.IE.setupUi(self.ventana)
        self.ventana.show()
        self.IE.insertar.clicked.connect(self.insertar_ESCUELA)    
        self.mostrar_ESCUELA()

    def abrir_ELIMINAR_ESCUELA(self):
        self.ventana = QMainWindow()
        self.IE = Ui_Form_ELIMINAR_ESCUELA()
        self.IE.setupUi(self.ventana)
        self.ventana.show()
        self.IE.eliminar.clicked.connect(self.eliminar_ESCUELA)    
        self.mostrar_ESCUELA()

    def abrir_ACTUALIZAR_ESCUELA(self):
        self.ventana = QMainWindow()
        self.IE = Ui_Form_ACTUALIZAR_ESCUELA()
        self.IE.setupUi(self.ventana)
        self.ventana.show()
        self.IE.actualizar.clicked.connect(self.actualizar_ESCUELA)    
        self.mostrar_ESCUELA()
    
    def abrir_CONSULTAR_ESCUELA(self):
        self.ventana = QMainWindow()
        self.CE = Ui_Form_CONSULTAR_ESCUELA()
        self.CE.setupUi(self.ventana)
        self.ventana.show()
        self.CE.consultar.clicked.connect(self.consultar_ESCUELA)    

#FUNCIONES PARA LA BASE DE DATOS
    #FUNCIONES PARA ALUMNO   
    def insertar_ALUMNO(self):
        try:
            cursor1 = connection.cursor()
            cursor11 = connection.cursor()
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()  
            cursor4 = connection.cursor()             
            cursor5 = connection.cursor()
            cursor7 = connection.cursor()
            cursor8 = connection.cursor()
            sql = '''SELECT SUBSTR(ALM_ID,4,2) FROM ALUMNO'''
            cursor1.execute(sql)
            numero = cursor1.fetchall()
            id = max(numero)
            ID= "A00"+str(int(id[0]) +1)
            cursor1.close()
            nombre_alumno = self.IS.nombre.text()
            apellido_alumno = self.IS.apellido_pat.text()
            apellido2_alumno = self.IS.apellido_mat.text()
            sexo = self.IS.sexo.currentText()
            fecha_de_nacimiento = self.IS.fecha_na.text()
            fecha_de_inscripcion = self.IS.fecha_ins.text()
            curp = self.IS.curp.text()
            grado_academico = self.IS.grado.currentText()
            inscripcion = str(self.IS.inscripcion.currentIndex())
            beca = str(self.IS.beca.currentIndex())
            tipo_sangre = self.IS.sangre.currentText()
            seguro = str(self.IS.seguro.currentIndex())
            discapacidad = self.IS.discapacidad.currentText()
            enfermedad = self.IS.cronica.currentText()
            nss=self.IS.NSS.text()
            #CONEXION CON TABLA DE DIRECCIÓN
            sql = '''SELECT SUBSTR(DIR_ID,4,2) FROM DIRECCION'''
            cursor11.execute(sql)
            numero = cursor11.fetchall()
            id = max(numero)
            ID_DIRECCION= "DIR"+str(int(id[0])+ 1)
            cursor11.close()
            Colonia = self.IS.colonia.text()
            Postal = self.IS.CP.text()
            Calle = self.IS.calle.text()
            Interior = self.IS.interior.text()
            Exterior = self.IS.exterior.text()
            Alcaldia = self.IS.alcaldia.text()
            Estado = self.IS.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()
            sql = '''INSERT INTO DIRECCION VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(ID_DIRECCION,Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO)
            cursor7.execute(sql) 
            connection.commit()
            cursor7.close()
            #CIERRO CONEXION DE TABLA DIRECCIÓN
            escuela = self.IS.CCT.text()
            #CONEXION CON TABLA TUTOR
            cursor4 = connection.cursor()
            cursor8 = connection.cursor()
            sql = '''SELECT SUBSTR(TTR_ID,4,2) FROM TUTOR'''
            cursor4.execute(sql)
            numero = cursor4.fetchall()
            id = max(numero)
            ID_TUTOR= "T00"+str(int(id[0]) +1)
            cursor4.close()
            nombre = self.IS.nombre_2.text()
            apellido = self.IS.apellido_pat_tutor.text()
            apellido2 = self.IS.apellido_mat_tutor.text()
            sexo = self.IS.sexo_2.currentText()
            sql = '''INSERT INTO TUTOR VALUES ('{}','{}','{}','{}','{}','{}')'''.format(ID_TUTOR,nombre,apellido,apellido2,sexo,ID_DIRECCION)
            cursor8.execute(sql) 
            connection.commit()
            cursor8.close()       
            #CIERRO CONEXION CON TABLA TUTOR
            #INICIO CONEXION CON TABLA CARRERA
            carrera = self.IS.carrera.currentText()
            sql = '''SELECT CAR_ID FROM CARRERA WHERE UPPER(CAR_NOMBRE_CARRERA) LIKE UPPER('{}')'''.format(carrera)
            cursor5.execute(sql)
            CAR = cursor5.fetchone()
            CAR_ID = str(CAR[0])
            cursor5.close()
            #CIERRO CONEXION CON TABLA CARRERA
            sql = '''INSERT INTO ALUMNO VALUES('{}','{}','{}','{}','{}',to_date('{}','DD-MM-YYYY'),to_date('{}','DD-MM-YYYY'),
            '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(ID,nombre_alumno,apellido_alumno,apellido2_alumno,sexo,fecha_de_nacimiento,fecha_de_inscripcion,curp,
            grado_academico,inscripcion,beca,seguro,tipo_sangre,discapacidad,enfermedad,nss,ID_DIRECCION,escuela,ID_TUTOR,CAR_ID)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            self.mostrar_ALUMNO()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Falta algún dato por llenar ó "+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()    
    
    def eliminar_ALUMNO(self):
        try:   
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            curp = self.EL.curp.text()
            activa = 1
            if curp == '':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("No se ingreso el curp")
                msg.setWindowTitle("ERROR")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec() 
                activa = 0
            sql = '''SELECT ALM_ID FROM ALUMNO WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
            cursor3.execute(sql)
            ide = cursor3.fetchone()
            ID = ide[0]
            cursor3.close()
            sql= '''DELETE FROM GRUPO WHERE UPPER(GRP_ALUMNO_ID) LIKE UPPER('{}')'''.format(ID)
            cursor2.execute(sql) 
            connection.commit()
            cursor2.close()
            sql = '''DELETE FROM ALUMNO WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            if activa == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
                msg.setWindowTitle("EXITOSO")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No se puede borrar alumno \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()  
    
    def actualizar_ALUMNO(self):
        try:    
            cursor = connection.cursor()
            cursor1 = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            cursor5 = connection.cursor()
            cursor6 = connection.cursor()
            cursor7 = connection.cursor()
            cursor8 = connection.cursor()
            curp = self.IS.curp_nuevo.text()

            nuevo_nombre = self.IS.nombre.text()
            nuevo_apellido = self.IS.apellido_pat.text()
            nuevo_apellido2 = self.IS.apellido_mat.text()
            nuevo_sexo = self.IS.sexo.currentText()
            fecha_de_nacimiento = self.IS.fecha_na.text()
            fecha_de_inscripcion = self.IS.fecha_ins.text()
            curp_nuevo = self.IS.curp.text()
            
            grado_academico = self.IS.grado.currentText()
            inscripcion = str(self.IS.inscripcion.currentIndex())
            beca = str(self.IS.beca.currentIndex())
            tipo_sangre = self.IS.sangre.currentText()
            seguro = str(self.IS.seguro.currentIndex())
            discapacidad = self.IS.discapacidad.currentText()
            enfermedad = self.IS.cronica.currentText()
            nss=self.IS.NSS.text()
            #CONEXION CON LA TABLA DE DIRECCION PARA ACTUALIZAR
            sql = '''SELECT ALM_DIRECCION_ID FROM ALUMNO WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
            cursor1.execute(sql)
            numero = cursor1.fetchone()
            ID= str(numero[0])
            
            cursor1.close()
            
            Colonia = self.IS.colonia.text()
            Postal = self.IS.CP.text()
            Calle = self.IS.calle.text()
            Interior = self.IS.interior.text()
            Exterior = self.IS.exterior.text()
            Alcaldia = self.IS.alcaldia.text()
            Estado = self.IS.estado.currentText()
            
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            print(ESTADO)
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            print(ALCALDIA)
            cursor3.close()
            sql = '''UPDATE DIRECCION SET DIR_COLONIA = '{}', DIR_CP = '{}', DIR_CALLE = '{}', DIR_NO_EXTERIOR = '{}', DIR_NO_INTERIOR = '{}', 
                    DIR_ALCALDIA_ID = '{}', DIR_ESTADO_ID = '{}'
                    WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO,ID)
            cursor4.execute(sql)
            connection.commit()
            cursor4.close()
            #TERMINO CONEXION
        
            escuela = self.IS.CCT.text()

            #CONEXION CON TABLA TUTOR
            sql = '''SELECT ALM_TUTOR_ID FROM ALUMNO WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
            cursor7.execute(sql)
            numero = cursor7.fetchone()
            ID_TUTOR1= str(numero[0])
            cursor7.close()

            nombre_t = self.IS.nombre_2.text()
            apellido_pat = self.IS.apellido_pat_tutor.text()
            apellido_mat = self.IS.apellido_mat_tutor.text()
            sexo = self.IS.sexo_2.currentText()
            sql = '''UPDATE TUTOR SET TTR_NOMBRE ='{}', TTR_APELLIDO_PAT = '{}', TTR_APELLIDO_MAT = '{}', TTR_SEXO = '{}' 
                    WHERE UPPER(TTR_ID) LIKE UPPER('{}')'''.format(nombre_t,apellido_pat,apellido_mat,sexo,ID_TUTOR1)
            cursor5.execute(sql)
            connection.commit()
            cursor5.close()
            #CIERRO CONEXION CON TABLA TUTOR

            #INICIO CONEXION CON TABLA CARRERA
            sql = '''SELECT ALM_CARRERA_ID FROM ALUMNO WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
            cursor8.execute(sql)
            numero = cursor8.fetchone()
            ID_CARRERA1= str(numero[0])
            cursor8.close()

            carrera = self.IS.carrera.currentText()
            
            sql = '''SELECT CAR_ID FROM CARRERA WHERE UPPER(CAR_NOMBRE_CARRERA) LIKE UPPER('{}')'''.format(carrera)
            cursor6.execute(sql)
            CAR = cursor6.fetchone()
            CAR_ID = str(CAR[0])
            cursor6.close()
            
            #CIERRO CONEXION CON TABLA CARRERA
            if CAR_ID == ID_CARRERA1:
                sql = '''UPDATE ALUMNO SET ALM_NOMBRE='{}',ALM_APELLIDO_PAT='{}',ALM_APELLIDO_MAT='{}',ALM_SEXO='{}',ALM_FECHA_NACIMIENTO=to_date('{}','DD-MM-YYYY'),ALM_FECHA_INS=to_date('{}','DD-MM-YYYY'),
                        ALM_CURP='{}',ALM_GRADO_ACADEMICO='{}',ALM_ESTATUS_INS='{}',ALM_BECADO='{}',ALM_ESTATUS_SEGURO='{}',ALM_TIPO_SANGRE='{}',ALM_DISCAPACIDAD='{}',ALM_ENFERMEDADES='{}',ALM_NSS='{}',ALM_ESCUELA_ID='{}'
                        WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(nuevo_nombre,nuevo_apellido,nuevo_apellido2,nuevo_sexo,fecha_de_nacimiento,fecha_de_inscripcion,curp_nuevo,
                grado_academico,inscripcion,beca,seguro,tipo_sangre,discapacidad,enfermedad,nss,escuela,curp)
                cursor.execute(sql) 
                connection.commit()
                cursor.close()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
                msg.setWindowTitle("EXITOSO")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec()
            else:
                sql = '''UPDATE ALUMNO SET ALM_NOMBRE='{}',ALM_APELLIDO_PAT='{}',ALM_APELLIDO_MAT='{}',ALM_SEXO='{}',ALM_FECHA_NACIMIENTO=to_date('{}','DD-MM-YYYY'),ALM_FECHA_INS=to_date('{}','DD-MM-YYYY'),
                ALM_CURP='{}',ALM_GRADO_ACADEMICO='{}',ALM_ESTATUS_INS='{}',ALM_BECADO='{}',ALM_ESTATUS_SEGURO='{}',ALM_TIPO_SANGRE='{}',ALM_DISCAPACIDAD='{}',ALM_ENFERMEDADES='{}',ALM_NSS='{}',ALM_ESCUELA_ID='{}'
                ,ALM_CARRERA_ID='{}' WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(nuevo_nombre,nuevo_apellido,nuevo_apellido2,nuevo_sexo,fecha_de_nacimiento,fecha_de_inscripcion,curp_nuevo,
                grado_academico,inscripcion,beca,seguro,tipo_sangre,discapacidad,enfermedad,nss,escuela,CAR_ID,curp)
                cursor.execute(sql) 
                connection.commit()
                cursor.close()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
                msg.setWindowTitle("EXITOSO")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ingreso el CURP o Faltan datos \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()  
   
    def consultar_ALUMNO(self):
        try:
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            cursor5 = connection.cursor()
            curp = self.CO.curp.text()
            sql = '''SELECT ALM_NOMBRE, ALM_APELLIDO_PAT, ALM_APELLIDO_MAT,ALM_SEXO,ALM_FECHA_NACIMIENTO,ALM_FECHA_INS,ALM_CURP,ALM_GRADO_ACADEMICO,
                    CAR_NOMBRE_CARRERA,ALM_ESTATUS_INS,ALM_BECADO,ESC_PLANTEL
                    FROM ALUMNO
                    JOIN DIRECCION ON ALUMNO.ALM_DIRECCION_ID = DIRECCION.DIR_ID
                    JOIN ESCUELA ON ALUMNO.ALM_ESCUELA_ID = ESCUELA.ESC_CCT
                    JOIN TUTOR ON ALUMNO.ALM_TUTOR_ID = TUTOR.TTR_ID
                    JOIN CARRERA ON ALUMNO.ALM_CARRERA_ID = CARRERA.CAR_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                    WHERE UPPER(ALM_CURP) LIKE ('{}') '''.format(curp)
            cursor.execute(sql)
            impresion = cursor.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CO.DATOS.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CO.DATOS.setItem(i,n,texto)
            sql = '''SELECT ALM_NSS,ALM_ESTATUS_SEGURO,ALM_TIPO_SANGRE,ALM_ENFERMEDADES,ALM_DISCAPACIDAD
                    FROM ALUMNO
                    JOIN DIRECCION ON ALUMNO.ALM_DIRECCION_ID = DIRECCION.DIR_ID
                    JOIN ESCUELA ON ALUMNO.ALM_ESCUELA_ID = ESCUELA.ESC_CCT
                    JOIN TUTOR ON ALUMNO.ALM_TUTOR_ID = TUTOR.TTR_ID
                    JOIN CARRERA ON ALUMNO.ALM_CARRERA_ID = CARRERA.CAR_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                    WHERE UPPER(ALM_CURP) LIKE ('{}') '''.format(curp)
            cursor2.execute(sql)
            impresion = cursor2.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CO.MEDICOS.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CO.MEDICOS.setItem(i,n,texto)
            cursor2.close()

            sql = '''SELECT EST_ESTADO,DIR_COLONIA,ALC_ALCALDIA,DIR_CP,DIR_CALLE,DIR_NO_EXTERIOR,DIR_NO_INTERIOR
                    FROM ALUMNO
                    JOIN DIRECCION ON ALUMNO.ALM_DIRECCION_ID = DIRECCION.DIR_ID
                    JOIN ESCUELA ON ALUMNO.ALM_ESCUELA_ID = ESCUELA.ESC_CCT
                    JOIN TUTOR ON ALUMNO.ALM_TUTOR_ID = TUTOR.TTR_ID
                    JOIN CARRERA ON ALUMNO.ALM_CARRERA_ID = CARRERA.CAR_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID 
                    WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
            cursor3.execute(sql)
            impresion = cursor3.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CO.DIRECCION.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CO.DIRECCION.setItem(i,n,texto)

            cursor3.close()

            sql = '''SELECT TTR_NOMBRE,TTR_APELLIDO_PAT,TTR_APELLIDO_MAT
                    FROM ALUMNO
                    JOIN DIRECCION ON ALUMNO.ALM_DIRECCION_ID = DIRECCION.DIR_ID
                    JOIN ESCUELA ON ALUMNO.ALM_ESCUELA_ID = ESCUELA.ESC_CCT
                    JOIN TUTOR ON ALUMNO.ALM_TUTOR_ID = TUTOR.TTR_ID
                    JOIN CARRERA ON ALUMNO.ALM_CARRERA_ID = CARRERA.CAR_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID 
                    WHERE UPPER(ALM_CURP) LIKE ('{}')'''.format(curp)
            cursor4.execute(sql)
            impresion = cursor4.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CO.TUTOR.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CO.TUTOR.setItem(i,n,texto)

            cursor4.close()

            sql = '''SELECT MAT_MATERIAS,GRP_CALIFICACION
                    FROM GRUPO
                    JOIN ALUMNO ON GRUPO.GRP_ALUMNO_ID = ALUMNO.ALM_ID
                    JOIN MATERIA ON GRUPO.GRP_MATERIA_ID = MATERIA.MAT_ID
                    WHERE UPPER(ALM_CURP) LIKE ('{}')'''.format(curp)
            cursor5.execute(sql)
            impresion = cursor5.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CO.CALIFICACION.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CO.CALIFICACION.setItem(i,n,texto)

            cursor5.close()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ingreso el CURP \n ó \n no se encontro el alumno con el CURP: "+ curp)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()

    def mostrar_ALUMNO(self):
        cursor = connection.cursor()
        sql = '''SELECT ALM_NOMBRE, ALM_APELLIDO_PAT, ALM_APELLIDO_MAT,ALM_SEXO,ALM_FECHA_NACIMIENTO,ALM_FECHA_INS,ALM_CURP,ALM_GRADO_ACADEMICO,CAR_NOMBRE_CARRERA
                ,ALM_ESTATUS_INS,ALM_BECADO,ALM_ESTATUS_SEGURO,ALM_TIPO_SANGRE,ALM_DISCAPACIDAD,ALM_ENFERMEDADES,ALM_NSS,EST_ESTADO
                ,DIR_COLONIA,ALC_ALCALDIA,DIR_CP,DIR_CALLE,ESC_PLANTEL,TTR_NOMBRE,TTR_APELLIDO_PAT,TTR_APELLIDO_MAT
                FROM ALUMNO
                JOIN DIRECCION ON ALUMNO.ALM_DIRECCION_ID = DIRECCION.DIR_ID
                JOIN ESCUELA ON ALUMNO.ALM_ESCUELA_ID = ESCUELA.ESC_CCT
                JOIN TUTOR ON ALUMNO.ALM_TUTOR_ID = TUTOR.TTR_ID
                JOIN CARRERA ON ALUMNO.ALM_CARRERA_ID = CARRERA.CAR_ID
                JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID'''
        cursor.execute(sql)
        impresion = cursor.fetchall()
        valor1 = int(len(impresion))
        valor2 = int(len(impresion[0]))
    
        for i in range(valor1):
            self.IS.tableWidget.insertRow(i)
            for n in range(valor2):
                t = str(impresion[i][n])
                texto = QTableWidgetItem(t)
                self.IS.tableWidget.setItem(i,n,texto)
                
        cursor.close()
    
    def mostrar_ALUMNO_E(self):
        
        cursor = connection.cursor()
        
        sql = '''SELECT ALM_NOMBRE, ALM_APELLIDO_PAT, ALM_APELLIDO_MAT,ALM_SEXO,ALM_FECHA_NACIMIENTO,ALM_FECHA_INS,ALM_CURP,ALM_GRADO_ACADEMICO,CAR_NOMBRE_CARRERA
                ,ALM_ESTATUS_INS,ALM_BECADO,ALM_ESTATUS_SEGURO,ALM_TIPO_SANGRE,ALM_DISCAPACIDAD,ALM_ENFERMEDADES,ALM_NSS,EST_ESTADO
                ,DIR_COLONIA,ALC_ALCALDIA,DIR_CP,DIR_CALLE,ESC_PLANTEL,TTR_NOMBRE,TTR_APELLIDO_PAT,TTR_APELLIDO_MAT
                FROM ALUMNO
                JOIN DIRECCION ON ALUMNO.ALM_DIRECCION_ID = DIRECCION.DIR_ID
                JOIN ESCUELA ON ALUMNO.ALM_ESCUELA_ID = ESCUELA.ESC_CCT
                JOIN TUTOR ON ALUMNO.ALM_TUTOR_ID = TUTOR.TTR_ID
                JOIN CARRERA ON ALUMNO.ALM_CARRERA_ID = CARRERA.CAR_ID
                JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID'''
        cursor.execute(sql)
        impresion = cursor.fetchall()
        
        valor1 = int(len(impresion))
        valor2 = int(len(impresion[0]))

        for i in range(valor1):
            self.EL.tablaeliminar.insertRow(i)
            for n in range(valor2):
                t = str(impresion[i][n])
                texto = QTableWidgetItem(t)
                self.EL.tablaeliminar.setItem(i,n,texto)
        cursor.close()
   
    #FUNCIONES PARA TUTOR
    def insertar_TUTOR(self):
        try:
            cursor1 = connection.cursor()
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            cursor5 = connection.cursor()
            sql = '''SELECT SUBSTR(TTR_ID,4,2) FROM TUTOR'''
            cursor1.execute(sql)
            numero = cursor1.fetchall()
            id = max(numero)
            ID= "T00"+str(int(id[0]) +1)
            cursor1.close()
            nombre = self.IT.nombre_2.text()
            apellido = self.IT.apellido_pat_tutor.text()
            apellido2 = self.IT.apellido_mat_tutor.text()
            sexo = self.IT.sexo_2.currentText()
            #CONEXION CON TABLA DIRECCION
            sql = '''SELECT SUBSTR(DIR_ID,4,2) FROM DIRECCION'''
            cursor4.execute(sql)
            numero = cursor4.fetchall()
            id = max(numero)
            ID_DIRECCION= "DIR"+str(int(id[0])+ 1)
            cursor4.close()
            Colonia = self.IT.colonia.text()
            Postal = self.IT.CP.text()
            Calle = self.IT.calle.text()
            Interior = self.IT.interior.text()
            Exterior = self.IT.exterior.text()
            Alcaldia = self.IT.alcaldia.text()
            Estado = self.IT.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()
            sql = '''INSERT INTO DIRECCION VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(ID_DIRECCION,Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO)
            cursor5.execute(sql) 
            connection.commit()
            cursor5.close()
            #DESCONEXION CON TABLA DIRECCION
            sql = '''INSERT INTO TUTOR VALUES ('{}','{}','{}','{}','{}','{}')'''.format(ID,nombre,apellido,apellido2,sexo,ID_DIRECCION)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Falta algún dato por llenar ó "+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()    
   
    def eliminar_TUTOR(self):
        try:    
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            nombre = self.IT.nombre_2.text()
            apellido = self.IT.apellido_pat_tutor.text()
            apellido2 = self.IT.apellido_mat_tutor.text()
            sql = '''SELECT TTR_ID FROM TUTOR WHERE UPPER(TTR_NOMBRE) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_PAT) LIKE UPPER ('{}') 
                    AND UPPER (TTR_APELLIDO_MAT) LIKE UPPER ('{}')'''.format(nombre,apellido,apellido2)
            cursor2.execute(sql)
            error = cursor2.fetchall()
            ERROR = error[0]
            sql = '''DELETE FROM TUTOR WHERE UPPER(TTR_NOMBRE) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_PAT) LIKE UPPER ('{}') 
                    AND UPPER (TTR_APELLIDO_MAT) LIKE UPPER ('{}')'''.format(nombre,apellido,apellido2)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Falta algún dato por llenar ó "+"Hay un alumno ligado con el tutor")
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()    
   
    def actualizar_TUTOR(self):
        try:
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            cursor1 = connection.cursor()
            id_tutor = self.AT.ID_TUTOR.text()

            nuevo_nombre = self.AT.nombre_2.text()
            nuevo_apellido = self.AT.apellido_pat_tutor.text()
            nuevo_apellido2 = self.AT.apellido_mat_tutor.text()
            nuevo_sexo = self.AT.sexo_2.currentText()
            #CONEXION CON TABLA DE DIRECCIÓN
            sql = '''SELECT TTR_DIRECCION_ID FROM TUTOR WHERE UPPER(TTR_ID) LIKE ('{}') '''.format(id_tutor)
            cursor1.execute(sql)
            numero = cursor1.fetchone()
            ID = str(numero[0])     
            cursor1.close()
            Colonia = self.AT.colonia.text()
            Postal = self.AT.CP.text()
            Calle = self.AT.calle.text()
            Interior = self.AT.interior.text()
            Exterior = self.AT.exterior.text()
            Alcaldia = self.AT.alcaldia.text()
            Estado = self.AT.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()
            sql = '''UPDATE DIRECCION SET DIR_COLONIA = '{}', DIR_CP = '{}', DIR_CALLE = '{}', DIR_NO_EXTERIOR = '{}', DIR_NO_INTERIOR = '{}', 
                    DIR_ALCALDIA_ID = '{}', DIR_ESTADO_ID = '{}'
                    WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO,ID)
            cursor4.execute(sql)
            connection.commit()
            cursor4.close()
            #CIERRO CONEXION DE TABLA DIRECCIÓN
            sql = '''UPDATE TUTOR SET TTR_NOMBRE = '{}', TTR_APELLIDO_PAT = '{}', TTR_APELLIDO_MAT = '{}',
                    TTR_SEXO = '{}'
                    WHERE UPPER(TTR_ID) LIKE UPPER('{}')'''.format(nuevo_nombre,nuevo_apellido,nuevo_apellido2,nuevo_sexo,id_tutor)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:    
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Falta algún dato por llenar ó "+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()  
    
    def consultar_TUTOR(self):
        try:    
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            nombre = self.CT.nombre.text()
            apellido = self.CT.apellido_pat.text()
            apellido2 = self.CT.apellido_materno.text()
            sql = '''SELECT TTR_NOMBRE, TTR_APELLIDO_PAT, TTR_APELLIDO_MAT, TTR_SEXO
                    FROM TUTOR
                    JOIN DIRECCION ON TUTOR.TTR_DIRECCION_ID = DIRECCION.DIR_ID
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                    WHERE UPPER(TTR_NOMBRE) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_PAT) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_MAT) LIKE UPPER('{}')'''.format(nombre,apellido,apellido2)
            cursor.execute(sql)
            impresion = cursor.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CT.TUTOR.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CT.TUTOR.setItem(i,n,texto)
            cursor.close()
            sql = '''SELECT EST_ESTADO,DIR_COLONIA,ALC_ALCALDIA, DIR_CP, DIR_CALLE, DIR_NO_EXTERIOR,DIR_NO_INTERIOR
                    FROM TUTOR
                    JOIN DIRECCION ON TUTOR.TTR_DIRECCION_ID = DIRECCION.DIR_ID
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                    WHERE UPPER(TTR_NOMBRE) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_PAT) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_MAT) LIKE UPPER('{}')'''.format(nombre,apellido,apellido2)
            cursor2.execute(sql)
            impresion = cursor2.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))

            for i in range(valor1):
                self.CT.DIRECCION.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CT.DIRECCION.setItem(i,n,texto)
            cursor2.close()
            sql = '''SELECT TTR_ID
                    FROM TUTOR
                    WHERE UPPER(TTR_NOMBRE) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_PAT) LIKE UPPER('{}') AND UPPER(TTR_APELLIDO_MAT) LIKE UPPER('{}')'''.format(nombre,apellido,apellido2)
            cursor3.execute(sql)
            impresion = cursor3.fetchone()
            ID = str(impresion[0])
            cursor3.close()
            sql = '''SELECT ALM_NOMBRE,ALM_APELLIDO_PAT,ALM_APELLIDO_MAT
                        FROM ALUMNO
                        WHERE UPPER(ALM_TUTOR_ID) LIKE UPPER('{}')'''.format(ID) 
            cursor4.execute(sql)    
            impresion = cursor4.fetchall()
            try: 
                valor1 = int(len(impresion))
                valor2 = int(len(impresion[0]))

                for i in range(valor1):
                    self.CT.DATOS.insertRow(i)
                    for n in range(valor2):
                        t = str(impresion[i][n])
                        texto = QTableWidgetItem(t)
                        self.CT.DATOS.setItem(i,n,texto)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("No se encontro un tutorado")
                msg.setWindowTitle("EXITOSO")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec()
            cursor4.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Falta algún dato por llenar ó "+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec() 
    
    def mostrar_TUTOR(self):
        cursor = connection.cursor()
        sql = '''SELECT TTR_NOMBRE, TTR_APELLIDO_PAT, TTR_APELLIDO_MAT, TTR_SEXO, DIR_COLONIA, DIR_CP, DIR_CALLE, DIR_NO_EXTERIOR,DIR_NO_INTERIOR, ALC_ALCALDIA, EST_ESTADO
                FROM TUTOR
                JOIN DIRECCION ON TUTOR.TTR_DIRECCION_ID = DIRECCION.DIR_ID
                JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID'''
        cursor.execute(sql)
        impresion = cursor.fetchall()
        valor1 = int(len(impresion))
        valor2 = int(len(impresion[0]))
    
        for i in range(valor1):
            self.IT.tableWidget.insertRow(i)
            for n in range(valor2):
                t = str(impresion[i][n])
                texto = QTableWidgetItem(t)
                self.IT.tableWidget.setItem(i,n,texto)
                
        cursor.close()
    
    def mostrar_TUTOR_a(self):
        cursor = connection.cursor()
        sql = '''SELECT TTR_ID,TTR_NOMBRE, TTR_APELLIDO_PAT, TTR_APELLIDO_MAT, TTR_SEXO, DIR_COLONIA, DIR_CP, DIR_CALLE, DIR_NO_EXTERIOR,DIR_NO_INTERIOR, ALC_ALCALDIA, EST_ESTADO
                FROM TUTOR
                JOIN DIRECCION ON TUTOR.TTR_DIRECCION_ID = DIRECCION.DIR_ID
                JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID'''
        cursor.execute(sql)
        impresion = cursor.fetchall()
        valor1 = int(len(impresion))
        valor2 = int(len(impresion[0]))
    
        for i in range(valor1):
            self.AT.tableWidget.insertRow(i)
            for n in range(valor2):
                t = str(impresion[i][n])
                texto = QTableWidgetItem(t)
                self.AT.tableWidget.setItem(i,n,texto)
                
        cursor.close()
    #FUNCIONES PARA DIRECCION
    def insertar_DIRECCION(self):
        try:
            cursor1 = connection.cursor()
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            sql = '''SELECT SUBSTR(DIR_ID,4,2) FROM DIRECCION'''
            cursor1.execute(sql)
            numero = cursor1.fetchall()
            id = max(numero)
            ID= "DIR"+str(int(id[0])+ 1)
            cursor1.close()
            Colonia = self.ID.colonia.text()
            Postal = self.ID.CP.text()
            Calle = self.ID.calle.text()
            Interior = self.ID.interior.text()
            Exterior = self.ID.exterior.text()
            Alcaldia = self.ID.alcaldia.text()
            Estado = self.ID.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()
            sql = '''INSERT INTO DIRECCION VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(ID,Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado todos los campos \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec() 
            
    def mostrar_DIRECCION(self):
        
            cursor = connection.cursor()
            sql = '''SELECT EST_ESTADO,DIR_COLONIA,ALC_ALCALDIA,DIR_CP,DIR_CALLE,DIR_NO_EXTERIOR,DIR_NO_INTERIOR
                    FROM DIRECCION
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID'''
            cursor.execute(sql)
            impresion = cursor.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))
        
            for i in range(valor1):
                self.ID.tabla.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.ID.tabla.setItem(i,n,texto)
            cursor.close()

    def eliminar_DIRECCION(self):
        try:
            cursor2 = connection.cursor()
            cursor1 = connection.cursor()
            id = self.ED.curp.text()
            sql = '''SELECT DIR_ID FROM DIRECCION WHERE UPPER(DIR_ID) LIKE UPPER('{}') '''.format(id)
            cursor2.execute(sql)
            error = cursor2.fetchall()
            ERROR = error[0]
            cursor2.close()
            sql = '''DELETE FROM DIRECCION WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(id)
            cursor1.execute(sql)
            connection.commit()
            cursor1.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado un ID \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
    
    def mostrar_DIRECCION_ELIMINAR(self):
        
            cursor = connection.cursor()
            sql = '''SELECT DIR_ID,EST_ESTADO,DIR_COLONIA,ALC_ALCALDIA,DIR_CP,DIR_CALLE,DIR_NO_EXTERIOR,DIR_NO_INTERIOR
                    FROM DIRECCION
                    JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                    JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID'''
            cursor.execute(sql)
            impresion = cursor.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))
        
            for i in range(valor1):
                self.ED.tabla.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.ED.tabla.setItem(i,n,texto)
            cursor.close()

    def actualizar_DIRECCION(self):
        try:    
            cursor1 = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            id = self.ED.ID_DIRECCION.text()
            Colonia = self.ED.colonia.text()
            Postal = self.ED.CP.text()
            Calle = self.ED.calle.text()
            Interior = self.ED.interior.text()
            Exterior = self.ED.exterior.text()
            Alcaldia = self.ED.alcaldia.text()
            Estado = self.ED.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()

            sql = '''UPDATE DIRECCION SET DIR_COLONIA = '{}', DIR_CP = '{}', DIR_CALLE = '{}', DIR_NO_EXTERIOR = '{}', DIR_NO_INTERIOR = '{}', 
                    DIR_ALCALDIA_ID = '{}', DIR_ESTADO_ID = '{}'
                    WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO,id)
            cursor1.execute(sql)
            connection.commit()
            cursor1.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()

        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado un ID \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
            
    def consultar_DIRECCION(self):
        try: 
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            curp = self.CD.curp.text()
            DIRECCION_ID = self.CD.ID.text()
            if(DIRECCION_ID == ''):
                sql = '''SELECT ALM_DIRECCION_ID FROM ALUMNO WHERE UPPER(ALM_CURP) LIKE UPPER('{}')'''.format(curp)
                cursor2.execute(sql)
                numero = cursor2.fetchone()
                IDa= str(numero[0])
                cursor2.close()
                sql = '''SELECT DIR_ID,DIR_COLONIA,DIR_CP,DIR_CALLE,DIR_NO_EXTERIOR,DIR_NO_INTERIOR,EST_ESTADO,ALC_ALCALDIA
                        FROM DIRECCION
                        JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                        JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                        WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(IDa)
                
                cursor.execute(sql)
                impresion = cursor.fetchall()
                valor1 = int(len(impresion))
                valor2 = int(len(impresion[0]))
                
                for i in range(valor1):
                    self.CD.tabla.insertRow(i)
                    for n in range(valor2):
                        t = str(impresion[i][n])
                        texto = QTableWidgetItem(t)
                        self.CD.tabla.setItem(i,n,texto)
                cursor.close()
            else:
                sql = '''SELECT DIR_ID,DIR_COLONIA,DIR_CP,DIR_CALLE,DIR_NO_EXTERIOR,DIR_NO_INTERIOR,EST_ESTADO,ALC_ALCALDIA
                        FROM DIRECCION
                        JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                        JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                        WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(DIRECCION_ID)
                cursor.execute(sql)
                impresion = cursor.fetchall()
                valor1 = int(len(impresion))
                valor2 = int(len(impresion[0]))
                
                for i in range(valor1):
                    self.CD.tabla.insertRow(i)
                    for n in range(valor2):
                        t = str(impresion[i][n])
                        texto = QTableWidgetItem(t)
                        self.CD.tabla.setItem(i,n,texto)
                cursor.close()
                cursor2.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado un CURP o ID \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
    #FUNCIONES PARA ESCUELA
    def insertar_ESCUELA(self):
        try:    
            cursor1 = connection.cursor()
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            cursor5 = connection.cursor()
            cursor6 = connection.cursor()
            CCT = self.IE.CCT.text()
            PLANTEL = self.IE.plantel.text()
            TELEFONO = self.IE.telefono.text()
            WEB = self.IE.web.text()
            correo = self.IE.correo.text()
            #CONEXION CON TABLA DE CORREO
            dominio = self.IE.dominio.currentText()
            sql = '''SELECT COR_ID FROM CORREO WHERE UPPER(COR_CORREO) LIKE UPPER('{}')'''.format(dominio)
            cursor6.execute(sql)
            D = cursor6.fetchone()
            DOMINIO = str(D[0])
            cursor6.close()
            #CIERRO CONEXION CON TABLA DE CORREO
            institucion = self.IE.institucion.currentText()
            sql = '''SELECT INS_ID FROM INSTITUCION WHERE UPPER(INS_NOMBRE_ESCUELA) LIKE UPPER('{}')'''.format(institucion)
            cursor4.execute(sql)
            I = cursor4.fetchone()
            INSTITUCION = str(I[0])
            cursor4.close()
            #CONEXION CON LA TABLA DIRECCION
            sql = '''SELECT SUBSTR(DIR_ID,4,2) FROM DIRECCION'''
            cursor1.execute(sql)
            numero = cursor1.fetchall()
            id = max(numero)
            ID= "DIR"+str(int(id[0])+ 1)
            cursor1.close()
            Colonia = self.IE.colonia.text()
            Postal = self.IE.CP.text()
            Calle = self.IE.calle.text()
            Interior = self.IE.interior.text()
            Exterior = self.IE.exterior.text()
            Alcaldia = self.IE.alcaldia.text()
            Estado = self.IE.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()
            sql = '''INSERT INTO DIRECCION VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(ID,Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO)
            cursor.execute(sql) 
            connection.commit()
            cursor.close()
            #CIERRO LA CONEXION CON LA TABLA DIRECCION
            sql = '''INSERT INTO ESCUELA VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(CCT,PLANTEL,TELEFONO,WEB,DOMINIO,INSTITUCION,ID,correo)
            cursor5.execute(sql)
            connection.commit()
            cursor5.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado algun dato \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()  

    def eliminar_ESCUELA(self):
        try:    
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            CCT = self.IE.CCT.text()
            sql = '''SELECT ESC_CCT FROM ESCUELA WHERE  UPPER(ESC_CCT) LIKE UPPER('{}')'''.format(CCT)
            cursor2.execute(sql)
            error = cursor2.fetchall()
            ERROR = error[0] 
            sql = '''DELETE ESCUELA WHERE UPPER(ESC_CCT) LIKE UPPER('{}')'''.format(CCT)
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado el CCT \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
    
    def actualizar_ESCUELA(self):
        try:
            cursor = connection.cursor()
            cursor1 = connection.cursor()
            cursor2 = connection.cursor()
            cursor3 = connection.cursor()
            cursor4 = connection.cursor()
            cursor5 = connection.cursor()
            cursor6 = connection.cursor()
            #PIDO DATOS
            CCT_ANTIGUO = self.IE.CCT.text()
            PLANTEL = self.IE.plantel.text()
            TELEFONO = self.IE.telefono.text()
            WEB = self.IE.web.text()
            correo = self.IE.correo.text()
            dominio = self.IE.dominio.currentText()
            institucion = self.IE.institucion.currentText()
            #Obtengo el id de dominio
            sql = '''SELECT COR_ID FROM CORREO WHERE UPPER(COR_CORREO) LIKE UPPER('{}')'''.format(dominio)
            cursor.execute(sql)
            d = cursor.fetchone()
            DOMINIO = str(d[0]) 
            cursor.close()
            #Obtengo el id de institucion
            sql = '''SELECT INS_ID FROM INSTITUCION WHERE UPPER(INS_NOMBRE_ESCUELA) LIKE UPPER('{}')'''.format(institucion)
            cursor4.execute(sql)
            i = cursor4.fetchone()
            INSTITUCION = str(i[0])
            cursor4.close()
            #CONEXION CON LA TABLA DE DIRECCION PARA ACTUALIZAR
            sql = '''SELECT ESC_DIRECCION_ID FROM ESCUELA WHERE UPPER(ESC_CCT) LIKE UPPER('{}')'''.format(CCT_ANTIGUO)
            cursor1.execute(sql)
            numero = cursor1.fetchone()
            ID= str(numero[0])
            cursor1.close()
            Colonia = self.IE.colonia.text()
            Postal = self.IE.CP.text()
            Calle = self.IE.calle.text()
            Interior = self.IE.interior.text()
            Exterior = self.IE.exterior.text()
            Alcaldia = self.IE.alcaldia.text()
            Estado = self.IE.estado.currentText()
            sql = '''SELECT EST_ID FROM ESTADO WHERE UPPER(EST_ESTADO) LIKE UPPER('{}')'''.format(Estado)
            cursor2.execute(sql)
            EST = cursor2.fetchone()
            ESTADO = str(EST[0])
            cursor2.close()
            sql = '''SELECT ALC_ID FROM ALCALDIA WHERE UPPER(ALC_ALCALDIA) LIKE UPPER('{}')'''.format(Alcaldia)
            cursor3.execute(sql)
            ALC = cursor3.fetchone()
            ALCALDIA = str(ALC[0])
            cursor3.close()
            sql = '''UPDATE DIRECCION SET DIR_COLONIA = '{}', DIR_CP = '{}', DIR_CALLE = '{}', DIR_NO_EXTERIOR = '{}', DIR_NO_INTERIOR = '{}', 
                    DIR_ALCALDIA_ID = '{}', DIR_ESTADO_ID = '{}'
                    WHERE UPPER(DIR_ID) LIKE UPPER('{}')'''.format(Colonia,Postal,Calle,Interior,Exterior,ALCALDIA,ESTADO,ID)
            cursor6.execute(sql)
            connection.commit()
            cursor6.close()
            #TERMINO CONEXION CON LA TABLA DE DIRECCION
            sql = '''UPDATE ESCUELA SET ESC_PLANTEL = '{}',ESC_TELEFONO = '{}',ESC_PAGINA_WEB = '{}',ESC_DOMINIO_ID = '{}', ESC_INSTITUCION_ID = '{}',
                        ESC_NOMBRE_CORREO = '{}' WHERE UPPER(ESC_CCT) LIKE UPPER('{}')'''.format(PLANTEL,TELEFONO,WEB,DOMINIO,INSTITUCION,correo,CCT_ANTIGUO)
            cursor5.execute(sql)
            connection.commit()
            cursor5.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación \nPor favor cierre y abra la ventana para ver los cambios")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado algun dato \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()  
    
    def consultar_ESCUELA(self):
        try:    
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            CCT = self.CE.CCT.text()
            sql = '''SELECT ESC_CCT, INS_NOMBRE_ESCUELA,ESC_PLANTEL, ESC_TELEFONO,ESC_PAGINA_WEB,ESC_NOMBRE_CORREO,COR_CORREO
                FROM ESCUELA
                JOIN DIRECCION ON ESCUELA.ESC_DIRECCION_ID = DIRECCION.DIR_ID
                JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                JOIN INSTITUCION ON ESCUELA.ESC_INSTITUCION_ID = INSTITUCION.INS_ID
                JOIN CORREO ON ESCUELA.ESC_DOMINIO_ID = CORREO.COR_ID
                WHERE UPPER(ESC_CCT) LIKE UPPER('{}')
                '''.format(CCT)
            cursor2.execute(sql)
            impresion = cursor2.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))
            for i in range(valor1):
                self.CE.tableWidget.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CE.tableWidget.setItem(i,n,texto)
            cursor2.close()
            sql = '''SELECT DIR_COLONIA,DIR_CP,DIR_CALLE,
                DIR_NO_INTERIOR,DIR_NO_EXTERIOR,ALC_ALCALDIA,EST_ESTADO 
                FROM ESCUELA
                JOIN DIRECCION ON ESCUELA.ESC_DIRECCION_ID = DIRECCION.DIR_ID
                JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
                JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
                JOIN INSTITUCION ON ESCUELA.ESC_INSTITUCION_ID = INSTITUCION.INS_ID
                JOIN CORREO ON ESCUELA.ESC_DOMINIO_ID = CORREO.COR_ID
                WHERE UPPER(ESC_CCT) LIKE UPPER('{}')
                '''.format(CCT)
            cursor.execute(sql)
            impresion = cursor.fetchall()
            valor1 = int(len(impresion))
            valor2 = int(len(impresion[0]))
            for i in range(valor1):
                self.CE.direccion.insertRow(i)
                for n in range(valor2):
                    t = str(impresion[i][n])
                    texto = QTableWidgetItem(t)
                    self.CE.direccion.setItem(i,n,texto)
            
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Se realizo correctamente la operación")
            msg.setWindowTitle("EXITOSO")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        except Exception as e:
            msg = QMessageBox()
            error = str(e)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No ha ingresado algun dato \n ó \n"+error)
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()  
    
    def mostrar_ESCUELA(self):
        cursor = connection.cursor()
        sql = '''SELECT ESC_CCT, INS_NOMBRE_ESCUELA,ESC_PLANTEL, ESC_TELEFONO,ESC_PAGINA_WEB,ESC_NOMBRE_CORREO,COR_CORREO,DIR_COLONIA,DIR_CP,DIR_CALLE,
            DIR_NO_INTERIOR,DIR_NO_EXTERIOR,ALC_ALCALDIA,EST_ESTADO 
            FROM ESCUELA
            JOIN DIRECCION ON ESCUELA.ESC_DIRECCION_ID = DIRECCION.DIR_ID
            JOIN ESTADO ON DIRECCION.DIR_ESTADO_ID = ESTADO.EST_ID
            JOIN ALCALDIA ON DIRECCION.DIR_ALCALDIA_ID = ALCALDIA.ALC_ID
            JOIN INSTITUCION ON ESCUELA.ESC_INSTITUCION_ID = INSTITUCION.INS_ID
            JOIN CORREO ON ESCUELA.ESC_DOMINIO_ID = CORREO.COR_ID'''
        cursor.execute(sql)
        impresion = cursor.fetchall()
        valor1 = int(len(impresion))
        valor2 = int(len(impresion[0]))
        
        for i in range(valor1):
            self.IE.tableWidget.insertRow(i)
            for n in range(valor2):
                t = str(impresion[i][n])
                texto = QTableWidgetItem(t)
                self.IE.tableWidget.setItem(i,n,texto)
        cursor.close()
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())