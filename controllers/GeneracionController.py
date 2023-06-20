import sys
from flask import request, jsonify
from app import conexion

def index():
    try:
        # generaciones = Generacion.query.all()
        # return jsonify([generacion.serialize() for generacion in generaciones])
        cursor = conexion.connection.cursor()
        sql = "SELECT * from generaciones"
        cursor.execute(sql)
        datos = cursor.fetchall()
        generaciones = []
        for f in datos:
            generacion = {'id':f[0], 'imagen1': f[1], 'imagen2': f[2], 'imagen3': f[3], 'texto1': f[4], 'texto2': f[5], 'texto3': f[6], 'id_user': f[7]}
            generaciones.append(generacion)
        return jsonify({'generaciones': generaciones, 'mensaje': "Generaciones listadas."})
        # return jsonify({'generaciones': [], 'mensaje': "Generaciones listadas."})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})

def store():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO generaciones (id, imagen1, imagen2, imagen3, texto1, texto2, texto3, id_user) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')""".format(request.json['id'], request.json['imagen1'], request.json['imagen2'], request.json['imagen3'], request.json['texto1'], request.json['texto2'], request.json['texto3'], request.json['id_user'])
        cursor.execute(sql)
        conexion.connection.commit() #confirmacion
        return jsonify({'mensaje': "Generacion registrado."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

def show(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * from generaciones WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            generacion = {'id':datos[0], 'imagen1': datos[1], 'imagen2': datos[2], 'imagen3': datos[3], 'texto1': datos[4], 'texto2': datos[5], 'texto3': datos[6], 'id_user': datos[7]}
            return jsonify({'generacion': generacion, 'mensaje': "Generacion encontrada."})
        else:
            return jsonify({'mensaje': "Generacion no encontrada."})
            
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

def update(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE generaciones SET imagen1 = '{1}', imagen2 = '{2}', imagen3 = '{3}', texto1 = '{4}', texto2 = '{5}', texto3 = '{6}', id_user = {7}
        """.format(id, request.json['imagen1'], request.json['imagen2'], request.json['imagen3'], request.json['texto1'], request.json['texto2'], request.json['texto3'], request.json['id_user'])
        cursor.execute(sql)
        conexion.connection.commit() #confirmacion
        return jsonify({'mensaje': "Generacion actualizado."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

def destroy(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM generaciones WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirmacion
        return jsonify({'mensaje': "Generacion eliminada."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

