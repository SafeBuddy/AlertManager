
from flask import jsonify

def create_response(success, message, status_code, data=None):
    response = {"success": success, "message": message}
    if data:
        response["data"] = data
    return jsonify(response), status_code
