
import logging as log

#esta es la seccion de errores que nos mostrara el programa cuando exista alguno
#mas abajo definimos la seriedad o el nivel del error y este sera impreso cuando exista
#tambien, daremos unos atributos a los errores para saber con exactitud cuando y que son
#especificamos el formato, el level, el archivo(en caso de ser un file) la linea y el mensaje
#asi podremos resolver el problema excato que nos avisa el programa y logging
#con handlers le indicamos que detalle en un archivos


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')