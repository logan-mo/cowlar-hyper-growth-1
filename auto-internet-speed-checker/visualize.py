## speed_log.csv
# logging_time,download_speed,upload_speed
# 2024-06-11 19:51:44,29.172024062845633,13.097001682297895
# 2024-06-11 19:52:59,28.457764647373335,20.63910092198474


# plot the above data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("speed_log.csv")
df["logging_time"] = pd.to_datetime(df["logging_time"])

plt.figure(figsize=(10, 5))
plt.plot(
    df["logging_time"], df["download_speed"], label="Download Speed (Mbps)", marker="o"
)

plt.plot(
    df["logging_time"], df["upload_speed"], label="Upload Speed (Mbps)", marker="o"
)

plt.xlabel("Time")
plt.ylabel("Speed (Mbps)")
plt.title("Internet Speed Over Time")
plt.legend()
plt.grid()

plt.show()
