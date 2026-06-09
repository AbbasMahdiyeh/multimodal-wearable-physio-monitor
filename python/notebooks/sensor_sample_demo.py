"""
sensor_sample_demo.py

Purpose:
    Demonstrates how to convert one raw CSV sensor line into a structured
    SensorSample object.

Why this file exists:
    - Helps test the data model without ESP32 hardware.
    - Shows how raw serial data becomes structured Python data.
    - Makes the project easier to understand for future development.
"""

import sys
from pathlib import Path

# Add project source directory to Python's import search path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from wearable_data_models.sensor_sample import SensorSample


def main() -> None:
    # Example line with:
    # timestamp_ms, ppg_ir, ppg_red, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z
    csv_line = "1712345678901,61234,58321,-0.25,0.17,9.92,120.5,-43.2,15.7"

    # Convert raw CSV text into a structured SensorSample object
    sample = SensorSample.from_csv_line(csv_line)

    # Print the full object
    print(sample)

    # Access individual fields
    print("PPG IR:", sample.ppg_ir)
    print("Acceleration Z:", sample.acc_z)
    print("Gyroscope X:", sample.gyro_x)


if __name__ == "__main__":
    main()