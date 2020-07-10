from logger_base import logger
from psycopg2 import pool
import sys


class Connection:

    __DATABASE = "test"
    __USERNAME = "postgres"
    __PASSWORD = "admin123"
    __DB_PORT = "5432"
    __HOST = "127.0.0.1"
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def getPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    port=cls.__DB_PORT,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    database=cls.__DATABASE
                )
                logger.debug(f'Pool Creation Successful')
                return cls.__pool
            except Exception as e:
                logger.error(f'Erro Pool Creating => {e}')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        logger.debug(f'Bonnection Obtained by Pool => {connection}')
        return connection

    @classmethod
    def liberateConnection(cls, connection):
        cls.getPool().putconn(connection)
        logger.debug(f'Return Pool Connection')
        logger.debug(f'Pool State => {cls.__pool}')

    @classmethod
    def closeConnections(cls):
        cls.getPool().closeall()
        logger.debug(f'Close Connections')


if __name__ == '__main__':
    connection = Connection.getConnection()
    Connection.liberateConnection(connection)
    Connection.closeConnections()
