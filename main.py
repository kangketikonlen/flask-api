from flask import Flask
from flask_restful import Api, abort, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class KaryawanModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(128), nullable=False)
    usia = db.Column(db.Integer, nullable=False)


db.create_all()

karyawan_put_args = reqparse.RequestParser()
karyawan_put_args.add_argument(
    "nama", type=str, help="Harap isi nama karyawan", required=True
)
karyawan_put_args.add_argument(
    "usia", type=int, help="Harap isi usia karyawan", required=True
)

resource_fields = {"id": fields.Integer, "nama": fields.String, "usia": fields.Integer}


class Karyawan(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = KaryawanModel.query.filter_by(id=id).first()
        if not result:
            abort(409, pesan="Karyawan tidak di temukan...")
        return result

    @marshal_with(resource_fields)
    def put(self, id):
        args = karyawan_put_args.parse_args()
        result = KaryawanModel.query.filter_by(id=id).first()
        if result:
            abort(409, pesan="Karyawan sudah ada...")
        karyawan = KaryawanModel(id=id, nama=args["nama"], usia=args["usia"])
        db.session.add(karyawan)
        db.session.commit()
        return karyawan, 201

    @marshal_with(resource_fields)
    def patch(self, id):
        args = karyawan_put_args.parse_args()
        result = KaryawanModel.query.filter_by(id=id).first()
        if not result:
            abort(404, pesan="Karyawan tidak di temukan, update gagal...")
        result.nama = args["nama"]
        result.usia = args["usia"]
        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, id):
        result = KaryawanModel.query.filter_by(id=id).first()
        if not result:
            abort(404, pesan="Karyawan tidak di temukan, delete gagal...")
        db.session.delete(id)
        return "", 204


api.add_resource(Karyawan, "/karyawan/<int:id>")

if (__name__) == "__main__":
    app.run(debug=True)
