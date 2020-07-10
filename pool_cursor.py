from connection import Connection
from logger_base import logger


class PoolCursor:

    def __init__(self):
        self.__conn: None
        self.__cursor: None

    def __enter__(self):
        self.__conn = Connection.getConnection()
        self.__cursor = self.__conn.cursor()
        logger.debug(f'Start With method ')
        return self.__cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug(f'Execute Exit Method')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Exception => {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit Transaction')
        self.__cursor.close()
        Connection.liberateConnection(self.__conn)


if __name__ == '__main__':
    with PoolCursor() as cursor:
        cursor.execute('SELECT * FROM users')
        logger.debug(cursor.fetchall())
        
