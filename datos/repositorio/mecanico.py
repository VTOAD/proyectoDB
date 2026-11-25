from datos.modelos import Mecanico
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Mecanico)


def buscar(id_registro):
    return buscar_registro(Mecanico, id_registro)


def eliminar(registro):
    eliminar_registro(registro)
