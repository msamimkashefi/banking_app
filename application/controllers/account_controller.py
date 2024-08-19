from datetime import datetime
import hashlib

from flask import jsonify

from application import mysql, FERNET


class AccountController:


    def get_new_acc_number(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT max(account_number) FROM account")
        rs = cur.fetchall()
        mysql.connection.commit()
        return str(int(rs[0][0]) +1)


    #loads a specific  users accounts , user's name and the next available account number for new account creation
    def get_users_accounts(self, user):
            #Get a new Account Number (required in user accounts modal, user registration page)
            cur = mysql.connection.cursor()
            cur.execute("SELECT (max(account_number) + 1) FROM account")
            rr = cur.fetchall()
            mysql.connection.commit()
            new_account_number =  str(int(rr[0][0]))

            #User of Accounts
            user_id = FERNET.decrypt(user['user'].encode())


            cur = mysql.connection.cursor()
            cur.execute("SELECT  first_name, last_name FROM user WHERE id = %s", (user_id,))
            rrr = cur.fetchall()
            mysql.connection.commit()
            user_name = ()
            if rrr:
                user_name = rrr[0][0] + " " + rrr[0][1]


            #get accounts of user
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM account WHERE account_holder = %s", (user_id,))
            rs = cur.fetchall()
            mysql.connection.commit()
            accounts = []
            for r in rs:
                accounts.append({
                    'account': FERNET.encrypt(str(r[0]).encode()).decode(),
                    'account_number': r[1],
                    'balance': r[2],
                    'type': r[4],
                    'holder': FERNET.encrypt(str(r[3]).encode()).decode(),
                    'opening_date': r[5],
                    'status': r[6]
                })
            data = {'accounts': accounts, "new_acc_num": new_account_number, "account_holder_name": user_name}
            return jsonify(data);
        # try:
        # except Exception as e:
        #     return ("Problem loading from db: " + str(e))


    def create_account(self, acc_data):
        acc_type = acc_data['type']
        balance = acc_data['balance']
        user = FERNET.decrypt(acc_data['holder'].encode())
        new_acc_number = self.get_new_acc_number()

        cur = mysql.connection.cursor()
        query = "INSERT INTO account (account_number, balance, account_holder, type, opening_time, account_status) VALUES (%s, %s, %s, %s, %s , %s)"
        values = (new_acc_number, balance, user, acc_type, datetime.now(), 'active')
        rv = cur.execute(query, values)
        mysql.connection.commit()
        return jsonify(rv)

    #returns a specifc user's accounts if a users is specified or it will return all accounts
    def get_accounts(self, holder=None):
        #holder of Accounts

        cur = mysql.connection.cursor()
        if holder:
            holder_id = FERNET.decrypt(holder['holder'].encode())
            cur.execute("SELECT * FROM account WHERE account_holder = %s", (holder_id,))
        else:
            cur.execute("SELECT * FROM account")
        rv = cur.fetchall()
        mysql.connection.commit()
        user_name = ()
        accounts = []
        for r in rv:
            accounts.append({
                'account': FERNET.encrypt(str(r[0]).encode()).decode(),
                'account_number': r[1],
                'balance': r[2],
                'type': r[4],
                'holder': FERNET.encrypt(str(r[3]).encode()).decode(),
                'opening_date': r[5],
                'status': r[6]
            })
        return jsonify(accounts)

    def get_accounts_balance(self,account):
        cur = mysql.connection.cursor()
        if account:
            account_id = FERNET.decrypt(account['account'].encode())
            cur.execute("SELECT balance FROM account WHERE id = %s", (account_id,))
            rv = cur.fetchall()
            mysql.connection.commit()
            return {'account': account, "balance": rv[0][0]}
        else:
            return None


    def execute_transaction(self,data):
        if data:
            tr_amount = data['tr_amount']
            r_account = data['r_account']
            s_account = data['s_account']
            note = data["note"]

            cur = mysql.connection.cursor()
            s_account_id = FERNET.decrypt(s_account.encode())
            cur.execute("SELECT id FROM account WHERE account_number = %s", (r_account,))
            rv = cur.fetchall()
            mysql.connection.commit()
            if rv:
                r_account_id = rv[0][0]
                cur.execute("UPDATE account SET balance = (balance - %s)  WHERE id = %s", (tr_amount, s_account_id))
                rv = cur.fetchall()
                mysql.connection.commit()

                cur.execute("UPDATE account SET balance = (balance + %s)  WHERE id = %s", (tr_amount, r_account_id))
                rv = cur.fetchall()
                mysql.connection.commit()

                cur.execute("SELECT MAX(tr_number) FROM transaction")
                rv = cur.fetchall()
                mysql.connection.commit()
                if rv[0][0]:
                    tr_number = int(rv[0][0]) + 1
                else:
                    tr_number = 1


                query = "INSERT INTO transaction (tr_number, tr_amount, tr_time, source_account, destination_account, transfered_by, note) VALUES (%s, %s, %s, %s, %s, NULL , %s)"
                values = (tr_number, tr_amount, datetime.now(), s_account_id, r_account_id, note)
                rv = cur.execute(query, values)
                mysql.connection.commit()
                return jsonify(1)
            else:
                return "Receiving account not found"
        else:
            return "No Data"

    #returns transactions of a user if user specified or all transactions
    def load_transactions(self, user):
        cur = mysql.connection.cursor()

        # if user:
        #     user_id = FERNET.decrypt(user['user'].encode())
        #     cur.execute("SELECT tr.* FROM transaction tr LEFT JOIN account sac ON tr.source_account = sac.id  LEFT JOIN account rac ON tr.destination_account = rac.id  WHERE tr.transfered_by = %s", (user_id,))
        # else:
        cur.execute("SELECT tr.*, sac.account_number as sender, rac.account_number as receiver FROM transaction tr LEFT JOIN account sac ON tr.source_account = sac.id  LEFT JOIN account rac ON tr.destination_account = rac.id")
        rv = cur.fetchall()
        mysql.connection.commit()
        # user_name = ()
        transactions = []
        for r in rv:
            transactions.append({
                'transaction': FERNET.encrypt(str(r[0]).encode()).decode(),
                'tr_number': r[1],
                'tr_amount': r[2],
                'tr_time': r[3],
                'transfered_by': r[6],
                'sending_account': r[8],
                'receiving_account': r[9],
                'note': r[7],
            })
        return jsonify(transactions)
