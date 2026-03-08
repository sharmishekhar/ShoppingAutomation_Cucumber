import pandas as pd


def get_login_data():

    data = pd.read_csv("data/login_data.csv")

    return data.to_dict("records")



