from flask import Flask, Blueprint
from flask import jsonify
from custom_logger_utils import create_logger
app_name = "Check80"

app = Flask(app_name)
blueprint_name = "blueprint" + app_name
app_api = Blueprint(blueprint_name, __name__)
logger = create_logger(app_name)


@app_api.route('/', methods=['GET'])
def api0():
    logger.info("API call received")
    data = {"code": 200, "source": "api1", "message": "This service 0"}
    return jsonify(data)


@app_api.route('/api01', methods=['GET'])
def api1():
    logger.info("API call received")
    data = {"code": 200, "source": "api1", "message": "This service 0"}
    return jsonify(data)


@app_api.route('/api02', methods=['GET'])
def api2():
    logger.info("API call received")
    data = {"code": 200, "source": "api2", "message": "This service 0"}
    return jsonify(data)

app.register_blueprint(app_api)

if __name__ == "__main__":
    app.run()
