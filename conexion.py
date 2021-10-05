from psycopg2 import pool

from logger_base import log

#esta clase administra la conexion  la base de datos
#corrobora los valores, ip, bd y password para conectarnos
#a pgadmin4 o por consola
#ademas crearemos los metodos para crear un pool de conexion
#estos metodos nos crean aperturas para obtener un pool de conexion
#obtener la conexion bd->pool
#liberar conexiones del pool y a la vez cerrarla despues de liberarla
#para que otros usuarios puedan tomarla

class Conexion:
    _DATABASE = 'Proyecto'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _min_con = 1
    _max_con = 5
    pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.pool is None:
            try:
                cls.pool = pool.SimpleConnectionPool(cls._min_con, cls._max_con,
                                                     host=cls._HOST,
                                                     user=cls._USERNAME,
                                                     password=cls._PASSWORD,
                                                     database=cls._DATABASE,
                                                     port=cls._DB_PORT
                                                     )
                log.debug(f'conexion exitosa...')
                return cls.pool
            except Exception as e:
               log.error(f'ocurrio un error: {e}')
        else:
            return cls.pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f' se obtuvo la conexion: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'se ha liberado una conexion: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        log.debug(f' se han cerrado las conexiones')

#bloque de pruebas
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    conexion3 = Conexion.obtenerConexion()
