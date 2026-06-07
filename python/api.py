from flask import Flask, request, jsonify
import db

app = Flask(__name__)

db.init_db()


# =========================
# STANDARD RESPONSE FORMAT
# =========================
def response(success, data=None, error=None):
    return {
        "success": success,
        "data": data,
        "error": error
    }


# =========================
# LOG FUNCTION
# =========================
def log(endpoint, method, status="SUCCESS"):
    db.add_log(endpoint, method, status)


# =========================
# ROOT
# =========================
@app.route("/")
def home():
    log("/", "GET")

    return jsonify(response(
        True,
        data="Hardware Inventory REST API is running"
    ))


# =========================
# GET ALL DEVICES
# =========================
@app.route("/devices", methods=["GET"])
def get_all_devices():
    devices = db.get_devices()

    result = []
    for d in devices:
        result.append({
            "id": d[0],
            "name": d[1],
            "status": d[2],
            "created_at": d[3]
        })

    log("/devices", "GET")

    return jsonify(response(True, data=result))


# =========================
# GET SINGLE DEVICE
# =========================
@app.route("/devices/<int:device_id>", methods=["GET"])
def get_device(device_id):
    d = db.get_device(device_id)

    if not d:
        log("/devices/<id>", "GET", "FAILED")
        return jsonify(response(False, error="Device not found")), 404

    log("/devices/<id>", "GET")

    return jsonify(response(True, data={
        "id": d[0],
        "name": d[1],
        "status": d[2],
        "created_at": d[3]
    }))


# =========================
# ADD DEVICE
# =========================
@app.route("/devices", methods=["POST"])
def add_device():
    data = request.json

    if not data:
        log("/devices", "POST", "FAILED")
        return jsonify(response(False, error="No JSON data provided")), 400

    name = data.get("name")
    status = data.get("status")

    if not name or not status:
        log("/devices", "POST", "FAILED")
        return jsonify(response(False, error="Missing name or status")), 400

    db.add_device(name, status)

    log("/devices", "POST")

    return jsonify(response(True, data="Device added successfully")), 201


# =========================
# UPDATE DEVICE
# =========================
@app.route("/devices/<int:device_id>", methods=["PUT"])
def update_device(device_id):
    data = request.json

    if not data:
        log("/devices/<id>", "PUT", "FAILED")
        return jsonify(response(False, error="No JSON data provided")), 400

    status = data.get("status")

    if not status:
        log("/devices/<id>", "PUT", "FAILED")
        return jsonify(response(False, error="Missing status")), 400

    db.update_device(device_id, status)

    log("/devices/<id>", "PUT")

    return jsonify(response(True, data="Device updated"))


# =========================
# DELETE DEVICE
# =========================
@app.route("/devices/<int:device_id>", methods=["DELETE"])
def delete_device(device_id):
    db.delete_device(device_id)

    log("/devices/<id>", "DELETE")

    return jsonify(response(True, data="Device deleted"))


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)