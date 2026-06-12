"""
simulated_sensor_generator.py

Purpose:
    Generates simulated wearable sensor data without physical hardware.

Why this file exists:
    - Allows development when ESP32 and sensors are not available.
    - Provides fake but realistic sensor-like data for testing.
    - Keeps simulation logic inside the source code instead of demo scripts.
    - Enables testing of the complete data-processing pipeline.

Simulation model:

PPG (MAX30102):
    - IR and Red signals are always positive.
    - Values are generated within a realistic range for testing.

Accelerometer (MPU6050):
    - Positive and negative values are possible depending on
      movement direction and sensor orientation.
    - Z-axis is centered around Earth's gravity (~9.81 m/s²)
      to simulate a stationary wearable device.

Gyroscope (MPU6050):
    - Positive values indicate rotation in one direction.
    - Negative values indicate rotation in the opposite direction.
    - Values are generated within a realistic angular velocity range.

Output:
    Generates one CSV-formatted sensor sample containing:

    timestamp_ms,
    ppg_ir,
    ppg_red,
    acc_x,
    acc_y,
    acc_z,
    gyro_x,
    gyro_y,
    gyro_z
"""

import random
import time


def generate_simulated_sensor_line() -> str:
    """
    Generate one simulated ESP32 CSV sensor line.

    Output format:
        timestamp_ms, ppg_ir, ppg_red, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z
    """

    # Simulated timestamp in milliseconds
    timestamp_ms = int(time.time() * 1000)

    # Simulated PPG values from MAX30102
    ppg_ir = random.randint(50000, 70000)
    ppg_red = random.randint(45000, 65000)

    # Simulated accelerometer values from MPU6050
    acc_x = round(random.uniform(-1.0, 1.0), 3)
    acc_y = round(random.uniform(-1.0, 1.0), 3)

    # Simulate gravity when device is stationary
    acc_z = round(random.uniform(8.5, 10.5), 3)

    # Simulate rotational movement around each axis
    gyro_x = round(random.uniform(-250.0, 250.0), 3)
    gyro_y = round(random.uniform(-250.0, 250.0), 3)
    gyro_z = round(random.uniform(-250.0, 250.0), 3)

    # Format data like one CSV line from ESP32
    return (
        f"{timestamp_ms},"
        f"{ppg_ir},"
        f"{ppg_red},"
        f"{acc_x},"
        f"{acc_y},"
        f"{acc_z},"
        f"{gyro_x},"
        f"{gyro_y},"
        f"{gyro_z}"
    )