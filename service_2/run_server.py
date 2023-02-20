from flask import Flask, Blueprint
from flask import jsonify
from custom_logger_utils import create_logger


app_name = "Check2"
app = Flask(app_name)

blueprint_name = "blueprint" + app_name
app_api = Blueprint(blueprint_name, __name__)
logger = create_logger(app_name)


@app_api.route('/', methods=['GET'])
def api0():
    logger.info("API call received: /")
    data = {"code": 200, "source": "api1", "message": "This service 2"}
    return jsonify(data)


@app_api.route('/api3', methods=['GET'])
def api1():
    logger.info("API call received: /api3")
    data = {"code": 200, "source": "api3", "message": "This service 2"}
    return jsonify(data)


@app_api.route('/api4', methods=['GET'])
def api2():
    logger.info("API call received: api4")
    data = {"code": 200, "source": "api4", "message": "This service 2"}
    return jsonify(data)


app.register_blueprint(app_api)
# app.register_blueprint(app_api,url_prefix="/c2")


if __name__ == "__main__":
    app.run()
