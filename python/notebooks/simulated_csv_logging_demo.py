"""
simulated_csv_logging_demo.py

Purpose:
    Generates simulated wearable sensor data and saves it into a CSV file.

Why this file exists:
    - Allows testing the data logging pipeline without ESP32 hardware.
    - Connects simulation, data model, and CSV storage together.
    - Creates sample datasets that can later be used for preprocessing,
      visualization, and machine learning experiments.
"""

import sys
import time
from pathlib import Path

# Add project source directory to Python's import search path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from wearable_data_collection.sensor_csv_logger import SensorCSVLogger
from wearable_data_models.sensor_sample import SensorSample
from wearable_data_collection.simulated_sensor_generator import generate_simulated_sensor_line


def main() -> None:
    # Output folder for generated datasets
    output_directory = PROJECT_ROOT / "data"

    # Create output folder if it does not exist
    output_directory.mkdir(exist_ok=True)

    # Output CSV file path
    output_file_path = output_directory / "simulated_sensor_data.csv"

    # Create CSV logger object
    logger = SensorCSVLogger(output_file_path=str(output_file_path))

    # Write CSV column names
    logger.write_header()

    # Number of simulated samples to save
    number_of_samples = 20

    for _ in range(number_of_samples):
        # Generate one simulated raw CSV line
        raw_line = generate_simulated_sensor_line()

        # Convert raw CSV line into a structured SensorSample object
        sample = SensorSample.from_csv_line(raw_line)

        # Save the structured sample into the CSV file
        logger.append_sample(sample)

        # Small delay to simulate real-time sensor sampling
        time.sleep(0.2)

    print(f"Saved {number_of_samples} simulated samples to:")
    print(output_file_path)


if __name__ == "__main__":
    main()