"""
simulated_serial_reader_demo.py

Purpose:
    Demonstrates how simulated wearable sensor data can be generated
    and consumed without requiring physical ESP32 hardware.

Why this file exists:
    - Allows development when hardware is unavailable.
    - Tests the simulated data pipeline.
    - Verifies that sensor data generation works correctly.
    - Provides a simple example for future contributors.

Workflow:
    1. Request one simulated sensor line from the generator.
    2. Print the generated data.
    3. Repeat the process multiple times.
"""

import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.append(str(SRC_PATH))

from wearable_data_collection.simulated_sensor_generator import (
    generate_simulated_sensor_line,
)

def main() -> None:
    # Number of simulated lines to print
    number_of_samples = 10

    for _ in range(number_of_samples):
        # Generate one fake ESP32 serial line
        simulated_line = generate_simulated_sensor_line()

        # Print the simulated incoming data
        print(simulated_line)

        # Simulate sensor sampling delay
        time.sleep(0.5)


if __name__ == "__main__":
    main()