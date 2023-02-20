from flask import Flask
from flask import jsonify

app_name = "Check80"
app = Flask(app_name)


@app.route('/', methods=['GET'])
def api0():
    data = {"code": 200, "source": "api1", "message": "This service 0"}
    return jsonify(data)


@app.route('/api01', methods=['GET'])
def api1():
    data = {"code": 200, "source": "api1", "message": "This service 0"}
    return jsonify(data)


@app.route('/api02', methods=['GET'])
def api2():
    data = {"code": 200, "source": "api2", "message": "This service 0"}
    return jsonify(data)

if __name__ == "__main__":
    app.run()
