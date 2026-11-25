# Taller mecánico

Aplicación de consola para registrar clientes, vehículos, mantenimientos, repuestos y facturas de un taller. Usa SQLite como base de datos local y requiere iniciar sesión.

## Integrantes

Completar con los nombres de los integrantes del grupo antes de entregar.

## Instalación en Windows

El proyecto se verificó con Python 3.14. Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Usa una terminal interactiva para que Maskpass pueda leer los caracteres de la contraseña.

| Dependencia | Uso |
| --- | --- |
| Peewee | Modelos y consultas a SQLite |
| bcrypt | Generación y validación del hash de contraseña |
| Maskpass | Entrada de contraseña con asteriscos |
| python-dotenv | Lectura de la configuración local |

## Base de datos y primera cuenta

Al ejecutar `main.py`, Peewee crea las tablas e índices que falten en el archivo local `taller.sqlite3`. Para elegir otra ruta, copia `.env.example` a `.env` y edita `RUTA_BASE_DATOS`. La ruta relativa se resuelve desde la carpeta del proyecto.

También puedes crear una base vacía con el [script SQL](datos/sql/crear_base_datos.sql). Ejecuta esto desde la carpeta del proyecto:

```powershell
.\.venv\Scripts\python.exe -c "import sqlite3; from pathlib import Path; from auxiliares.configuracion import RUTA_BASE_DATOS; conexion = sqlite3.connect(RUTA_BASE_DATOS); conexion.executescript(Path('datos/sql/crear_base_datos.sql').read_text(encoding='utf-8')); conexion.close()"
```

Si la base no tiene usuarios, el programa pide crear la primera cuenta y luego solicita iniciar sesión con ella. Elige una contraseña de al menos 8 caracteres (máximo de 72 bytes). Las cuentas se administran en **Usuarios**. Para eliminar una cuenta debes iniciar sesión con otra.

## Uso del menú

Cada entidad permite crear, listar, buscar por ID, modificar y eliminar. Al editar, Enter conserva el dato y un guion vacía un campo opcional. Al eliminar un registro con datos relacionados, SQLite protege las referencias existentes. Para eliminarlo, primero revisa los registros que lo referencian.

Para probar el flujo, crea un taller, un cliente y un proveedor. Luego puedes registrar un mecánico, un vehículo y un repuesto. Usa sus ID para crear una mantención, anotar los repuestos usados y emitir una factura. Ingresa los montos en pesos enteros. El total de la factura se calcula sumando el subtotal y los impuestos ingresados.

## Estructura

| Ruta | Responsabilidad |
| --- | --- |
| `datos/conexion.py` y `datos/model_base.py` | Conexión SQLite y configuración de Peewee |
| `datos/modelos/` | Tablas y relaciones |
| `datos/repositorio/` | Funciones de guardado con `save()`, listado, búsqueda y eliminación |
| `datos/sql/` | Script de creación de tablas e índices |
| `negocio/` | Reglas del taller, validación de formularios y autenticación |
| `presentacion/` | Login, entrada de datos y menús de consola |
| `auxiliares/` | Configuración, validaciones comunes y mensajes |
| `main.py` | Punto de entrada |

El [diagrama de clases](diagrama_clases.md) adapta el modelo entregado del taller a las tablas de esta aplicación e incorpora `DetalleMantencion` y `Usuario`. La carpeta se inició con el diagrama de referencia. El código y los scripts originales de la Evaluación 2 se deben recuperar del repositorio del equipo para acreditar la continuidad histórica.
