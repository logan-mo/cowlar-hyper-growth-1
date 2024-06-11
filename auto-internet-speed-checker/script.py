from typing import Tuple
import datetime
import speedtest

LOG_FILE_PATH = "speed_log.csv"


def log_speed(download_speed, upload_speed):
    logging_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE_PATH, "a") as file:
        file.write(f"{logging_time},{download_speed},{upload_speed}\n")


def get_internet_speed() -> Tuple[float, float]:
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000

    return download_speed, upload_speed


try:
    download_speed, upload_speed = get_internet_speed()
    log_speed(download_speed, upload_speed)
except Exception as e:
    print(f"Error: {e}")
