from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/api/discord/members/post', methods=['POST'])
def add_member():
    Token = request.args.get('token')
    #token in config.json
    with open('config.json') as f:
        data = json.load(f)
        token = data['token']
    if Token == token:
        pass
    else:
        #status code 401
        return jsonify({'message': 'Unauthorized'}), 401
    json_data = open('db/db.json').read()
    data = json.loads(json_data)
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
    print(new_member)
    data.update(new_member)
    with open('db/db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify(new_member)

@app.route('/api/discord/members/<int:id>', methods=['GET'])
def get_member(id):
    json_data = open('db/db.json').read()
    data = json.loads(json_data)
    for id in data:
        if id == id:
            return jsonify(data[id])
        else:
            return jsonify({'message': 'Member not found'})


@app.route('/api/discord/members')
def get_members():
    json_data = open('db/db.json').read()
    data = json.loads(json_data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
    