# Proyectos de aprendizaje / prácticas

Colección de mini proyectos desarrollados para practicar fundamentos de Python. Incluye un clon básico de Twitter, una aplicación de gestión de empleados con base de datos PostgreSQL y un videojuego simple desarrollado con Pygame. Proyectos realizados durante mi aprendizaje práctico y experimentación.

---

## Requisitos

- Python 3.12

### Instalación de dependencias

```bash
# (Opcional) Crear entorno virtual
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# Instala el requirements
pip install -r requirements.txt
```

---

## Proyectos incluidos

### 🐦 Clon básico de Twitter

Clon visual de la interfaz de Twitter desarrollado con HTML y CSS. Incluye JavaScript mínimo utilizado únicamente para interacciones básicas como navegación y cierre de elementos de la interfaz. Proyecto enfocado en práctica de maquetado y replicación de diseño frontend.

#### Ejecución
Abrir la carpeta del proyecto y ejecutar un Live Server  
(por ejemplo usando la extensión Live Server de VS Code).

---

### 👨‍💼 Gestión de empleados

Aplicación conectada a PostgreSQL para administrar empleados.

#### Configuración

Completar las credenciales de la base de datos:

```python
base_datos = "DATABASE_NAME"
usuario = "USER"
servidor = "HOST"
contraseña = "PASSWORD"
puerto = "PORT"
```

#### Ejecución

```bash
python Base_de_datos_empleados/app_empleados.py
```

---

### 🎮 Juego 2D con Pygame

Pequeño videojuego desarrollado para practicar lógica de programación y manejo de eventos.

#### Ejecución

```bash
python Aliens-Attack/main.py
```

---

## Contacto
Este repositorio es un proyecto educativo y de demostración personal. No se aceptan Pull Requests ni contribuciones externas. Si deseas hacer sugerencias o comentarios, puedes utilizar la sección **Discussions** del repositorio.


Contacto profesional: emamarin256@gmail.com
