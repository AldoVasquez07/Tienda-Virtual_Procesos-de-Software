from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from modelos.login import gestor_login

app = Flask(__name__, static_folder='../static', template_folder='../templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user, case = gestor_login(email, password)

        if user:
            return jsonify({"message": "Inicio de sesión exitoso", "user": user.__dict__}), 200
        else:
            return jsonify({"message": "Credenciales incorrectas"}), 401


    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
