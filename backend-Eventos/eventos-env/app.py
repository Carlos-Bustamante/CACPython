from flask import Flask ,jsonify ,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
CORS(app) 


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/eventos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)


class Producto(db.Model): 
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    fecha=db.Column(db.String(100))
    lugar=db.Column(db.String(100))
    def __init__(self,nombre,precio,fecha,lugar):

        self.nombre=nombre
        self.precio=precio
        self.fecha=fecha
        self.lugar=lugar

with app.app_context():
    db.create_all()


# ************************************************************


class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','fecha','lugar')

producto_schema=ProductoSchema()
productos_schema=ProductoSchema(many=True)

# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()
    result=productos_schema.dump(all_productos) 
    return jsonify(result) 

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)


@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST'])
def create_producto():    
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['fecha']
    imagen=request.json['lugar']
    new_producto=Producto(nombre,precio,stock,imagen)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
    producto.nombre=request.json['nombre']
    producto.precio=request.json['precio']
    producto.stock=request.json['fecha']
    producto.imagen=request.json['lugar']
    db.session.commit()
    return producto_schema.jsonify(producto)

# programa principal *******************************
if __name__=='__main__':
    app.run(debug=True, port=5000)