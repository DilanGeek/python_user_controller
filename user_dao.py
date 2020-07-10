from user import User
from pool_cursor import PoolCursor
from logger_base import logger


class UserDao:

    __SELECT = 'SELECT * FROM users ORDER BY id_user'
    __INSERT = 'INSERT INTO users(username,password) VALUES(%s,%s)'
    __UPDATE = 'UPDATE users SET username=%s, password=%s WHERE id_user=%s'
    __DELETE = 'DELETE FROM users WHERE id_user = %s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT))
            cursor.execute(cls.__SELECT)
            data = cursor.fetchall()
            users = []
            for user in data:
                user = User(user[0], user[1], user[2])
                users.append(user)
            return users

    @classmethod
    def insert(cls, user):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            logger.debug(f'Add User => {user}')
            values = (user.get_username(), user.get_password())
            cursor.execute(cls.__INSERT, values)
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.debug(f'Update User => {user}')
            values = (user.get_username(),
                      user.get_password(), user.get_id_user())
            cursor.execute(cls.__UPDATE, values)
            return cursor.rowcount

    @classmethod
    def delete(cls, user):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.debug(f'Delete User => {user}')
            values = (user.get_id_user(),)
            cursor.execute(cls.__DELETE, values)
            return cursor.rowcount


if __name__ == '__main__':
    # select users
    # users = UserDao.select()
    # for user in users:
    #     print(user)
    #     logger.debug(user)

    # insert user
    # user = User(username='dilangeek', password='admin123')
    # data_insert = UserDao.insert(user)
    # logger.debug(f'User insert => {data_insert}')

    # update user
    # user = User(1, 'saaidgeek', 'admin123')
    # update_user = UserDao.update(user)
    # logger.debug(f'User Update: {update_user}')

    # eliminar un registro existente
    # user = User(id_user=2)
    # user_delete = UserDao.delete(user)
    # logger.debug(f'User Delete: {user_delete}')
