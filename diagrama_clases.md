# Diagrama de clases del taller

```mermaid
classDiagram
    class ModelBase {
        +int id
    }
    ModelBase <|-- Taller
    class Taller {
        +str nombre_sucursal
        +str direccion
        +str telefono
        +time horario_apertura
        +time horario_cierre
    }
    ModelBase <|-- Cliente
    class Cliente {
        +str rut
        +str nombre
        +str telefono
        +str email
        +str direccion
    }
    ModelBase <|-- Mecanico
    class Mecanico {
        +Taller taller
        +str codigo_empleado
        +str nombre
        +str especialidad
        +int anios_experiencia
    }
    ModelBase <|-- Vehiculo
    class Vehiculo {
        +Cliente cliente
        +str patente
        +str marca
        +str modelo
        +int anio
        +int kilometraje
    }
    ModelBase <|-- Camioneta
    class Camioneta {
        +Vehiculo vehiculo
        +int capacidad_carga_kg
        +str tipo_traccion
        +bool tiene_cupula
    }
    ModelBase <|-- Automovil
    class Automovil {
        +Vehiculo vehiculo
        +int cantidad_puertas
        +str tipo_maletero
    }
    ModelBase <|-- Proveedor
    class Proveedor {
        +str rut_empresa
        +str razon_social
        +str contacto
    }
    ModelBase <|-- Repuesto
    class Repuesto {
        +Taller taller
        +Proveedor proveedor
        +str codigo_pieza
        +str nombre_pieza
        +str marca_pieza
        +int precio_unitario
        +int stock_disponible
        +int stock_minimo
    }
    ModelBase <|-- Mantencion
    class Mantencion {
        +Vehiculo vehiculo
        +Mecanico mecanico
        +date fecha_ingreso
        +date fecha_salida (opcional)
        +str tipo_servicio
        +str observaciones (opcional)
        +int costo_mano_obra
        +str estado_actual
    }
    ModelBase <|-- DetalleMantencion
    class DetalleMantencion {
        +Mantencion mantencion
        +Repuesto repuesto
        +int cantidad
    }
    ModelBase <|-- Factura
    class Factura {
        +Mantencion mantencion
        +str numero_folio
        +date fecha_emision
        +int subtotal
        +int impuestos
        +int total
        +str metodo_pago
    }
    ModelBase <|-- Usuario
    class Usuario {
        +str nombre_usuario
        +str contrasena_hash
    }
    Taller "1" -- "0..*" Mecanico : emplea
    Taller "1" -- "0..*" Repuesto : almacena
    Cliente "1" -- "0..*" Vehiculo : posee
    Vehiculo "1" -- "0..1" Automovil : detalle
    Vehiculo "1" -- "0..1" Camioneta : detalle
    Vehiculo "1" -- "0..*" Mantencion : historial
    Mecanico "1" -- "0..*" Mantencion : ejecuta
    Proveedor "1" -- "0..*" Repuesto : suministra
    Mantencion "1" -- "0..*" DetalleMantencion : incluye
    Repuesto "1" -- "0..*" DetalleMantencion : se usa en
    Mantencion "1" -- "0..1" Factura : genera
```

Cada modelo hereda el identificador y la conexión de `ModelBase`. El detalle de un vehículo puede ser de automóvil o camioneta. El cliente de una factura se obtiene a través de la mantención y el vehículo. El taller que atendió al cliente se obtiene a través de la mantención y el mecánico.
