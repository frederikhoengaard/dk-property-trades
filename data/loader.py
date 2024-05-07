import os
from typing import Optional

import pandas as pd
from pandas import DataFrame


def load_dataset(as_frame=False) -> Optional[DataFrame]:
    """
    The utility function to load the housing
    data set from the partitions and return it
    either as a dataframe or write it as a parquet file

    :param as_frame: whether to return as dataframe
    :return: a dataframe of the housing data set
    """
    directory = 'partitions'

    dataframes = []

    # Loop through all Parquet files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.parquet'):
            file_path = os.path.join(directory, filename)
            df = pd.read_parquet(file_path)
            dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)
    if as_frame:
        return merged_df
    else:
        merged_df.to_parquet("data.parquet")


if __name__ == '__main__':
    df = load_dataset(as_frame=True)
    print(len(df))
