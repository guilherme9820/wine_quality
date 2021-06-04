import os
import yaml
import pandas as pd
import argparse

## Step 1: Read the parameters
## Step 2: Process the data
## Step 3: Return a new dataframe containing the data

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config):
    data_path = config["data_source"]["gdrive"]     
    df = pd.read_csv(data_path)
    return df

if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    
    config = read_params(parsed_args.config)
    data = get_data(config)
    print(data.head())
