# --  IMPORTES --
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import datetime, json

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
    return(jsonify('Ok!'))

# -- CREAR PERSONA --
@app.route('/crear_persona', methods=['POST'])
def crear_persona():
    nombre = request.json['nombre_persona']
    apellido = request.json['apellido_persona']
    dni = request.json['dni_persona']
    cur = mysql.connection.cursor()
    query = 'INSERT INTO personas(nombre_persona, apellido_persona, dni_persona) VALUES ('+'"'+nombre+'",'+'"'+apellido+'",'+dni+')'
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
    rol = request.json['rol']
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
    query = 'INSERT INTO usuarios(nombre_usuario, id_persona_fk, id_area_fk, contraseña, rol) VALUES ('+'"'+nombre_usuario+'",'+id_persona_str+','+id_area_str+','+'"'+contraseña+'",'+'"'+rol+'"'+')'
    print(query)
    cur.execute(query)
    mysql.connection.commit()
    return(jsonify("Ok!"))

# -- CREAR FICHAS --
@app.route('/crear_ficha', methods=['POST'])
def crear_ficha():
    dni_paciente = request.json['dni_paciente']
    peso = request.json['peso']
    temperatura = request.json['temperatura']
    presion = request.json['presion']
    enfermedades_preexistentes = request.json['enfermedades_preexistentes']
    observaciones = request.json['observaciones']
    cur = mysql.connection.cursor()
    dni_paciente = str(dni_paciente)
    cur.execute('SELECT id_persona FROM personas WHERE dni_persona = ' + dni_paciente)
    id_persona_fk = cur.fetchone()
    id_persona_str = str(id_persona_fk)
    id_persona_str = id_persona_str.replace('(', '')
    id_persona_str = id_persona_str.replace(')', '')
    id_persona_str = id_persona_str.replace(',', '')
    peso = str(peso)
    temperatura = str(temperatura)
    presion = str(presion)
    query = 'INSERT INTO fichas(id_persona_fk, peso, temperatura, presion, enfermedades_preexistentes, observaciones) VALUES ('+id_persona_str+','+peso+','+temperatura+','+presion+',"'+enfermedades_preexistentes+'","'+observaciones+'")'
    cur.execute(query)
    mysql.connection.commit()
    return(jsonify('Ok!'))

# -- EMITIR ALERTA --
@app.route('/emitir_alerta', methods=['POST'])
def emitir_alerta():
    nombre_usuario = request.json['nombre_usuario']
    origen = request.json['origen']
    tipo = request.json['tipo']
    cur = mysql.connection.cursor()
    cur.execute('SELECT id_usuario FROM usuarios WHERE nombre_usuario = "' + nombre_usuario +'"')
    id_usuario_fk = cur.fetchone()
    id_usuario_str = str(id_usuario_fk)
    id_usuario_str = id_usuario_str.replace('(', '')
    id_usuario_str = id_usuario_str.replace(')', '')
    id_usuario_str = id_usuario_str.replace(',', '')
    query = 'INSERT INTO alertas(id_usuario_fk, origen, hora_inicio, fecha_inicio, tipo) VALUES ("'+id_usuario_str+'","'+origen+'", DATE_FORMAT(NOW(),"%H%i%s"), DATE_FORMAT(NOW(),"%Y%m%d"),"'+tipo+'")'
    print(query)
    cur.execute(query)
    mysql.connection.commit()
    return(jsonify('Ok!'))

# -- DAR DE ALTA ALERTA --
@app.route('/dar_de_alta', methods=['PUT'])
def dar_de_alta():
    id_alerta = request.json['id_alerta']
    cur = mysql.connection.cursor()
    id_alerta_str = str(id_alerta)
    id_alerta_str = id_alerta_str.replace('(', '')
    id_alerta_str = id_alerta_str.replace(')', '')
    id_alerta_str = id_alerta_str.replace(',', '')
    query = 'UPDATE alertas SET estado = "Atendido", hora_fin = DATE_FORMAT(NOW(),"%H%i%s"), fecha_fin = DATE_FORMAT(NOW(),"%Y%m%d") WHERE id_alerta = '+id_alerta_str
    cur.execute(query)
    mysql.connection.commit()
    return(jsonify('Ok!'))



# -- VER ÁREAS
def areaObj(row):
    return {
        "id" : row[0],
        "nombre" : row[1]
    }
@app.route('/ver_areas')
def ver_areas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM areas')
    areas = cur.fetchall()
    areas = [areaObj(x) for x in areas]
    return(jsonify(areas))

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
def userObj(row):
    return {
        "id" : row[0],
        "nombre_usuario" : row[1],
        "id_persona_fk": row[2],
        "id_area_fk": row[3],
        "contraseña": row[4]
    }
@app.route('/ver_usuarios')
def ver_usuarios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    usuarios = cur.fetchall()
    print(usuarios)
    usuarios = [userObj(x) for x in usuarios]
    cur.close()
    return(jsonify(usuarios))

# -- VER USUARIOS MEDICOS --
def userObj(row):
    return {
        "id" : row[0],
        "nombre_usuario" : row[1],
        "id_persona_fk": row[2],
        "id_area_fk": row[3],
        "contraseña": row[4]
    }
@app.route('/ver_usuarios_medicos')
def ver_usuarios_medicos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE rol = "medico"')
    usuarios = cur.fetchall()
    print(usuarios)
    usuarios = [userObj(x) for x in usuarios]
    cur.close()
    return(jsonify(usuarios))

# -- VER ALERTAS --
def alertaObj(row):
    return {
        "id" : row[0],
        "id_usuario_fk" : row[1],
        "origen": row[2],
        "hora_inicio": row[3],
        "hora_fin": row[4],
        "estado": row[5],
        "fecha_inicio": row[6],
        "fecha_fin": row[7],
        "tipo": row[8]
    }

@app.route('/ver_alertas')
def ver_alertas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alertas')
    alertas = cur.fetchall()
    alertas = [alertaObj(x) for x in alertas]
    cur.close()
    return(jsonify(json.dumps(alertas, default=str)))

# -- VER FICHAS --
def fichaObj(row):
    return {
        "id" : row[0],
        "id_persona_fk" : row[1],
        "peso": row[2],
        "temperatura": row[3],
        "presion": row[4],
        "enfermedades_preexistentes": row[5],
        "observaciones": row[6]
    }

@app.route('/ver_fichas')
def ver_fichas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM fichas')
    fichas = cur.fetchall()
    fichas = [fichaObj(x) for x in fichas]
    cur.close()
    return(jsonify(fichas))

# -- VER FICHAS POR ID DE PERSONA--
def fichaObj(row):
    return {
        "id" : row[0],
        "id_persona_fk" : row[1],
        "peso": row[2],
        "temperatura": row[3],
        "presion": row[4],
        "enfermedades_preexistentes": row[5],
        "observaciones": row[6]
    }

@app.route('/ver_fichas_id')
def ver_fichas_id():
    id_ficha = request.json['id']
    id_ficha_str = str(id_ficha)
    id_ficha_str = id_ficha_str.replace('(', '')
    id_ficha_str = id_ficha_str.replace(')', '')
    id_ficha_str = id_ficha_str.replace(',', '')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM fichas WHERE id_persona_fk = ' + id_ficha_str)
    fichas = cur.fetchall()
    fichas = [fichaObj(x) for x in fichas]
    cur.close()
    return(jsonify(fichas))



# -- BUCLE PRINCIPAL DE LA APP --
if (__name__) == '__main__':
    app.run(port=5000, debug=True)
