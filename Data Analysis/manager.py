import os
import csv
import datetime
from dateutil.parser import parse
import pandas as pd

def load_location():
    root_path_from = 'iPhone Data/Location/'
    root_path_to = 'iPhone Data/csvs/loaded_csvs/'
    file_list = os.listdir(root_path_from)

    for file in file_list:
        f_gps = root_path_to + file[:-4] + "_gps.csv"
        f_sensor = root_path_to + file[:-4] + "_sensor.csv"

        with open(root_path_from + file, 'r') as f:

            with open(f_gps, 'w') as f_gps_out:
                csvWriter = csv.writer(f_gps_out)
                csvWriter.writerow(['date', 'altitude', 'latitude', 'longitude'])

            with open(f_sensor, 'w') as f_sensor_out:
                csvWriter = csv.writer(f_sensor_out)
                csvWriter.writerow(['date', 'relativeAltitude', 'pressure'])

            while True:
                line = f.readline()
                if not line: break

                if line.endswith("0000\n"):
                    # date
                    date = line[:19]
                    date = parse(date) + datetime.timedelta(hours=9)

                    # altitude, latitude, longitude
                    line = f.readline()
                    altitude = line[9:-1]
                    line = f.readline()
                    latitude = line[9:-1]
                    line = f.readline()
                    longitude = line[10:-1]

                    with open(f_gps, 'a') as f_gps_out:
                        csvWriter = csv.writer(f_gps_out)
                        csvWriter.writerow([date, altitude, latitude, longitude])

                elif line.endswith("0000)\n"):
                    # date
                    date = line[:19]
                    date = parse(date) + datetime.timedelta(hours=9)

                    # relativeAltitude, pressure
                    line = f.readline()
                    relativeAltitude = line[17:-1]
                    line = f.readline()
                    pressure = line[9:-1]

                    with open(f_sensor, 'a') as f_sensor_out:
                        csvWriter = csv.writer(f_sensor_out)
                        csvWriter.writerow([date, relativeAltitude, pressure])

def load_flightsClimbed():
    root_path_from = 'iPhone Data/FlightsClimbed/'
    root_path_to = 'iPhone Data/csvs/flightsClimbed_csvs/'
    file_list = os.listdir(root_path_from)

    with open(root_path_to + "filghtsClimbed_merged.csv", 'w') as f_out:
        csvWriter = csv.writer(f_out)
        csvWriter.writerow(['date', 'isStair', 'value'])

    for file in file_list:
        if file == '.DS_Store': continue

        with open(root_path_from + file, 'r') as f:

            while True:
                line = f.readline()
                if not line: break

                parsed = line.split(' ')

                start_date = parsed[17][11:]
                start_date = start_date + ' ' + parsed[18]
                start_date = parse(start_date)

                end_date = parsed[20][9:]
                end_date = end_date + ' ' + parsed[21]
                end_date = parse(end_date)

                value = parsed[23][7:8]

                with open(root_path_to + "filghtsClimbed_merged.csv", 'a') as f_out:
                    csvWriter = csv.writer(f_out)
                    while True:
                        if start_date == end_date + datetime.timedelta(seconds=1): break

                        csvWriter.writerow([start_date, '1', value])
                        start_date = start_date + datetime.timedelta(seconds=1)




