
from logger_base import log


""" creamos la clase persona dandole los atributos que son similares
a los de la base de datos para tener coherencia en los datos ingresados
como seran atributos privados usamos getter and setter para poder
llamarlos desde la clase PersonaDao e insertar datos y usarlos en una lista
"""

class Persona:
    def __init__(self, idPersona=None , nombre=None, apellido=None, correo=None):
        self._idPersona = idPersona
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo

    # usamos el decorador STR para llamar los strings ingresados
    # idPersona, nombre, apellido y correo
    def __str__(self):
        return f'''
            idPersona: {self._idPersona}
            nombre: {self._nombre}
            apellido: {self._apellido}
            correo: {self._correo}
        '''

    # aplicamos los getters % setters para acceder a los atributos privados de la clase
    @property
    def idPersona(self):
        return self._idPersona
    @idPersona.setter
    def idPersona(self, idPersona):
        self._idPersona = idPersona


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

# bloque de pruebas***** recordad que usamos log para ver la informacion ingresada o errores
# if __name__ == '__main__':
#     persona1 = Persona('Juan', 'Perez', 'jperez@mail.com')
#     log.debug(persona1)
#     # Simular un insert
#     persona1 = Persona(nombre='Juan', apellido='Perez', correo='jperez@mail.com')
#     log.debug(persona1)
#     # Simular un delete
#     persona1 = Persona(idPersona=2)
#     log.debug(persona1)
#     log.debug(persona1)