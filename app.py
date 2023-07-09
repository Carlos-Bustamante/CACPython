from flask import Flask ,jsonify ,request
from flask_cors import CORS      
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#BBDD
class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float())
    fecha = db.Column(db.Integer)
    lugar = db.Column(db.String(400))

    def __init__(self,nombre, precio, fecha, lugar):
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        self.imagen = lugar

#Resto de las tablas si las hubiera

with app.app_context():
    db.create_all() #Se crea la tabla

class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','fecha''lugar')

producto_schema=ProductoSchema()            # El objeto producto_schema es para traer un producto
productos_schema=ProductoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto


@app.route('/evento', methods=['GET'])
def get_evento():
    evento = evento.query.all()
    resultado = productos_schema.dump(evento)
    return jsonify(resultado)

@app.route('/evento/<id>',methods=['GET'])
def get_producto(id):
    evento=evento.query.get(id)
    return producto_schema.jsonify(evento)   # retorna el JSON de un producto recibido como parametro


@app.route('/evento/<id>',methods=['DELETE'])
def delete_producto(id):
    evento=evento.query.get(id)
    db.session.delete(evento)
    db.session.commit()
    return producto_schema.jsonify(evento)

@app.route('/eventos', methods=['POST'])
def create_eventos():
       nombre = request.json['nombre'] 
       precio = request.json['precio']
       fecha = request.json['fecha']
       lugar = request.json['lugar']
       nuevo_evento = evento(nombre, precio, fecha, lugar)
       db.session.add(nuevo_evento)
       db.session.commit()
       return producto_schema.jsonify(nuevo_evento)

@app.route('/eventos/<id>', methods=['PUT'])
def update_producto(id):
    eventos = eventos.query.get(id)
    
    nombre = request.json['nombre'] 
    precio = request.json['precio']
    fecha = request.json['fecha']
    lugar = request.json['lugar']

    eventos.nombre = nombre
    eventos.precio = precio
    eventos.fecha = fecha
    eventos.lugar = lugar

    db.session.commit()
    return producto_schema.jsonify(eventos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
