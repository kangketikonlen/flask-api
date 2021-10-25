from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

karyawan_put_args = reqparse.RequestParser()
karyawan_put_args.add_argument(
    "nama",
    type=str,
    help="Harap isi nama karyawan",
    required=True
)
karyawan_put_args.add_argument(
    "usia",
    type=int,
    help="Harap isi usia karyawan",
    required=True
)

karyawan = {}


def abort_not_exists(id):
    if id not in karyawan:
        abort(404, pesan="Karyawan tidak ditemukan!")


def abort_exists(id):
    if id not in karyawan:
        abort(409, pesan="Karyawan sudah ada!")


class Karyawan(Resource):
    def get(self, id):
        abort_not_exists(id)
        return karyawan[id]

    def put(self, id):
        args = karyawan_put_args.parse_args()
        karyawan[id] = args
        return karyawan[id], 201

    def delete(self, id):
        abort_not_exists(id)
        del karyawan[id]
        return '', 204


api.add_resource(Karyawan, "/karyawan/<int:id>")

if(__name__) == "__main__":
    app.run(debug=True)
