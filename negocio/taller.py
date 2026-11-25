from peewee import BooleanField, DateField, ForeignKeyField, IntegerField, TimeField

from auxiliares.mensajes import REGISTRO_INEXISTENTE
from auxiliares.validaciones import (
    convertir_fecha, convertir_hora, entero_no_negativo, texto_obligatorio,
)
from datos.modelos import (
    Automovil, Camioneta, Cliente, DetalleMantencion, Factura, Mantencion,
    Mecanico, Proveedor, Repuesto, Taller, Vehiculo,
)
from datos.repositorio import (
    taller,
    cliente,
    mecanico,
    vehiculo,
    camioneta,
    automovil,
    proveedor,
    repuesto,
    mantencion,
    detalle_mantencion,
    factura,
)
from datos.repositorio.comun import cerrar_base_datos, iniciar_base_datos

ENTIDADES = {
    "taller": (Taller, taller),
    "cliente": (Cliente, cliente),
    "mecanico": (Mecanico, mecanico),
    "vehiculo": (Vehiculo, vehiculo),
    "camioneta": (Camioneta, camioneta),
    "automovil": (Automovil, automovil),
    "proveedor": (Proveedor, proveedor),
    "repuesto": (Repuesto, repuesto),
    "mantencion": (Mantencion, mantencion),
    "detalle_mantencion": (DetalleMantencion, detalle_mantencion),
    "factura": (Factura, factura),
}
REPOSITORIOS = dict(ENTIDADES.values())


def campos_editables(modelo):
    return [
        campo for campo in modelo._meta.sorted_fields
        if not campo.primary_key and not (modelo is Factura and campo.name == "total")
    ]


def pedir_registro(repositorio, id_registro):
    registro = repositorio.buscar(id_registro)
    if registro is None:
        raise ValueError(REGISTRO_INEXISTENTE)
    return registro


def datos_publicos(registro):
    datos = {}
    for campo in registro._meta.sorted_fields:
        if isinstance(campo, ForeignKeyField):
            datos[campo.column_name] = getattr(registro, campo.object_id_name)
        else:
            datos[campo.name] = getattr(registro, campo.name)
    return datos


def campos_formulario(entidad):
    modelo, _ = ENTIDADES[entidad]
    campos = {}
    for campo in campos_editables(modelo):
        nombre = campo.name
        etiqueta = nombre.replace("_", " ")
        if isinstance(campo, ForeignKeyField):
            etiqueta = f"ID de {etiqueta}"
        elif isinstance(campo, BooleanField):
            etiqueta += " (s/n)"
        elif isinstance(campo, DateField):
            etiqueta += " (AAAA-MM-DD)"
        elif isinstance(campo, TimeField):
            etiqueta += " (HH:MM)"
        if campo.null:
            etiqueta += " (opcional)"
        campos[nombre] = etiqueta
    return campos


def convertir_valor(campo, valor):
    nombre = campo.name.replace("_", " ")
    if campo.null and not valor:
        return None
    if isinstance(campo, ForeignKeyField):
        id_registro = entero_no_negativo(valor, nombre)
        return pedir_registro(REPOSITORIOS[campo.rel_model], id_registro)
    if isinstance(campo, IntegerField):
        return entero_no_negativo(valor, nombre)
    if isinstance(campo, BooleanField):
        if valor.lower() not in ("s", "n"):
            raise ValueError(f"Responde s o n para {nombre}.")
        return valor.lower() == "s"
    if isinstance(campo, DateField):
        return convertir_fecha(valor, nombre)
    if isinstance(campo, TimeField):
        return convertir_hora(valor, nombre)
    return texto_obligatorio(valor, nombre)


def validar_vehiculo(registro):
    registro.patente = registro.patente.upper()
    if len(registro.patente) != 6 or not registro.patente.isalnum():
        raise ValueError("La patente debe tener 6 letras o números.")
    if registro.anio < 1886:
        raise ValueError("Ingresa un año válido.")


def validar_tipo_vehiculo(id_vehiculo, otro_repositorio):
    if otro_repositorio.buscar_por_vehiculo(id_vehiculo):
        raise ValueError("El vehículo ya está registrado con otro tipo.")


def validar_registro(entidad, registro):
    match entidad:
        case "vehiculo":
            validar_vehiculo(registro)
        case "cliente" if "@" not in registro.email or " " in registro.email:
            raise ValueError("Ingresa un correo válido.")
        case "mantencion" if registro.fecha_salida is not None:
            if registro.fecha_salida < registro.fecha_ingreso:
                raise ValueError("La fecha de salida debe ser posterior o igual a la de ingreso.")
        case "automovil":
            validar_tipo_vehiculo(registro.vehiculo_id, camioneta)
        case "camioneta":
            validar_tipo_vehiculo(registro.vehiculo_id, automovil)
        case "detalle_mantencion" if registro.cantidad == 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        case "factura":
            registro.total = entero_no_negativo(
                str(registro.subtotal + registro.impuestos), "El total"
            )


def guardar(entidad, entradas, id_registro=None):
    modelo, repositorio = ENTIDADES[entidad]
    registro = modelo() if id_registro is None else pedir_registro(repositorio, id_registro)
    for campo in campos_editables(modelo):
        if campo.name in entradas:
            setattr(registro, campo.name, convertir_valor(campo, entradas[campo.name]))
        elif id_registro is None and not campo.null:
            raise ValueError(f"Falta el campo {campo.name.replace('_', ' ')}.")
    validar_registro(entidad, registro)
    repositorio.guardar(registro)
    return registro.id


def listar(entidad):
    _, repositorio = ENTIDADES[entidad]
    return [datos_publicos(registro) for registro in repositorio.listar()]


def buscar(entidad, id_registro):
    _, repositorio = ENTIDADES[entidad]
    return datos_publicos(pedir_registro(repositorio, id_registro))


def eliminar(entidad, id_registro):
    _, repositorio = ENTIDADES[entidad]
    repositorio.eliminar(pedir_registro(repositorio, id_registro))
