import bcrypt

from auxiliares.validaciones import texto_obligatorio
from datos.modelos import Usuario
from datos.repositorio import usuario
from negocio.taller import pedir_registro


def hay_usuarios():
    return usuario.existen_usuarios()


def autenticar(nombre_usuario, contrasena):
    registro = usuario.buscar_por_nombre(nombre_usuario.strip().lower())
    contrasena_bytes = contrasena.encode("utf-8")
    if registro and 0 < len(contrasena_bytes) <= 72:
        if bcrypt.checkpw(contrasena_bytes, registro.contrasena_hash.encode("ascii")):
            return registro.id
    return None


def guardar_usuario(nombre_usuario, contrasena, id_usuario=None):
    registro = Usuario() if id_usuario is None else pedir_registro(usuario, id_usuario)
    registro.nombre_usuario = texto_obligatorio(nombre_usuario, "el nombre de usuario").lower()
    if id_usuario is None or contrasena:
        contrasena_bytes = contrasena.encode("utf-8")
        if not 8 <= len(contrasena_bytes) <= 72 or not contrasena.strip():
            raise ValueError("La contraseña debe tener entre 8 y 72 bytes y contener texto.")
        registro.contrasena_hash = bcrypt.hashpw(contrasena_bytes, bcrypt.gensalt()).decode("ascii")
    usuario.guardar(registro)


def datos_usuario(registro):
    return {"id": registro.id, "nombre_usuario": registro.nombre_usuario}


def listar_usuarios():
    return [datos_usuario(registro) for registro in usuario.listar()]


def buscar_usuario(id_usuario):
    return datos_usuario(pedir_registro(usuario, id_usuario))


def eliminar_usuario(id_usuario, id_usuario_actual):
    if id_usuario == id_usuario_actual:
        raise ValueError("La cuenta que inició sesión debe permanecer activa.")
    usuario.eliminar(pedir_registro(usuario, id_usuario))
