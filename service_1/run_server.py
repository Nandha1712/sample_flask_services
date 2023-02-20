from flask import Flask, Blueprint
from flask import jsonify

app_name = "Check1"
app = Flask(app_name)

blueprint_name = "blueprint" + app_name
app_api = Blueprint(blueprint_name, __name__)


@app_api.route('/', methods=['GET'])
def api0():
    data = {"code": 200, "source": "api1", "message": "This service 1"}
    return jsonify(data)


@app_api.route('/api3', methods=['GET'])
def api1():
    data = {"code": 200, "source": "api3", "message": "This service 1"}
    return jsonify(data)


@app_api.route('/api4', methods=['GET'])
def api2():
    data = {"code": 200, "source": "api4", "message": "This service 1"}
    return jsonify(data)

app.register_blueprint(app_api)
# app.register_blueprint(app_api,url_prefix="/c1")

if __name__ == "__main__":
    app.run()
