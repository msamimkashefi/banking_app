from application import app
from flask import render_template, request, jsonify, json
from application.controllers import user_controller, account_controller, transaction_controller




user__controller = user_controller.UserController()
account__controller = account_controller.AccountController()
@app.route("/")

def index_view():
    return render_template('index.html')

@app.route("/layout")
def layout_view():
    return render_template('layout.html')

@app.route("/register-user")
def register_view():
    return render_template('register.html')

@app.route("/transaction")
def transaction_view():
    return render_template('transactions.html')


@app.route("/materialize.min.js")
def materialize_js():
    return render_template('js/materialize.min.js')

@app.route("/materialize.min.css")
def materialize_css():
    return render_template("css/materialize.min.css")

@app.route("/bootstrap.min.js")
def bootstrap_js():
    return render_template('js/bootsrap.min.js')

@app.route("/bootsrap.min.css")
def bootstrap_css():
    return render_template("css/bootstrap.min.css")

@app.route("/jquery")
def jquery():
    return render_template('js/jquery-3.7.1.js')

@app.route("/register-account-holder", methods = ['POST'])
def register_account_holder():
    if request.method == 'POST':
        # data = json.loads(request.data)
        data = request.form
        return user__controller.register_user(data)
@app.route('/load_all_users', methods = ['POST'])
def load_all_users():
    return user__controller.get_all_users()

@app.route('/load_users_accounts_reg_view', methods = ['POST'])
def load_users_accounts_reg_view():
    data = request.form
    return account__controller.get_users_accounts(data)

@app.route('/create-account', methods = ['POST'])
def create_accounts():
    data = request.form
    return account__controller.create_account(data)


@app.route('/load_users_accounts_tr_view', methods = ['POST'])
def load_users_accounts_tr_view():
    data = request.form
    return account__controller.get_accounts(data)


@app.route('/load_accounts_balance', methods = ['POST'])
def load_account_balance():
    data = request.form
    return account__controller.get_accounts_balance(data)


@app.route('/execute_transaction', methods = ['POST'])
def execute_transaction():
    data = request.form
    return account__controller.execute_transaction(data)


@app.route('/load_transactions', methods = ['POST'])
def load_transactions():
    data = request.form
    return account__controller.load_transactions(data)




