from logger_base import logger

class User:

    def __init__(self, id_user=None, username=None, password=None):
        self.__id_user = id_user
        self.__username = username
        self.__password = password

    def __str__(self):
        return(
            f'Id User: {self.__id_user},'
            f'UserName: {self.__username},'
            f'Password: {self.__password}'
        )

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_id_user(self, id_user):
        self.__id_user = id_user

    def get_id_user(self):
        return self.__id_user

    def set_id_user(self, id_user):
        self.__id_user = id_user

if __name__ == '__main__':
    usuario1 = User(1, 'jperez', '123')
    logger.debug(usuario1)
    # # simulando un objeto a insertar de tipo usuario
    # usuario2 = User(username='kgomez', password='543')
    # logger.debug(usuario2)
    # # simular el caso de eliminar un objeto de tipo usuario
    # usuario3 = User(id_user=2)
    # logger.debug(usuario3)
