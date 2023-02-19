import flask
from utils import JSON

app = flask.Flask(__name__)


# token in config.json
Token = JSON.Read('../config.json')['token']


@app.route('/post', methods=['POST'])
def add_member():
    if flask.request.args.get("token") != Token:
        return flask.make_response(flask.jsonify({"success": False, "message": "No data provided for stat."}), 498)

    data = JSON.Read('../db/db.json')
    data[new_member] = {
        request.json["discord"]: {
            "email": request.json["email"],
            "curso": request.json["curso"],
            "year": request.json["year"],
            "github": request.json["github"],
            "twitter": request.json["twitter"],
            "instagram": request.json["instagram"],
            "fname": request.json["fname"],
            "lname": request.json["lname"],
            "phone": request.json["phone"],
            "description": request.json["description"]
        }
    }

    JSON.Write('../db/db.json', data)
    return flask.make_response(flask.jsonify({
        "success": True,
        "message": "Member registered!",
        "data": new_member
    }), 200)


@app.route('/members/<int:id>', methods=['GET'])
def members(id):
    if flask.request.args.get("token") != Token:
        return flask.make_response(flask.jsonify({"success": False, "message": "No valid token provided."}), 498)

    data = JSON.Read('../db/db.json')

    for id in data:
        if id == id:
            return flask.jsonify(data[id]), 200
        else:
            return flask.make_response(flask.jsonify({
                "success": False,
                "message": "Member not found!",
                "data": None
            }), 404)
    



@app.route('/allmembers')
def get_members():
    if flask.request.args.get("token") != Token:
        return flask.make_response(flask.jsonify({"success": False, "message": "No data provided for stat."}), 498)
    return flask.make_response(flask.jsonify(JSON.Read("../db/db.json")), 200)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
