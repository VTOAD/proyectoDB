from peewee import Model

from datos.conexion import base_datos


class ModelBase(Model):
    class Meta:
        database = base_datos
        legacy_table_names = False
