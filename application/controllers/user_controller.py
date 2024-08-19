from datetime import datetime
import hashlib
import time
from logging import DEBUG
from venv import logger

from flask_mysqldb import MySQL
from flask import jsonify, json
from application import app,mysql,FERNET

class UserController:

    def register_user(self, user):
        # validate data
        first_name = user['first_name']
        last_name = user['last_name']
        birth_date = user['birth_date']
        nationality = user['nationality']
        current_address = user['current_address']
        email = user['email']
        phone = user['phone']
        password = user['pass']
        h_password = hashlib.md5(password.encode()).hexdigest()
        with app.app_context():
            cur = mysql.connection.cursor()
            try:
                query = "INSERT INTO user(first_name, last_name, birth_date, nationality, current_address, email, phone, password, created_at, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s)"
                values = (first_name, last_name, birth_date, nationality, current_address, email, phone, h_password , datetime.now(), "ac_holder" )
                rv = cur.execute(query,values)
                mysql.connection.commit()

                return jsonify(rv)
            except Exception as e:
                return ("Problem inserting into db: " + str(e))
            # cur.execute("INSERT INTO user"
            #             " first_name = \"" + first_name + " \" "
            #             "last_name = \"" + last_name + "\" "
            #             "birth_date = \"" + birth_date + "\" "
            #             "nationality = \"" + nationality + "\" "
            #             "current_address = \"" + current_address + "\" "
            #             "email = \"" + email + "\" "
            #             "phone = \"" + phone + "\" "
            #             "password = \"" + h_password + "\" "
            #             "created_by = NULL "
            #             "created_at = \"" + time.strftime("%Y-%m-%D %H:%M:%S") + "\" "
            #             "type = \"ac_holder\" "
            #             )


    def get_all_users(self):
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM user")
            rs = cur.fetchall()
            mysql.connection.commit()
            users = [];
            for r in rs:
                users.append({
                    'user': FERNET.encrypt(str(r[0]).encode()).decode(),
                    'id': r[0],
                    'first_name': r[1],
                    'last_name': r[2],
                    'email': r[3],
                    'phone': r[4],
                    'created_at': r[7],
                    'type': ("SysAdmin" if r[8] == 'admin' else "Account Holder"),
                    'birth_date': r[9],
                    'nationality': r[10],
                    'current_address': r[11]
                })

            return jsonify(users);
        except Exception as e:
            return ("Problem loading from db: " + str(e))



