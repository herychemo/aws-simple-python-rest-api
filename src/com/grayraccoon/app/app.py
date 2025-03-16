# app.py
from flask import Flask, request, jsonify, redirect

from .db import get_db
from .initdb import initdb
from .service import ResourcesService

app = Flask(__name__)

initdb()

service = ResourcesService()

@app.get("/")
def get_root():
    return redirect('/resources', code=302)

@app.get("/resources")
def get_all_resources():
    items = service.find_all()
    return jsonify(items)

@app.get("/resources/<int:resource_id>")
def get_resource_by_id(resource_id):
    item = service.find_by_id(resource_id)
    if item is None:
        return jsonify({"error": "Not Found"}), 404

    return jsonify(item)

@app.post("/resources")
def create_resource():
    if not request.is_json:
        return "{'error', 'request must be json'}", 415
    item = request.get_json()

    item = service.save(item)
    return jsonify(item), 201

@app.put("/resources/<int:resource_id>")
def update_resource(resource_id):
    if not request.is_json:
        return "{'error', 'request must be json'}", 415
    item = request.get_json()
    item['ID'] = resource_id

    item = service.save(item)
    return jsonify(item), 200

@app.delete("/resources/<int:resource_id>")
def delete_resource(resource_id):
    service.delete(resource_id)
    return '{}', 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
