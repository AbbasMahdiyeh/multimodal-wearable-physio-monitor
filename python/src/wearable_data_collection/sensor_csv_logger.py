from pathlib import Path

from wearable_data_models.sensor_sample import SensorSample


class SensorCSVLogger:
    """
    Saves SensorSample objects into a CSV file.
    """

    def __init__(self, output_file_path: str):
        # Path where the CSV file will be saved
        self.output_file_path = Path(output_file_path)

    def write_header(self) -> None:
        # Create the CSV header row
        header = (
            "timestamp_ms,"
            "ppg_ir,"
            "ppg_red,"
            "acc_x,"
            "acc_y,"
            "acc_z,"
            "gyro_x,"
            "gyro_y,"
            "gyro_z\n"
        )

        self.output_file_path.write_text(header, encoding="utf-8")

    def append_sample(self, sample: SensorSample) -> None:
        # Convert one SensorSample object into one CSV row
        row = (
            f"{sample.timestamp_ms},"
            f"{sample.ppg_ir},"
            f"{sample.ppg_red},"
            f"{sample.acc_x},"
            f"{sample.acc_y},"
            f"{sample.acc_z},"
            f"{sample.gyro_x},"
            f"{sample.gyro_y},"
            f"{sample.gyro_z}\n"
        )

        with self.output_file_path.open("a", encoding="utf-8") as file:
            file.write(row)