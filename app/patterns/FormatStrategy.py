import pandas as pd


class BaseFormat:

    def __init__(self):
        pass

    @staticmethod
    def return_as(dict_data):
        """
        :return: None
        """
        return dict_data


class SimpleDictionaryFormat:

    def __init__(self):
        pass

    @staticmethod
    def return_as(dict_data):
        """
        :return: None
        """
        return dict_data


class DataFrameFormat:

    def __init__(self):
        pass

    @staticmethod
    def return_as(dict_data):
        return pd.DataFrame(dict_data)
