import os
import csv
import pandas as pd
import datetime
from dateutil.parser import parse

def merge_same_time_data():

    root_path_from = 'iPhone Data/csvs/loaded_csvs/'
    root_path_to = 'iPhone Data/csvs/processed_csvs/'
    file_list = os.listdir(root_path_from)

    for file in file_list:

        if file == '.DS_Store': continue

        data = pd.read_csv(root_path_from + file)
        processed_data = data.groupby(['date'], as_index=False).mean()
        f_processed = root_path_to + file[:-4] + "_processed.csv"

        processed_data.to_csv(f_processed)

def merge_two_csvs():

    root_path_from = 'iPhone Data/csvs/processed_csvs/'
    root_path_to = 'iPhone Data/csvs/merged_csvs/'
    file_list = os.listdir('iPhone Data/Location/')

    for file in file_list:

        if file == '.DS_Store': continue

        f_gps = root_path_from + file[:-4] + "_gps_processed.csv"
        f_sensor = root_path_from + file[:-4] + "_sensor_processed.csv"
        f_merged = root_path_to + file[:-4] + "_merged.csv"

        data_gps = pd.read_csv(f_gps)
        data_sensor = pd.read_csv(f_sensor)

        data_merged = data_gps.merge(data_sensor, left_on='date', right_on='date', how='outer')

        data_merged = data_merged.sort_values('date').reset_index(drop=False)
        data_merged = data_merged.interpolate()
        data_merged = data_merged.dropna()

        data_merged.to_csv(f_merged)



def impute_empty_time_data():
    print("implement!")

def drop_out_egde_data():
    print("implement!")