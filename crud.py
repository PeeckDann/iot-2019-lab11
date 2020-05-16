from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src.main.model.fish import Fish
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SeaFish(Fish, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_in_uah = db.Column(db.Integer, unique=False)
    producer = db.Column(db.String(32), unique=False)
    species = db.Column(db.String(32), unique=False)
    product_condition = db.Column(db.String(32), unique=False)
    product_category = db.Column(db.String(32), unique=False)

    def __init__(self, price_in_uah=0, producer='default_producer', species='default_species',
                 product_condition=None, product_category='default_product_category'):
        super().__init__(price_in_uah, producer, species, product_condition, product_category)


class SeaFishSchema(ma.Schema):
    class Meta:
        fields = ('price_in_uah', 'producer', 'species', 'product_condition', 'product_category')


sea_fish_schema = SeaFishSchema()
sea_fish_schemas = SeaFishSchema(many=True)


@app.route("/fish", methods=["POST"])
def create_equip():
    price_in_uah = request.json['price_in_uah']
    producer = request.json['producer']
    species = request.json['species']
    product_condition = request.json['product_condition']
    product_category = request.json['product_category']
    sea_fish_seafood = SeaFish(price_in_uah, producer, species, product_condition, product_category)
    db.session.add(sea_fish_seafood)
    db.session.commit()
    return sea_fish_schema.jsonify(sea_fish_seafood)


@app.route("/fish", methods=["GET"])
def get_equip():
    all_sea_fish_seafood = SeaFish.query.all()
    result = sea_fish_schemas.dump(all_sea_fish_seafood)
    return jsonify({'sea_fish_seafood': result})


@app.route("/fish/<id>", methods=["GET"])
def get_all_equip(id):
    sea_fish_seafood = SeaFish.query.get(id)
    if not sea_fish_seafood:
        abort(404)
    return sea_fish_schema.jsonify(sea_fish_seafood)


@app.route("/fish/<id>", methods=["PUT"])
def equip_update(id):
    sea_fish_seafood = SeaFish.query.get(id)
    if not sea_fish_seafood:
        abort(404)
    old_seafood = copy.deepcopy(sea_fish_seafood)
    sea_fish_seafood.price_in_uah = request.json['price_in_uah']
    sea_fish_seafood.producer = request.json['producer']
    sea_fish_seafood.species = request.json['species']
    sea_fish_seafood.product_condition = request.json['product_condition']
    sea_fish_seafood.product_category = request.json['product_category']
    db.session.commit()
    return sea_fish_schema.jsonify(old_seafood)


@app.route("/fish/<id>", methods=["DELETE"])
def equip_delete(id):
    sea_fish_seafood = SeaFish.query.get(id)
    if not sea_fish_seafood:
        abort(404)
    db.session.delete(sea_fish_seafood)
    db.session.commit()
    return sea_fish_schema.jsonify(sea_fish_seafood)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
