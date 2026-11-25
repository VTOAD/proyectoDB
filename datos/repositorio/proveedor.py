from datos.modelos import Proveedor
from datos.repositorio.comun import (
    buscar_registro, eliminar_registro, guardar_registro, listar_registros,
)


def guardar(registro):
    guardar_registro(registro)


def listar():
    return listar_registros(Proveedor)


def buscar(id_registro):
    return buscar_registro(Proveedor, id_registro)


def eliminar(registro):
    eliminar_registro(registro)
