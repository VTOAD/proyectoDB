from datos.modelos import Camioneta
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Camioneta)


def buscar(id_registro):
    return buscar_registro(Camioneta, id_registro)


def eliminar(registro):
    eliminar_registro(registro)


def buscar_por_vehiculo(id_vehiculo):
    return Camioneta.get_or_none(Camioneta.vehiculo == id_vehiculo)
