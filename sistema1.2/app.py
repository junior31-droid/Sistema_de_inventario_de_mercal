from flask import Flask, flash , render_template, request, redirect, send_from_directory , url_for , session
import flask
from flask_sqlalchemy import SQLAlchemy
import os
import mysql.connector
from mysql.connector import Error
                              
app= Flask (__name__)
app.secret_key= "my_super_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/// my_datebase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

db_config = {
    'host': 'localhost',
    'database': 'inventario',
    'user': 'root',
    'password': ''
}

def get_bd_connection():
        try:
            conexion= mysql.connector.connect(**db_config)
            return conexion
        except Error as e:
            flask(f"Error para conectar a MySQL: {e}", 'danger')
            return None
        
class User(db.Model):
     id= db.Column(db.Integer, primary_key=True)
     username= db.Column(db.String(80), unique=True, nullable=False)
     email= db.Column(db.String(130), unique=True, nullable=False)
     password= db.Column(db.String(120), nullable=False)

#para las imagenes 
@app.route('/static/<path:filename>')
def serve_static(filename):
     return send_from_directory(os.path.join(app.root_path, "static" ),filename)
     

with app.app_context():
     db.create_all()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method =="POST":
        user = User.query.filter_by(username=request.form['usuario']).first()
        if user and user.password == request.form['contrasena']:
            session['username'] = user.username
            return redirect(url_for('home'))
        flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/")
def home():
     if "username" not in session:
         return redirect(url_for("login"))
     return render_template("home.html")


@app.route("/activosdigitales")
def activos_digitales():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("activosdigitales.html")

@app.route("/activoshardware")
def activos_hardware():
    if "username" not in session:
        return redirect(url_for('login'))
    return render_template("activoshardware.html")


if __name__ == "__main__":
    app.run(debug=True) 
