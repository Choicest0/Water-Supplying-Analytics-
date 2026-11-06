"""
HydroPulse Dehradun - Data Analytics & Simulation Controller
File: main.py
"""

import time
from app import fetch_telemetry

class DehradunWaterAnalytics:
    def __init__(self):
        print("Initializing HydroPulse Dehradun Engine...")

    def run_analytics_stream(self):
        print("==================================================================")
        print("     HydroPulse Dehradun: Real-Time Stream Analytics Engine       ")
        print("==================================================================")
        
        data = fetch_telemetry()
        for record in data:
            zone = record['zone']
            flow = record['flow_rate_lps']
            tds = record['tds_ppm']
            status = record['status']
            purity = record['purity']
            
            print(f"Zone: {zone:<13} | Flow: {flow:>6} L/s | TDS: {tds:>3} ppm | Alert: {status:<13} | Quality: {purity}")

if __name__ == "__main__":
    engine = DehradunWaterAnalytics()
    engine.run_analytics_stream()
