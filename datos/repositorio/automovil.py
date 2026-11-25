from datos.modelos import Automovil
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Automovil)


def buscar(id_registro):
    return buscar_registro(Automovil, id_registro)


def eliminar(registro):
    eliminar_registro(registro)


def buscar_por_vehiculo(id_vehiculo):
    return Automovil.get_or_none(Automovil.vehiculo == id_vehiculo)
