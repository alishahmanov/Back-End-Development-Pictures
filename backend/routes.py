from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    return jsonify(length=len(data)), 200


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data)

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = next((item for item in data if item["id"] == id), None)
    if picture is None:
        abort(404)
    return jsonify(picture)


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    picture = request.get_json()
    if not isinstance(picture, dict) or type(picture.get("id")) is not int:
        abort(400)
    picture_id = picture["id"]
    if any(item["id"] == picture_id for item in data):
        return jsonify(Message=f"picture with id {picture_id} already present"), 302
    data.append(picture)
    return jsonify(picture), 201

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    picture = request.get_json()
    if not isinstance(picture, dict):
        abort(400)
    for index, item in enumerate(data):
        if item["id"] == id:
            data[index] = {**item, **picture, "id": id}
            return jsonify(data[index])
    abort(404)

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    for index, item in enumerate(data):
        if item["id"] == id:
            del data[index]
            return "", 204
    abort(404)
