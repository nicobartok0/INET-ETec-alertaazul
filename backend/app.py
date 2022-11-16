# --  IMPORTES --
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

# -- DEFINICIÓN DE APP COMO OBJETO DE FLASK --
app = Flask(__name__)

# -- CONFIGURACIÓN DE MYSQL --
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inet_db'
mysql = MySQL(app)

# -- CREAR ÁREA --
@app.route('/crear_area', methods=['POST'])
def crear_area():
    content = request.json['nombre_area']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO areas(nombre) VALUES ('+ '"' + content + '"' +')')
    mysql.connection.commit()
    cur.close()
    return(jsonify(content))

# -- CREAR PERSONA --
@app.route('/crear_persona', methods=['POST'])
def crear_persona():
    nombre = request.json['nombre_persona']
    apellido = request.json['apellido_persona']
    dni = request.json['dni_persona']
    tipo = request.json['tipo_persona']
    cur = mysql.connection.cursor()
    query = 'INSERT INTO personas(nombre_persona, apellido_persona, dni_persona, tipo_persona) VALUES ('+'"'+nombre+'",'+'"'+apellido+'",'+dni+','+'"'+tipo+'"'+')'
    print(query)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return(jsonify('Ok!'))

# -- CREAR USUARIO --
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    nombre_usuario = request.json['nombre_usuario']
    contraseña = request.json['contraseña']
    area = request.json['area']
    dni_persona = request.json['dni_persona']
    cur = mysql.connection.cursor()
    cur.execute('SELECT id_persona FROM personas WHERE dni_persona = %s' % (dni_persona))
    id_persona = cur.fetchone()
    id_persona_str = str(id_persona)
    id_persona_str = id_persona_str.replace('(', '')
    id_persona_str = id_persona_str.replace(')', '')
    id_persona_str = id_persona_str.replace(',', '')
    cur.execute('SELECT id FROM areas WHERE nombre = "' + '%s' % (area) + '"')
    id_area = cur.fetchone()
    id_area_str = str(id_area)
    id_area_str = id_area_str.replace('(', '')
    id_area_str = id_area_str.replace(')', '')
    id_area_str = id_area_str.replace(',', '')
    query = 'INSERT INTO usuarios(nombre_usuario, id_persona_fk, id_area_fk, contraseña) VALUES ('+'"'+nombre_usuario+'",'+id_persona_str+','+id_area_str+','+'"'+contraseña+'"'+')'
    print(query)
    cur.execute(query)
    mysql.connection.commit()
    return(jsonify("Ok!"))

# -- VER PERSONAS --
def personObj(row):
    return {
        "id" : row[0],
        "nombre_persona" : row[1],
        "apellido_persona" : row[2],
        "dni_persona" : row[3],
        "tipo_persona" : row[4]
    }

@app.route('/ver_personas')
def ver_personas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personas')
    usuarios = cur.fetchall()
    usuarios = [personObj(x) for x in usuarios]
    return(jsonify(usuarios))


# -- VER USUARIOS --
@app.route('/ver_usuarios')
def ver_usuarios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_usuario FROM usuarios')
    usuarios = cur.fetchone()
    cur.close()
    return(jsonify(usuarios))

# -- VER ALERTAS --
@app.route('/ver_alertas')
def ver_alertas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alertas')
    alertas = cur.fetchone()
    cur.close()
    return(jsonify(str(alertas)))




# -- BUCLE PRINCIPAL DE LA APP --
if (__name__) == '__main__':
    app.run(port=5000, debug=True)
