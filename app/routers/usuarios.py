from fastapi import APIRouter, HTTPException
from app.database import get_conexion

#vamos a crear la variable para las rutas:
router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

#endpoints: GET, GET, POST, PUT, DELETE, PATCH
@router.get("/")
def obtener_usuarios():
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("SELECT rut,tipo_usuario,p_nombre,s_nombre,p_apellido,s_apellido,direccion,correo, contra FROM usuario")
        usuario = []
        for rut, tipo_usuario, p_nombre, s_nombre, p_apellido, s_apellido, direccion, correo, contra in cursor:
            usuario.append({
                "rut": rut,
                "tipo_usuario": tipo_usuario,
                "p_nombre": p_nombre,
                "s_nombre": s_nombre,
                "p_apellido": p_apellido,
                "s_apellido": s_apellido,
                "direccion": direccion,
                "correo": correo,
                "contra": contra
            })
        cursor.close()
        cone.close()
        return usuario
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.get("/{rut_buscar}")
def obtener_usuario(rut_buscar: str):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("SELECT tipo_usuario,p_nombre,s_nombre,p_apellido,s_apellido,direccion,correo FROM usuario WHERE rut = :rut"
                       ,{"rut": rut_buscar})
        usuario = cursor.fetchone()
        cursor.close()
        cone.close()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {
            "rut": rut_buscar,
            "tipo_usuario": usuario[0],
            "p_nombre": usuario[1],
            "s_nombre": usuario[2],
            "p_apellido": usuario[3],
            "s_apellido": usuario[4],
            "direccion": usuario[5],
            "correo": usuario[6]
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.post("/")
def agregar_usuario(rut:str, tipo_usuario:str, p_nombre:str, s_nombre:str, p_apellido:str, s_apellido:str, direccion:str, correo:str, contra:str):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""
            INSERT INTO usuario
            VALUES(:rut, :tipo_usuario, :p_nombre, :s_nombre, :p_apellido, :s_apellido, :direccion, :correo, :contra)
        """,{"rut":rut, "tipo_usuario":tipo_usuario, "p_nombre":p_nombre, "s_nombre":s_nombre, "p_apellido":p_apellido, "s_apellido":s_apellido, "direccion":direccion, "correo":correo, "contra":contra})
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "usuario agregado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.put("/{rut_actualizar}")
def actualizar_usuario(rut_actualizar:str, p_nombre:str, s_nombre:str, p_apellido:str, s_apellido:str, direccion:str, correo:str):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""
                UPDATE usuario
                SET p_nombre = :p_nombre, s_nombre = :s_nombre, p_apellido = :p_apellido, s_apellido = :s_apellido, direccion = :direccion, correo = :correo
                WHERE rut = :rut
        """, {"p_nombre":p_nombre, "s_nombre":s_nombre, "p_apellido":p_apellido, "s_apellido":s_apellido, "direccion":direccion, "correo":correo, "rut":rut_actualizar})
        if cursor.rowcount==0:
            cursor.close()
            cone.close()
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "Usuario actualizado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.delete("/{rut_eliminar}")
def eliminar_usuario(rut_eliminar: str):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("DELETE FROM usuario WHERE rut = :rut"
                       ,{"rut": rut_eliminar})
        if cursor.rowcount==0:
            cursor.close()
            cone.close()
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "Usuario eliminado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


from typing import Optional

@router.patch("/{rut_actualizar}")
def actualizar_parcial(
    rut_actualizar: str,
    tipo_usuario: Optional[str] = None,
    p_nombre: Optional[str] = None,
    s_nombre: Optional[str] = None,
    p_apellido: Optional[str] = None,
    s_apellido: Optional[str] = None,
    direccion: Optional[str] = None,
    correo: Optional[str] = None,
    contra: Optional[str] = None
):
    try:
        # Verificar si al menos un campo fue proporcionado
        if not any([
            tipo_usuario, p_nombre, s_nombre, p_apellido, 
            s_apellido, direccion, correo, contra
        ]):
            raise HTTPException(status_code=400, detail="Debe enviar al menos 1 dato para actualizar")

        cone = get_conexion()
        cursor = cone.cursor()

        # Preparar campos y valores dinámicamente
        campos = []
        valores = {"rut": rut_actualizar}

        if tipo_usuario:
            campos.append("tipo_usuario = :tipo_usuario")
            valores["tipo_usuario"] = tipo_usuario
        if p_nombre:
            campos.append("p_nombre = :p_nombre")
            valores["p_nombre"] = p_nombre
        if s_nombre is not None:  # Puede ser vacío o nulo
            campos.append("s_nombre = :s_nombre")
            valores["s_nombre"] = s_nombre
        if p_apellido:
            campos.append("p_apellido = :p_apellido")
            valores["p_apellido"] = p_apellido
        if s_apellido is not None:
            campos.append("s_apellido = :s_apellido")
            valores["s_apellido"] = s_apellido
        if direccion:
            campos.append("direccion = :direccion")
            valores["direccion"] = direccion
        if correo:
            campos.append("correo = :correo")
            valores["correo"] = correo
        if contra:
            campos.append("contra = :contra")
            valores["contra"] = contra

        # Ejecutar consulta
        cursor.execute(f"UPDATE usuario SET {', '.join(campos)} WHERE rut = :rut", valores)

        if cursor.rowcount == 0:
            cursor.close()
            cone.close()
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        cone.commit()
        cursor.close()
        cone.close()

        return {"mensaje": "Usuario actualizado con éxito"}

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
