from typing import Optional

import serial

class ESP32SerialReader:
    """
    Reads sensor data from an ESP32 board through a USB serial connection.

    """
    def __init__(self, port: str, baud_rate: int = 115200, timeout: float = 1.0):

        self.port = port # Serial port name (e.g., COM3)
        self.baud_rate = baud_rate # Communication speed
        self.timeout = timeout # Wait time for incoming data

        # Serial connection object (created after connect)
        self.serial_connection: Optional[serial.Serial] = None

    def connect(self) -> None:
        # open the serial connection to the ESP32
        self.serial_connection = serial.Serial(
            port= self.port,
            baudrate= self.baud_rate,
            timeout= self.timeout
        )

    def read_line(self) -> Optional[str]:

        # Make sure the serial connection is already open
        if self.serial_connection is None:
            raise RuntimeError("Serial Connection is not established.")
        
        # Read one raw line from the ESP32
        raw_line = self.serial_connection.readline()

        # Return None if no data was received
        if not raw_line:
            return None
        
        # Convert bytes to text and remove extra whitespace
        decoded_line = raw_line.decode("utf-8").strip()

        return decoded_line
    
    def close(self) -> None:
        
        # Close the serial connection if it exists
        if self.serial_connection is not None:
            self.serial_connection.close()
            self.serial_connection = None
    
