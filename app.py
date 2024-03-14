from flask import Flask, render_template,request
from db import DatabaseManager
app = Flask(__name__)
users = DatabaseManager('users.db')
users.create_tables()
@app.route("/")
def home():
    return render_template('single.html')





@app.route("/read_form", methods=['POST'])
def read_form():
    users = DatabaseManager('users.db')
    users.create_tables()
    data = request.form
    userEmail = data['userEmail']
    userNmae = data['name']
    userPhone = data['phone']
    dictsend = (userEmail, userNmae, userPhone)
    users.query('''INSERT INTO Users VALUES (?,?,?)''', dictsend)
    print(dictsend)
    return render_template('single.html')

@app.route("/show")
def show():
    try:
        users = DatabaseManager('users.db')
        listuser=users.fetchall("""SELECT * FROM users""")
        print(listuser)
    except:
        listuser=[('В базе','нет','пользователей')]
    return render_template('show.html', listuser=listuser)


if __name__=="__main__":
    app.run(debug=True)


