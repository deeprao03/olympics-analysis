import pandas as pd
import numpy as np


def preprocess(df,region_df):

    # merge with region_df
    df = df.merge(region_df,on='NOC',how='left')

    # drop one extra column named as Unnamed:0
    df.drop(columns=["Unnamed: 0"], inplace=True)

    # drop duplicate values
    df.drop_duplicates(inplace=True)

    # one hot encoding medals
    df = pd.concat([df,pd.get_dummies(df['Medal'], dtype=np.uint8)],axis=1)

    return df