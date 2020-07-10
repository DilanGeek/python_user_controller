from user_dao import UserDao
from logger_base import logger
from user import User

option = None
while option != '5':
    print('Options')
    print('1. View Users:')
    print('2. Add User')
    print('3. Update User')
    print('4. Delete User')
    print('5. Exit')
    option = input('Inser an option (1-5): ')
    if option == '1':
        # view users
        users = UserDao.select()
        for user in users:
            print(user)
            logger.debug(user)
    elif option == '2':
        # insert user
        username = input('Insert username: ')
        password = input('Insert password: ')

        user = User(username=username, password=password)
        insert_data = UserDao.insert(user)
        logger.debug(f'User insert {insert_data}')
    elif option == '3':
        # update user
        id_user = input('Insert user to update: ')
        username = input('Insert new username: ')
        password = input('Insert new password: ')

        user = User(id_user,username,password)
        update_user = UserDao.update(user)
        logger.debug(f'User Update: {update_user}')
    elif option == '4':
        # delete user
        id_user = input('Insert user to delete: ')
        
        user = User(id_user=id_user)
        delete_user = UserDao.delete(user)
        logger.debug(f'User delete: {delete_user}')
else:
    print('Close Application')
