from flask import Flask, jsonify

app = Flask(__name__)

# Fake "flight operations" data
FLIGHTS = [
    {"tailNumber": "N123AB", "status": "En Route", "origin": "KCMH", "destination": "KTEB"},
    {"tailNumber": "N987XY", "status": "Scheduled", "origin": "KDAL", "destination": "KAPA"},
    {"tailNumber": "N555PJ", "status": "Maintenance", "origin": "KCMH", "destination": None},
]

@app.route("/")
def home():
    return "AeroOps – Flight Operations Demo"

@app.route("/flights")
def flights():
    return jsonify(FLIGHTS)

if __name__ == "__main__":
    print("Starting AeroOps server on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
