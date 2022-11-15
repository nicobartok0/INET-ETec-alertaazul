# --  IMPORTES --
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

# -- DEFINICIÓN DE APP COMO OBJETO DE FLASK --
app = Flask(__name__)

# -- CONFIGURACIÓN DE MYSQL --
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'azul_db'
mysql = MySQL(app)

# -- CREAR ÁREA --
@app.route('/crear_area')
def crear_area():
    nombre = request.form['nombre_area']

# -- CREAR USUARIO --
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    nombre_usuario = request.form['nombre_usuario']
    contraseña = request.form['contraseña']
    area = request.form['area']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO usuarios (nombre_usuario, contraseña, id_area_fk) VALUES (%s, %s, %s)', (nombre_usuario, contraseña, area))

# -- VER USUARIOS --
@app.route('/ver_usuarios')
def ver_usuarios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_usuario FROM usuarios')
    usuarios = cur.fetchall()
    return(jsonify(usuarios))

# -- VER ALERTAS --
@app.route('/ver_alertas')
def ver_alertas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alertas')
    alertas = cur.fetchone()
    return(jsonify(str(alertas)))




# -- BUCLE PRINCIPAL DE LA APP --
if (__name__) == '__main__':
    app.run(port=5000, debug=True)
