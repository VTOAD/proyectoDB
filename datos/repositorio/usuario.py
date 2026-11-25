from datos.modelos import Usuario
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Usuario)


def buscar(id_registro):
    return buscar_registro(Usuario, id_registro)


def eliminar(registro):
    eliminar_registro(registro)


def buscar_por_nombre(nombre_usuario):
    return Usuario.get_or_none(Usuario.nombre_usuario == nombre_usuario)


def existen_usuarios():
    return Usuario.select().exists()
