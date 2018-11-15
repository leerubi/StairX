import os
import pandas as pd

root_path_source = 'iPhone Data/csvs/'
root_path_csv = 'iPhone Data/processed_csvs/'

def merge_same_time_data():

    file_list = os.listdir(root_path_source)

    for file in file_list:

        if file == '.DS_Store': continue
        data = pd.read_csv(root_path_source+file)
        processed_data = data.groupby(['time'], as_index=False).mean()
        f_processed = root_path_csv + file[:-4] + "_processed.csv"
        processed_data.to_csv(f_processed)

def merge_two_csvs():
    print("implement!")

def impute_empty_time_data():
    print("implement!")

def drop_out_egde_data():
    print("implement!")