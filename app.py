from flask import Flask, request, jsonify, make_response, redirect, render_template_string
from flask_restful import Api, Resource, reqparse
import MySQLdb
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import xmltodict

app = Flask(__name__)
api = Api(app)

# Configure your app to use the JWT
app.config['JWT_SECRET_KEY'] = '071920'
jwt = JWTManager(app)

# Database configuration
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="admin",
    db="shoes"
)

login_form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<center>
<body>
    <h2>Login</h2>
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Submit">
    </form>   
</body>
</center>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':  # Replace with real user validation
            access_token = create_access_token(identity={'username': username})
            response = make_response(jsonify({'access_token': access_token}), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
        return make_response(jsonify({'message': 'Invalid credentials'}), 401)
    return render_template_string(login_form_html)

class Shoe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('shoesname', type=str, required=True, help="shoesname is required")

    @jwt_required()
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

    @jwt_required()
    def post(self):
        data = Shoe.parser.parse_args()
        cursor = db.cursor()
        cursor.execute("INSERT INTO shoe (shoesID, shoesname) VALUES (UUID(), %s)", (data['shoesname'],))
        db.commit()
        return {"message": "Shoe added successfully"}

    @jwt_required()
    def put(self, shoesID):
        data = Shoe.parser.parse_args()
        cursor = db.cursor()
        cursor.execute("UPDATE shoe SET shoesname = %s WHERE shoesID = %s", (data['shoesname'], shoesID))
        db.commit()
        return {"message": "Shoe updated successfully"}

    @jwt_required()
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
