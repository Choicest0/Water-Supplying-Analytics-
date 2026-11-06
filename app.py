"""
HydroPulse Dehradun - Backend Application Server
File: app.py
Framework: Flask
"""

import random
from flask import Flask, jsonify
from flask_cors import CORS  # <--- Added CORS import

app = Flask(__name__)
CORS(app)  # <--- Enabled CORS for all routes

# Dehradun Municipal Zones
ZONES = ["Rajpur Road", "Clock Tower", "Prem Nagar", "Clement Town"]

def fetch_telemetry():
    """Simulates real-time IoT water sensor readings."""
    telemetry = []
    for zone in ZONES:
        flow_rate = round(random.uniform(85.0, 115.0), 2)
        tds_level = random.randint(110, 180)
        pressure_drop = round(random.uniform(0.1, 1.8), 2)
        
        is_leak = pressure_drop > 1.2
        is_safe = tds_level <= 150
        
        telemetry.append({
            "zone": zone,
            "flow_rate_lps": flow_rate,
            "tds_ppm": tds_level,
            "pressure_drop_bar": pressure_drop,
            "status": "LEAK DETECTED" if is_leak else "OPTIMAL",
            "purity": "BIS 10500 SAFE" if is_safe else "ELEVATED MINERALS",
            "auto_valve_closed": is_leak
        })
    return telemetry

@app.route('/')
def home():
    return jsonify({
        "service": "HydroPulse Dehradun Backend API",
        "status": "Running",
        "endpoints": ["/api/v1/telemetry", "/api/v1/health"]
    })

@app.route('/api/v1/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify({
        "success": True,
        "count": len(ZONES),
        "data": fetch_telemetry()
    }), 200

@app.route('/api/v1/health', methods=['GET'])
def system_health():
    return jsonify({
        "grid_status": "OPERATIONAL",
        "total_pumps": 18,
        "average_tds": 142
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
