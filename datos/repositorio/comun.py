from peewee import IntegrityError

from auxiliares.mensajes import DATOS_EN_CONFLICTO
from datos.conexion import base_datos
from datos.modelos import MODELOS


def iniciar_base_datos():
    base_datos.connect(reuse_if_open=True)
    base_datos.create_tables(MODELOS)


def cerrar_base_datos():
    base_datos.close()


def guardar_registro(registro):
    try:
        registro.save()
    except IntegrityError:
        raise ValueError(DATOS_EN_CONFLICTO) from None


def listar_registros(modelo):
    return list(modelo.select().order_by(modelo.id))


def buscar_registro(modelo, id_registro):
    return modelo.get_or_none(modelo.id == id_registro)


def eliminar_registro(registro):
    try:
        registro.delete_instance()
    except IntegrityError:
        raise ValueError(DATOS_EN_CONFLICTO) from None
