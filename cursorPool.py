from logger_base import log
from conexion import Conexion



class CursorDePool:
    def __init__(self):
        self._conexion = None
        self._Cursor = None

    def __enter__(self):
        log.debug('f inicio metodo  __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._Cursor = self._conexion.cursor()
        return self._Cursor

    def __exit__(self, exception, valor_exception, detail_exception):
        log.debug(f'se ejecuta el metodo __exit__')
        if valor_exception :
            self._conexion.rollback()
            log.error(f'ocurrio un error: {valor_exception}, {exception}, {detail_exception}')
        else:
            self._conexion.commit()
            log.debug(f'se hizo un commit')
        self._Cursor.close()
        Conexion.liberarConexion(self._conexion)

#bloque de pruebas

if __name__ == '__main__':
    with CursorDePool() as cursor:
        log.debug(f'dentro del with')
        cursor.execute('SELECT * FROM "Personas"')
        log.debug(cursor.fetchall())
