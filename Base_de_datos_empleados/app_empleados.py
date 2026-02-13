from ast import Lambda
import sys
import psycopg2
from PyQt5.QtWidgets import *

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont

from util.base_de_datos import base_datos, contraseña, puerto, servidor, usuario

# conecto a base de datos neon

conn = psycopg2.connect(
    dbname=base_datos,
    user=usuario,
    password=contraseña,
    host=servidor,
    port=puerto
)


def seleccionar_emp1eado(tabla, nombre_input, puesto_input, salario_input):
    fila = tabla.currentRow()
    if fila == -1:
        return

    nombre_input.setText(tabla.item(fila, 1).text())
    puesto_input.setText(tabla.item(fila, 2).text())
    salario_input.setText(tabla.item(fila, 3).text())

def eliminar_por_id(Nombre,id_empleado,tabla):
    respuesta = QMessageBox.question(
        None, "Confirmar eliminacion",
        f'quieres eliminar al empleado "{Nombre}" con ID "{id_empleado}"',
        QMessageBox.Yes | QMessageBox.No
    )
    if respuesta == QMessageBox.Yes:
        cursor=conn.cursor()
        cursor.execute(
            "DELETE FROM empleados WHERE id=%s",(id_empleado,)
        )
        conn.commit()
        cursor.close()
        
        for caja_texto_input in tabla.parent().findChildren(QLineEdit):
            caja_texto_input.clear()
        
        tabla.clearSelection()
        tabla.setCurrentCell(-1, -1)
        
        cargar_tabla(tabla)


def guardar_empleado(nombre_input, puesto_input, salario_input, tabla):
    nombre = nombre_input.text()
    puesto = puesto_input.text()
    salario = salario_input.text()

    fila = tabla.currentRow()
    
    cursor = conn.cursor()
    
    if fila != -1:
        id_item=tabla.item(fila,0)
        if id_item:
            id_empleado = id_item.text()
            cursor.execute(
            """UPDATE empleados SET nombre=%s,puesto=%s,salario=%s
                WHERE id=%s""" ,(nombre, puesto,salario,id_empleado)
            )
    else:
        cursor.execute(
            "INSERT INTO empleados(nombre,puesto,salario) VALUES(%s,%s,%s)", 
            (nombre, puesto, salario))
    conn.commit()
    cursor.close()
    # limpiiamos caja de texto
    nombre_input.clear()
    puesto_input.clear()
    salario_input.clear()

    tabla.clearSelection()
    cargar_tabla(tabla)


def cargar_tabla(tabla):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados ORDER BY id")
    empleados = cursor.fetchall()
    cursor.close()
    tabla.setRowCount(len(empleados))
    tabla.setColumnCount(5)
    tabla.setHorizontalHeaderLabels(
        ["ID", "Nombre", "Puesto", "Salario", "Accion"])
    for i, empleado in enumerate(empleados):
        for j, columna in enumerate(empleado):
            item = QTableWidgetItem(str(columna))
            item.setTextAlignment(Qt.AlignCenter)
            tabla.setItem(i, j, item)
        
        boton_eliminar = QPushButton()
        boton_eliminar.setIcon(QIcon("Base_de_datos_empleados/papelerapy.png"))
        boton_eliminar.setIconSize(QSize(24, 24))
        boton_eliminar.setFlat(True)
        boton_eliminar.setToolTip("Eliminar")
        boton_eliminar.clicked.connect(
            lambda _, id=empleado[0] , noombre = empleado[1]:eliminar_por_id(noombre,id, tabla)
        )
        tabla.setCellWidget(i, 4, boton_eliminar)


# esta funcion crea la ventana de la app


def crear_ventana():
    ventana = QWidget()
    ventana.setWindowTitle("Mantenimiento de empleados")
    ventana.setGeometry(100, 100, 900, 400)

    layout = QVBoxLayout()
    entrada_layout = QHBoxLayout()

    # creamos nombre
    nombre_layout = QVBoxLayout()

    # caja de texto
    nombre_input = QLineEdit()
    nombre_input.setMinimumSize(200, 35)
    nombre_input.setFont(QFont("Arial", 12))

    # Imagen
    nombre_label = QLabel("Nombre")
    nombre_label.setFont(QFont("Arial", 11))

    nombre_layout.addWidget(nombre_label)
    nombre_layout.addWidget(nombre_input)

    entrada_layout.addLayout(nombre_layout)

    # creamos puesto
    puesto_layout = QVBoxLayout()

    # caja de texto
    puesto_input = QLineEdit()
    puesto_input.setMinimumSize(200, 35)
    puesto_input.setFont(QFont("Arial", 12))

    # Imagen
    puesto_label = QLabel("puesto")
    puesto_label.setFont(QFont("Arial", 11))

    puesto_layout.addWidget(puesto_label)
    puesto_layout.addWidget(puesto_input)

    entrada_layout.addLayout(puesto_layout)

    # creamos salario
    salario_layout = QVBoxLayout()

    # caja de texto
    salario_input = QLineEdit()
    salario_input.setMinimumSize(200, 35)
    salario_input.setFont(QFont("Arial", 12))

    # Imagen
    salario_label = QLabel("salario")
    salario_label.setFont(QFont("Arial", 11))

    salario_layout.addWidget(salario_label)
    salario_layout.addWidget(salario_input)

    entrada_layout.addLayout(salario_layout)

    # Boton guardar
    boton_guardar = QPushButton()
    boton_guardar.setIcon(QIcon("Base_de_datos_empleados/guardarpy.png"))
    boton_guardar.setIconSize(QSize(36, 36))
    boton_guardar.setFlat(True)
    boton_guardar.setToolTip("Guardar cambios")

    entrada_layout.addWidget(boton_guardar)

    # proporcion del tamaño de cada seccion

    entrada_layout.setStretch(0, 3)
    entrada_layout.setStretch(1, 1)
    entrada_layout.setStretch(2, 1)
    entrada_layout.setStretch(3, 0)

    layout.addLayout(entrada_layout)
    # creando grid - elemento grafico
    # Lo que el ususario va  a ver

    tabla = QTableWidget()
    tabla.setColumnCount(4)
    tabla.setHorizontalHeaderLabels(['id', "Nombre", "puesto", "salario"])

    tabla.horizontalHeader().setStretchLastSection(True)
    tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    layout.addWidget(tabla)
    # configuro cilck boton guardar
    boton_guardar.clicked.connect(
        lambda: guardar_empleado(
            nombre_input, puesto_input, salario_input, tabla)
    )

    # configuro seleccion

    tabla.cellClicked.connect(
        lambda row, col: seleccionar_emp1eado(
            tabla,
            nombre_input,
            puesto_input,
            salario_input)
    )

    ventana.setLayout(layout)
    cargar_tabla(tabla)
    ventana.show()
    return ventana

# esta funcion inicia PyQt5
# ejecuta la funcion anterior(crear ventana)
# frena la app cuando se cierra la ventana


def main():
    app = QApplication(sys.argv)
    ventana = crear_ventana()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
