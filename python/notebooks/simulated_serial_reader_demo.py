"""
simulated_serial_reader_demo.py

Purpose:
    Demonstrates how the data collection pipeline can be tested
    without physical ESP32 hardware.

Why this file exists:
    - Allows development at university when the ESP32 is not available.
    - Generates fake sensor-like data for testing the Python workflow.
    - Helps verify the project structure before real hardware integration.
    - Makes the GitHub repository easier to understand and test by others.

Workflow:
    1. Generate simulated sensor data.
    2. Format the data like a serial line from ESP32.
    3. Print the simulated incoming data.
"""

"""
Generate one simulated sensor sample.

Simulation assumptions:

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

Purpose:
    Allows testing the complete data-processing pipeline without
    requiring physical ESP32 hardware or sensors.
"""

import random
import time

def generate_simulated_sensor_line() -> str:
    # Simulated timestamp in milliseconds
    timestamp_ms = int(time.time() * 1000)

    # Simulated PPG values from MAX30102
    ppg_ir = random.randint(50000, 70000)
    ppg_red = random.randint(45000, 65000)

    # Simulated accelerometer values from MPU6050
    acc_x = round(random.uniform(-1.0, 1.0), 3)
    acc_y = round(random.uniform(-1.0, 1.0), 3)
    acc_z = round(random.uniform(8.5, 10.5), 3) # Simulate gravity when device is stationary

    # Simulated gyroscope values from MPU6050
    gyro_x = round(random.uniform(-250.0, 250.0), 3) # Simulate rotational movement around each axis
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