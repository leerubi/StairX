import os
import pandas as pd
import numpy as np

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

    # 시간 간격이 10초 이상일 때는 interpolation하지 않는 기능 추후 구현

    root_path_from = 'iPhone Data/csvs/processed_csvs/'
    root_path_to = 'iPhone Data/csvs/merged_csvs/'
    file_list = os.listdir(root_path_from)

    for file in file_list:

        if file == '.DS_Store': continue

        data = pd.read_csv(root_path_from + file)

        '''
        1. 제목 로우와 시간 칼럼을 만든다
        2. 있는 데이터를 넣는다 (A, B 둘다)
        3. interpolate()
        '''



        #
        # range = np.arange(data['date'].values[0], data['date'].values[-1])
        #
        # for elem in range:
        #     if elem not in np.array(data['date']):
        #         data = data.append({'date': elem}, ignore_index=True)
        #
        # data = data.sort_values('date').reset_index(drop=False)
        # data = data.interpolate()
        #
        # f_interpolated = root_path_to + file[:-14] + "_interpolated.csv"
        # data.to_csv(f_interpolated)

# def merge_two_csvs():
#     print("implement!")
#
#     root_path_from = 'iPhone Data/interpolated_csvs/'
#     root_path_to = 'iPhone Data/merged_csvs/'
#     file_list = os.listdir('iPhone Data/Location/')
#
#     for file in file_list:
#
#         if file == '.DS_Store': continue
#
#         f_gps = root_path_from + file[:-4] + "_gps_interpolated.csv"
#         f_sensor = root_path_from + file[:-4] + "_sensor_interpolated.csv"
#
#         data_gps = pd.read_csv(f_gps)
#         range_gps = np.arange(data_gps['time'].values[0], data_gps['time'].values[-1] + 1)
#
#         data_sensor = pd.read_csv(f_sensor)
#         range_sensor = np.arange(data_sensor['time'].values[0], data_sensor['time'].values[-1] + 1)
#
#         range_inter = np.intersect1d(range_gps, range_sensor)
#         data_gps = data_gps.loc[data_gps['time'] >= range_inter[0]]
#         data_gps = data_gps.loc[data_gps['time'] <= range_inter[-1]]
#         data_sensor = data_sensor.loc[data_sensor['time'] >= range_inter[0]]
#         data_sensor = data_sensor.loc[data_sensor['time'] <= range_inter[-1]]
#
#         merged_data = pd.merge(data_gps, data_sensor, left_index=True, right_index=True)
#         print("fds")


def impute_empty_time_data():
    print("implement!")

def drop_out_egde_data():
    print("implement!")