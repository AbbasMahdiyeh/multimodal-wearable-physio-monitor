"""
serial_reader_demo.py

Purpose:
    Demonstrates how to use the ESP32SerialReader class.

Why this file exists:
    - Provides a simple example for reading data from an ESP32.
    - Allows developers to understand the communication workflow.
    - Can later be extended to support simulated sensor data when
      physical hardware is not available.
    - Serves as a quick manual test before integrating the reader
      into larger data-processing pipelines.

Workflow:
    1. Create an ESP32SerialReader instance.
    2. Connect to the serial port.
    3. Read incoming sensor data.
    4. Print the received values.
    5. Close the connection safely.


"""

import sys
from pathlib import Path

# Add project source directory to Python's import search path.
# This allows notebook/demo files to import modules from python/src.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.append(str(SRC_PATH))

from wearable_data_collection.esp32_serial_reader import ESP32SerialReader

def main() -> None:

    # Change this port based on your ESP32 connection
    port = "COM3"

    # Create a reader object for the ESP32 serial connection
    reader = ESP32SerialReader(port=port)

    try:
        # Open the USB serial connection
        reader.connect()

        # Continuosly read incoming lines from ESP32
        while True:
            line = reader.read_line()

            # Print only valid received lines
            if line is not None:
                print(line)
    
    except KeyboardInterrupt:
        # Stop reading when the user presses Ctrl + C
        print("Reading stopped by user")

    finally:
        # Always close the serial connection safely
        reader.close()

if __name__ == "__main__":
    main()