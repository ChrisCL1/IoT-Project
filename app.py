from flask import Flask, jsonify
from func import *

app = Flask(__name__)

@app.route('/app', methods=['GET'])
def bluetooth_scan():
    scanner = BluetoothScanner()
    scanner.perform_inquiry()
    devices = scanner.nearby_devices
    return jsonify({'devices': devices})

if __name__ == '__main__':
    app.run(port=6000, debug=True)
