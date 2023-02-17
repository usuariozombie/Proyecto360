from flask import Flask, jsonify, request
from utils import JSON

app = Flask(__name__)

Token = request.args.get('token')
#token in config.json
token = JSON.Read('../config.json')['token']

@app.route('/api/discord/members/post', methods=['POST'])
def add_member():
    if Token == token:
        pass
    else:
        #status code 401
        return jsonify({'message': 'Unauthorized'}), 401
    data = JSON.Read('../db/db.json')
    new_member = {
        request.json['discord']: {
            'email': request.json['email'],
            'curso': request.json['curso'],
            'year': request.json['year'],
            'github': request.json['github'],
            'twitter': request.json['twitter'],
            'instagram': request.json['instagram'],
            'fname': request.json['fname'],
            'lname': request.json['lname'],
            'phone': request.json['phone'],
            'description': request.json['description']
        }
    }
    data.update(new_member)
    JSON.Write('../db/db.json', data)
    return jsonify({'message': 'Member added'})

@app.route('/api/discord/members/<int:id>', methods=['GET'])
def get_member(id):
    if Token == token:
        pass
    else:
        #status code 401
        return jsonify({'message': 'Unauthorized'}), 401
    data = JSON.Read('../db/db.json')
    for id in data:
        if id == id:
            return jsonify(data[id])
        else:
            return jsonify({'message': 'Member not found'})


@app.route('/api/discord/members')
def get_members():
    if Token == token:
        pass
    else:
        #status code 401
        return jsonify({'message': 'Unauthorized'}), 401
    data = JSON.Read('../db/db.json')
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
    