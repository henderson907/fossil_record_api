from flask import Flask, jsonify, request
from db_utils import get_all_fossils_db, add_new_fossil_db, find_fossil_by_country_db

app = Flask(__name__)

@app.route("/fossils", methods=["GET"])
def get_all_fossils():
    return jsonify(get_all_fossils_db())

@app.route("/fossils/add", methods=["POST"])
def add_new_fossil():
    new_fossil_dictionary = request.get_json()
    return jsonify(add_new_fossil_db(new_fossil_dictionary))

# Use GET method to retrieve records matching a specific country
@app.route("/fossils/<country>", methods=["GET"])
def find_fossils_by_country(country):
    return jsonify(find_fossil_by_country_db(country))

if __name__ == "__main__":
    app.run(debug=True)