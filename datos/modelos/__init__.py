from peewee import BooleanField, CharField, DateField, ForeignKeyField, IntegerField, TimeField

from datos.model_base import ModelBase


class Taller(ModelBase):
    nombre_sucursal = CharField()
    direccion = CharField()
    telefono = CharField()
    horario_apertura = TimeField()
    horario_cierre = TimeField()


class Cliente(ModelBase):
    rut = CharField(unique=True)
    nombre = CharField()
    telefono = CharField()
    email = CharField()
    direccion = CharField()


class Mecanico(ModelBase):
    taller = ForeignKeyField(Taller)
    codigo_empleado = CharField(unique=True)
    nombre = CharField()
    especialidad = CharField()
    anios_experiencia = IntegerField()


class Vehiculo(ModelBase):
    cliente = ForeignKeyField(Cliente)
    patente = CharField(unique=True)
    marca = CharField()
    modelo = CharField()
    anio = IntegerField()
    kilometraje = IntegerField()


class Camioneta(ModelBase):
    vehiculo = ForeignKeyField(Vehiculo, unique=True)
    capacidad_carga_kg = IntegerField()
    tipo_traccion = CharField()
    tiene_cupula = BooleanField()


class Automovil(ModelBase):
    vehiculo = ForeignKeyField(Vehiculo, unique=True)
    cantidad_puertas = IntegerField()
    tipo_maletero = CharField()


class Proveedor(ModelBase):
    rut_empresa = CharField(unique=True)
    razon_social = CharField()
    contacto = CharField()


class Repuesto(ModelBase):
    taller = ForeignKeyField(Taller)
    proveedor = ForeignKeyField(Proveedor)
    codigo_pieza = CharField(unique=True)
    nombre_pieza = CharField()
    marca_pieza = CharField()
    precio_unitario = IntegerField()
    stock_disponible = IntegerField()
    stock_minimo = IntegerField()


class Mantencion(ModelBase):
    vehiculo = ForeignKeyField(Vehiculo)
    mecanico = ForeignKeyField(Mecanico)
    fecha_ingreso = DateField()
    fecha_salida = DateField(null=True)
    tipo_servicio = CharField()
    observaciones = CharField(null=True)
    costo_mano_obra = IntegerField()
    estado_actual = CharField()


class DetalleMantencion(ModelBase):
    mantencion = ForeignKeyField(Mantencion)
    repuesto = ForeignKeyField(Repuesto)
    cantidad = IntegerField()


DetalleMantencion.add_index(
    DetalleMantencion.mantencion, DetalleMantencion.repuesto, unique=True
)


class Factura(ModelBase):
    mantencion = ForeignKeyField(Mantencion, unique=True)
    numero_folio = CharField(unique=True)
    fecha_emision = DateField()
    subtotal = IntegerField()
    impuestos = IntegerField()
    total = IntegerField()
    metodo_pago = CharField()


class Usuario(ModelBase):
    nombre_usuario = CharField(unique=True)
    contrasena_hash = CharField()


MODELOS = (
    Taller,
    Cliente,
    Mecanico,
    Vehiculo,
    Camioneta,
    Automovil,
    Proveedor,
    Repuesto,
    Mantencion,
    DetalleMantencion,
    Factura,
    Usuario,
)
