from datos.modelos import Vehiculo
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Vehiculo)


def buscar(id_registro):
    return buscar_registro(Vehiculo, id_registro)


def eliminar(registro):
    eliminar_registro(registro)
