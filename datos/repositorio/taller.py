from datos.modelos import Taller
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Taller)


def buscar(id_registro):
    return buscar_registro(Taller, id_registro)


def eliminar(registro):
    eliminar_registro(registro)
