PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE IF NOT EXISTS "cliente" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "rut" VARCHAR(255) NOT NULL,
    "nombre" VARCHAR(255) NOT NULL,
    "telefono" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "direccion" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "vehiculo" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "cliente_id" INTEGER NOT NULL,
    "patente" VARCHAR(255) NOT NULL,
    "marca" VARCHAR(255) NOT NULL,
    "modelo" VARCHAR(255) NOT NULL,
    "anio" INTEGER NOT NULL,
    "kilometraje" INTEGER NOT NULL,
    FOREIGN KEY ("cliente_id") REFERENCES "cliente" ("id")
);

CREATE TABLE IF NOT EXISTS "automovil" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "vehiculo_id" INTEGER NOT NULL,
    "cantidad_puertas" INTEGER NOT NULL,
    "tipo_maletero" VARCHAR(255) NOT NULL,
    FOREIGN KEY ("vehiculo_id") REFERENCES "vehiculo" ("id")
);

CREATE TABLE IF NOT EXISTS "camioneta" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "vehiculo_id" INTEGER NOT NULL,
    "capacidad_carga_kg" INTEGER NOT NULL,
    "tipo_traccion" VARCHAR(255) NOT NULL,
    "tiene_cupula" INTEGER NOT NULL,
    FOREIGN KEY ("vehiculo_id") REFERENCES "vehiculo" ("id")
);

CREATE TABLE IF NOT EXISTS "taller" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "nombre_sucursal" VARCHAR(255) NOT NULL,
    "direccion" VARCHAR(255) NOT NULL,
    "telefono" VARCHAR(255) NOT NULL,
    "horario_apertura" TIME NOT NULL,
    "horario_cierre" TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS "mecanico" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "taller_id" INTEGER NOT NULL,
    "codigo_empleado" VARCHAR(255) NOT NULL,
    "nombre" VARCHAR(255) NOT NULL,
    "especialidad" VARCHAR(255) NOT NULL,
    "anios_experiencia" INTEGER NOT NULL,
    FOREIGN KEY ("taller_id") REFERENCES "taller" ("id")
);

CREATE TABLE IF NOT EXISTS "mantencion" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "vehiculo_id" INTEGER NOT NULL,
    "mecanico_id" INTEGER NOT NULL,
    "fecha_ingreso" DATE NOT NULL,
    "fecha_salida" DATE,
    "tipo_servicio" VARCHAR(255) NOT NULL,
    "observaciones" VARCHAR(255),
    "costo_mano_obra" INTEGER NOT NULL,
    "estado_actual" VARCHAR(255) NOT NULL,
    FOREIGN KEY ("vehiculo_id") REFERENCES "vehiculo" ("id"),
    FOREIGN KEY ("mecanico_id") REFERENCES "mecanico" ("id")
);

CREATE TABLE IF NOT EXISTS "proveedor" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "rut_empresa" VARCHAR(255) NOT NULL,
    "razon_social" VARCHAR(255) NOT NULL,
    "contacto" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "repuesto" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "taller_id" INTEGER NOT NULL,
    "proveedor_id" INTEGER NOT NULL,
    "codigo_pieza" VARCHAR(255) NOT NULL,
    "nombre_pieza" VARCHAR(255) NOT NULL,
    "marca_pieza" VARCHAR(255) NOT NULL,
    "precio_unitario" INTEGER NOT NULL,
    "stock_disponible" INTEGER NOT NULL,
    "stock_minimo" INTEGER NOT NULL,
    FOREIGN KEY ("taller_id") REFERENCES "taller" ("id"),
    FOREIGN KEY ("proveedor_id") REFERENCES "proveedor" ("id")
);

CREATE TABLE IF NOT EXISTS "detalle_mantencion" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "mantencion_id" INTEGER NOT NULL,
    "repuesto_id" INTEGER NOT NULL,
    "cantidad" INTEGER NOT NULL,
    FOREIGN KEY ("mantencion_id") REFERENCES "mantencion" ("id"),
    FOREIGN KEY ("repuesto_id") REFERENCES "repuesto" ("id")
);

CREATE TABLE IF NOT EXISTS "factura" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "mantencion_id" INTEGER NOT NULL,
    "numero_folio" VARCHAR(255) NOT NULL,
    "fecha_emision" DATE NOT NULL,
    "subtotal" INTEGER NOT NULL,
    "impuestos" INTEGER NOT NULL,
    "total" INTEGER NOT NULL,
    "metodo_pago" VARCHAR(255) NOT NULL,
    FOREIGN KEY ("mantencion_id") REFERENCES "mantencion" ("id")
);

CREATE TABLE IF NOT EXISTS "usuario" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "nombre_usuario" VARCHAR(255) NOT NULL,
    "contrasena_hash" VARCHAR(255) NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS "cliente_rut" ON "cliente" ("rut");

CREATE INDEX IF NOT EXISTS "vehiculo_cliente_id" ON "vehiculo" ("cliente_id");

CREATE UNIQUE INDEX IF NOT EXISTS "vehiculo_patente" ON "vehiculo" ("patente");

CREATE UNIQUE INDEX IF NOT EXISTS "automovil_vehiculo_id" ON "automovil" ("vehiculo_id");

CREATE UNIQUE INDEX IF NOT EXISTS "camioneta_vehiculo_id" ON "camioneta" ("vehiculo_id");

CREATE INDEX IF NOT EXISTS "mecanico_taller_id" ON "mecanico" ("taller_id");

CREATE UNIQUE INDEX IF NOT EXISTS "mecanico_codigo_empleado" ON "mecanico" ("codigo_empleado");

CREATE INDEX IF NOT EXISTS "mantencion_vehiculo_id" ON "mantencion" ("vehiculo_id");

CREATE INDEX IF NOT EXISTS "mantencion_mecanico_id" ON "mantencion" ("mecanico_id");

CREATE UNIQUE INDEX IF NOT EXISTS "proveedor_rut_empresa" ON "proveedor" ("rut_empresa");

CREATE INDEX IF NOT EXISTS "repuesto_taller_id" ON "repuesto" ("taller_id");

CREATE INDEX IF NOT EXISTS "repuesto_proveedor_id" ON "repuesto" ("proveedor_id");

CREATE UNIQUE INDEX IF NOT EXISTS "repuesto_codigo_pieza" ON "repuesto" ("codigo_pieza");

CREATE INDEX IF NOT EXISTS "detalle_mantencion_mantencion_id" ON "detalle_mantencion" ("mantencion_id");

CREATE INDEX IF NOT EXISTS "detalle_mantencion_repuesto_id" ON "detalle_mantencion" ("repuesto_id");

CREATE UNIQUE INDEX IF NOT EXISTS "detalle_mantencion_mantencion_id_repuesto_id" ON "detalle_mantencion" ("mantencion_id", "repuesto_id");

CREATE UNIQUE INDEX IF NOT EXISTS "factura_mantencion_id" ON "factura" ("mantencion_id");

CREATE UNIQUE INDEX IF NOT EXISTS "factura_numero_folio" ON "factura" ("numero_folio");

CREATE UNIQUE INDEX IF NOT EXISTS "usuario_nombre_usuario" ON "usuario" ("nombre_usuario");

COMMIT;
