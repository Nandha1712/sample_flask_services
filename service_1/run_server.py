from flask import Flask
from flask import jsonify

app_name = "Check1"
app = Flask(app_name)


@app.route('/', methods=['GET'])
def api0():
    data = {"code": 200, "source": "api1", "message": "This service 1"}
    return jsonify(data)


@app.route('/api3', methods=['GET'])
def api1():
    data = {"code": 200, "source": "api3", "message": "This service 1"}
    return jsonify(data)


@app.route('/api4', methods=['GET'])
def api2():
    data = {"code": 200, "source": "api4", "message": "This service 1"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=3001)
