from flask import Flask, request
from flask_mysqldb import MySQL

from cryptography.fernet import Fernet


app = Flask(__name__)


app.config['SECRET_KEY'] = 'dfklsjLKSDJFOJe0fsDF()#&)(JFsjr3098jslkJDLKFJ#))(@()@#EOFDLFkjrf09jOF)$(#FJpfj2349jPIOSJDF)(@$J'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bank'

#create a mysql db object used in all controllers and models
mysql = MySQL(app)

#create encryption key and save to a file, use for data encryption and decryption
# ENC_KEY = Fernet.generate_key()
# with open("secret.key", "wb") as key_file:
#      key_file.write(ENC_KEY)
ENC_KEY = open("secret.key").readline()
FERNET = Fernet(ENC_KEY)


#
# with app.app_context():
#     cur = mysql.connection.cursor()
#     cur.execute("""SELECT first_name, last_name FROM users""")
#     rv = cur.fetchall()
#     print(rv)


from application import routes


