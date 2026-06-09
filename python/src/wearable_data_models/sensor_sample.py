from dataclasses import dataclass


@dataclass
class SensorSample:
    """
    Represents one synchronized sensor sample from the wearable system.
    """

    timestamp_ms: int
    ppg_ir: int
    ppg_red: int
    acc_x: float
    acc_y: float
    acc_z: float
    gyro_x: float
    gyro_y: float
    gyro_z: float

    @classmethod
    def from_csv_line(cls, csv_line: str) -> "SensorSample":
        # Split one CSV line into separate string values
        values = csv_line.split(",")

        # Make sure the line contains all required sensor fields
        if len(values) != 9:
            raise ValueError("CSV line must contain exactly 9 values.")

        return cls(
            timestamp_ms=int(values[0]),
            ppg_ir=int(values[1]),
            ppg_red=int(values[2]),
            acc_x=float(values[3]),
            acc_y=float(values[4]),
            acc_z=float(values[5]),
            gyro_x=float(values[6]),
            gyro_y=float(values[7]),
            gyro_z=float(values[8]),
        )