from datos.modelos import Repuesto
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Repuesto)


def buscar(id_registro):
    return buscar_registro(Repuesto, id_registro)


def eliminar(registro):
    eliminar_registro(registro)
