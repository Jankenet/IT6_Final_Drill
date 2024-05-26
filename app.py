
from flask import Flask, request, jsonify, make_response, redirect
from flask_restful import Api, Resource, reqparse
import MySQLdb
import xmltodict

app = Flask(__name__)
api = Api(app)

# Database configuration
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="admin",
    db="shoes"
)

class Shoe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('shoesname', type=str, required=True, help="shoesname is required")

    def get(self, shoesID=None):
        cursor = db.cursor()
        if shoesID:
            cursor.execute("SELECT * FROM shoe WHERE shoesID = %s", (shoesID,))
            shoe = cursor.fetchone()
            if shoe:
                shoe_data = {"shoesID": shoe[0], "shoesname": shoe[1]}
                return self.format_response(shoe_data)
            return {"message": "Shoe not found"}, 404
        cursor.execute("SELECT * FROM shoe")
        shoes = cursor.fetchall()
        shoe_list = [{"shoesID": shoe[0], "shoesname": shoe[1]} for shoe in shoes]
        return self.format_response(shoe_list)

    def post(self):
        data = Shoe.parser.parse_args()
        cursor = db.cursor()
        cursor.execute("INSERT INTO shoe (shoesID, shoesname) VALUES (UUID(), %s)", (data['shoesname'],))
        db.commit()
        return {"message": "Shoe added successfully"}

    def put(self, shoesID):
        data = Shoe.parser.parse_args()
        cursor = db.cursor()
        cursor.execute("UPDATE shoe SET shoesname = %s WHERE shoesID = %s", (data['shoesname'], shoesID))
        db.commit()
        return {"message": "Shoe updated successfully"}

    def delete(self, shoesID):
        cursor = db.cursor()
        cursor.execute("DELETE FROM shoe WHERE shoesID = %s", (shoesID,))
        db.commit()
        return {"message": "Shoe deleted successfully"}

    def format_response(self, data):
        format_type = request.args.get('format', 'json')
        if format_type == 'xml':
            response = make_response(xmltodict.unparse({"response": data}), 200)
            response.headers['Content-Type'] = 'application/xml'
            return response
        return jsonify(data)

@app.route('/')
def redirect_to_shoes():
    return redirect('/shoes')

api.add_resource(Shoe, '/shoes', '/shoes/<string:shoesID>')

if __name__ == '__main__':
    app.run(debug=True)
