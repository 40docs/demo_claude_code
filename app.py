"""Simple Flask web server for testing the Pet Adoption Center API."""

from flask import Flask, request, jsonify, render_template
from src.api.pets import create_pet, list_pets, get_pet, update_pet, delete_pet

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api")
def api_info():
    return jsonify({
        "message": "Pet Adoption Center API",
        "endpoints": {
            "GET /pets": "List all pets (optional: ?species=dog&status=available)",
            "GET /pets/<id>": "Get a specific pet",
            "POST /pets": "Create a new pet",
            "PUT /pets/<id>": "Update a pet",
            "DELETE /pets/<id>": "Delete a pet",
        }
    })


@app.route("/pets", methods=["GET"])
def handle_list_pets():
    species = request.args.get("species")
    status = request.args.get("status")
    return jsonify(list_pets(species=species, status=status))


@app.route("/pets/<int:pet_id>", methods=["GET"])
def handle_get_pet(pet_id):
    return jsonify(get_pet(pet_id))


@app.route("/pets", methods=["POST"])
def handle_create_pet():
    data = request.get_json()
    return jsonify(create_pet(data))


@app.route("/pets/<int:pet_id>", methods=["PUT"])
def handle_update_pet(pet_id):
    data = request.get_json()
    return jsonify(update_pet(pet_id, data))


@app.route("/pets/<int:pet_id>", methods=["DELETE"])
def handle_delete_pet(pet_id):
    return jsonify(delete_pet(pet_id))


if __name__ == "__main__":
    print("Starting Pet Adoption Center API...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host="0.0.0.0", port=5000)
