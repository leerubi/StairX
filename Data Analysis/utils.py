import os
import pandas as pd

def merge_same_time_data():

    root_path_from = 'iPhone Data/csvs/'
    root_path_to = 'iPhone Data/processed_csvs/'
    file_list = os.listdir(root_path_from)

    for file in file_list:

        if file == '.DS_Store': continue

        data = pd.read_csv(root_path_from + file)
        processed_data = data.groupby(['time'], as_index=False).mean()
        f_processed = root_path_to + file[:-4] + "_processed.csv"
        processed_data.to_csv(f_processed)

def interpolation():

    root_path_from = 'iPhone Data/processed_csvs/'
    root_path_to = 'iPhone Data/interpolated_csvs/'
    file_list = os.listdir(root_path_from)

    for file in file_list:

        if file == '.DS_Store': continue


def merge_two_csvs():
    print("implement!")
    # root_path_from = 'iPhone Data/processed_csvs/'
    # root_path_to = 'iPhone Data/merged_csvs/'
    # file_list = os.listdir('iPhone Data/Location/')
    #
    # column_names = ['date', 'time', 'altitude', 'latitude', 'longitude', 'relativeAltitude', 'pressure']
    #
    # for file in file_list:
    #
    #     if file == '.DS_Store': continue
    #
    #     f_gps = root_path_from + file[:-4] + "_gps_processed.csv"
    #     f_sensor = root_path_from + file[:-4] + "_sensor_processed.csv"
    #
    #     data1 = pd.read_csv(f_gps,
    #                         index_col=['time'],
    #                         parse_dates='time',
    #                         header=None,
    #                         names=column_names).sort_index()
    #     data2 = pd.read_csv(f_sensor,
    #                         index_col=['time'],
    #                         parse_dates='time',
    #                         header=None,
    #                         names=column_names).sort_index()
    #     data1.set_index(data1.reindex(data2.index, method='nearest').index, inplace=True)
    #
    #     f_merged = root_path_to + file[:-4] + "merged.csv"
    #     data1.to_csv(f_merged)



def impute_empty_time_data():
    print("implement!")

def drop_out_egde_data():
    print("implement!")