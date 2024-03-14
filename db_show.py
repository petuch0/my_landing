from db import DatabaseManager
try:
    users = DatabaseManager('users.db')
    listuser=users.fetchall("""SELECT * FROM users""")
    print(listuser)
except:
    listuser=[('В базе','нет','пользователей')]
    print(listuser)