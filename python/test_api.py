import requests

BASE_URL = "http://127.0.0.1:5000"


# =========================
# TEST: ROOT
# =========================
def test_home():
    r = requests.get(f"{BASE_URL}/")
    print("HOME:", r.json())


# =========================
# TEST: ADD DEVICE
# =========================
def test_add_device():
    payload = {
        "name": "ESP8266",
        "status": "available"
    }

    r = requests.post(f"{BASE_URL}/devices", json=payload)
    print("ADD:", r.json())


# =========================
# TEST: GET ALL DEVICES
# =========================
def test_get_devices():
    r = requests.get(f"{BASE_URL}/devices")
    print("ALL DEVICES:", r.json())


# =========================
# TEST: UPDATE DEVICE
# =========================
def test_update_device():
    payload = {
        "status": "in-use"
    }

    r = requests.put(f"{BASE_URL}/devices/1", json=payload)
    print("UPDATE:", r.json())


# =========================
# RUN ALL TESTS
# =========================
if __name__ == "__main__":
    test_home()
    test_add_device()
    test_get_devices()
    test_update_device()
    test_get_devices()