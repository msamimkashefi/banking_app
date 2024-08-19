from flask import Flask
import hashlib

from application import app, mysql


class User:
    table = 'user'

    def create(user):
        first_name = user['first_name']
        last_name = user['last_name']
        birth_date = user['birth_date']
        nationality = user['nationality']
        current_address = user['current_address']
        email = user['email_address']
        phone = user['phone_number']
        password = user['pass']
        h_password = hashlib.md5(password.encode())

        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user"
                        " first_name = \"" + first_name + " \" "
                        "last_name = \"" + last_name + "\" "
                        "birth_date = \"" + birth_date + "\" "
                        "nationality = \"" + nationality + "\" "
                        "current_address = \"" + current_address + "\" "
                        "email = \"" + email + "\" "
                        "phone = \"" + phone + "\" "
                        "password = \"" + h_password + "\" "
                        )
            rv = cur.execute()
            print(rv)
            return "OK"
