
from persona import Persona

from cursorPool import *

""" esta clase busca hacer uso de las transacciones con la bd
es decir, pasar los querys de la o separar el ingreso de datos 
ya que no se ingresan a traves de la clase persona, ahi solo 
se encuentran los atributos que seran ingresados y esos son pasados 
al patron o clase dao para que los ingrese a traves de sus querys 
mediante el CRUD"""


class PersonaDAO:
    """
    DAO (Data Access Object)
    posteriormente
    CRUD (Create-Read-Update-Delete)
    """
    _SELECCIONAR = 'SELECT * FROM "Personas" ORDER BY "idPersona"'
    _INSERTAR = 'INSERT INTO "Personas"(nombre, apellido, correo) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE "Personas" SET nombre = %s, apellido = %s, correo = %s WHERE "idPersona"=%s'
    _ELIMINAR = 'DELETE FROM "Personas" WHERE "idPersona"=%s'

    # creamos las variables junto a las querys a utilizar (CRUD)
    # posterior, creamos los metodos de la clase con cada funcion del crud
    # primero seleccionar, insertar, actualizar y eliminar
    # tambien llamamos a la clase conexion para verificar que este conectado
    # a la bd, usamos la clase log con sus mensajes para ver si existen errores
    # creamos e instanciamos la conexion y su cursor para disparar la conexion y las querys
    # en cada metodo usamos with para hacer apertura y cierre de la conexion (commit)
    # tambien instanciamos el cursor en cada una
    @classmethod
    def seleccionar(cls):
        with CursorDePool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDePool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.correo)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDePool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.correo, persona.idPersona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDePool() as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount


# bloque de pruebas para el CRUD
if __name__ == '__main__':

    # Insertar un registro
    persona1 = Persona(nombre='Carlos', apellido='Arancibia', correo='carancibia@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

    # Actualizar un registro
    # persona1 = Persona(1,'Juan Carlos', 'Juarez', 'cjjuarez@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar un registro
    # persona1 = Persona(id_persona=20)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')


