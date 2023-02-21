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
    new_member = {
        flask.request.json["discord"]: {
            "email": flask.request.json["email"],
            "curso": flask.request.json["curso"],
            "year": flask.request.json["year"],
            "github": flask.request.json["github"],
            "twitter": flask.request.json["twitter"],
            "instagram": flask.request.json["instagram"],
            "fname": flask.request.json["fname"],
            "lname": flask.request.json["lname"],
            "phone": flask.request.json["phone"],
            "description": flask.request.json["description"]
        }
    }
    
    data.update(new_member)

    JSON.Write('../db/db.json', data)
    return flask.make_response(flask.jsonify({
        "success": True,
        "message": "Member registered!",
        "data": new_member
    }), 200)


@app.route('/members/<int:userid>', methods=['GET'])
def members(userid):
    if flask.request.args.get("token") != Token:
        return flask.make_response(flask.jsonify({"success": False, "message": "No data provided for stat."}), 498)
    
    data = JSON.Read('../db/db.json')

    for id in data:
        if id == str(userid):
            return flask.jsonify(data[id]), 200

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
