import os
import csv
import numpy as np
from openpyxl import load_workbook

root_path_source = 'iPhone Data/Location/'
root_path_csv = 'iPhone Data/csvs/'

file_list = os.listdir(root_path_source)

date = ""
time = ""
altitude = ""
latitude = ""
longitude = ""
relativeAltitude = ""
pressure = ""

for file in file_list:

    f_gps = root_path_csv + file[:-4] + "_gps.csv"
    f_sensor = root_path_csv + file[:-4] + "_sensor.csv"

    with open(root_path_source + file, 'r') as f:

        with open(f_gps, 'w') as f_gps_out:
            csvWriter = csv.writer(f_gps_out)
            csvWriter.writerow(['date', 'time', 'altitude', 'latitude', 'longitude'])

        with open(f_sensor, 'w') as f_sensor_out:
            csvWriter = csv.writer(f_sensor_out)
            csvWriter.writerow(['date', 'time', 'relativeAltitude', 'pressure'])

        while True:
            line = f.readline()
            if not line: break

            if line.endswith("0000\n"):
                # date
                date = line[:10]

                # time
                hh = (int)(line[11:13])
                mm = (int)(line[14:16])
                ss = (int)(line[17:19])
                time = hh * 3600 + mm * 60 + ss

                # altitude, latitude, longitude
                line = f.readline()
                altitude = line[9:-1]
                line = f.readline()
                latitude = line[9:-1]
                line = f.readline()
                longitude = line[10:-1]

                with open(f_gps, 'a') as f_gps_out:
                    csvWriter = csv.writer(f_gps_out)
                    csvWriter.writerow([date, time, altitude, latitude, longitude])

            elif line.endswith("0000)\n"):
                # date
                date = line[:10]

                # time
                hh = (int)(line[11:13])
                mm = (int)(line[14:16])
                ss = (int)(line[17:19])
                time = hh * 3600 + mm * 60 + ss

                # relativeAltitude, pressure
                line = f.readline()
                relativeAltitude = line[17:-1]
                line = f.readline()
                pressure = line[9:-1]

                with open(f_sensor, 'a') as f_sensor_out:
                    csvWriter = csv.writer(f_sensor_out)
                    csvWriter.writerow([date, time, relativeAltitude, pressure])




