import os
import pandas as pd
import numpy as np
from IPython.display import display
from .base_loader import BaseLoader
from ..utils.logger import Logger


class CSVLoader(BaseLoader):
    def __init__(self, data: pd.DataFrame = None, file_path: str = None) -> None:
        self.file_path = file_path
        self.data = data
        self.logger = Logger.setup_logger(self.__class__.__name__)

        if not isinstance(self.data, pd.DataFrame) and self.file_path is None:
            raise ValueError("Please provide either a DataFrame or a file path.")

    def load_data(self, **kwargs) -> pd.DataFrame:
        """
        Load data from a CSV file.

        Parameters:
        **kwargs: specific parameters for the read_csv or read_pickle method.

        Returns:
        None
        """
        if self.file_path:
            _, file_extension = os.path.splitext(self.file_path)
            file_extension = file_extension[1:]  # remove the leading dot

        if isinstance(self.data, pd.DataFrame):
            print("Loading data from DataFrame...")
            return self.data
        else:
            if file_extension == "csv":
                self.logger.info("Reading data from a CSV file.")
                self.data = pd.read_csv(self.file_path, **kwargs)
            elif file_extension in ["pkl", "pickle"]:
                self.logger.info("Reading data from a pickle file.")
                self.data = pd.read_pickle(self.file_path, **kwargs)
            else:
                msg = f"Unsupported file type: {self.file_path}. Only read .pkl, .pickle, and .csv files."
                self.logger.error(msg)
                raise ValueError(msg)
            return self.data

    def get_schema(self) -> dict:
        return self.data.dtypes.apply(lambda x: x.name).to_dict()

    def update_schema(self, new_schema: dict) -> None:
        self.data = self.data.astype(new_schema)
        return self.data

    def show_info(self, num_rows: int = None, describe_all: str = "all") -> None:
        """
        Print the title and the content to show.

        Parameters:
        title (str): The title to print.
        to_show (Any): The content to print.

        Returns:
        None
        """
        if num_rows:
            pd.set_option("display.max_rows", num_rows)

        decor_title = "-" * 10
        decor_section = "=" * 100
        data = self.data  # load data once

        print(f"{decor_section}\nSAMPLE:\n{decor_section}")
        display(data.head())
        print(f"{decor_section}\nSCHEMA:\n{decor_section}")
        print(data.dtypes)
        print(f"{decor_section}\nDATAFRAME SHAPE:\n{decor_section}")
        print(data.shape)
        print(f"{decor_section}\nNANs:\n{decor_section}")
        print(data.isna().sum())
        print(f"{decor_section}\nGENERAL DUPLICATED:\n{decor_section}")
        print(data.duplicated().sum())
        print(f"{decor_section}\nSTATISTICS:\n{decor_section}")
        display(data.describe(include=describe_all, datetime_is_numeric=True))
        print(f"{decor_section}\nINFO:\n{decor_section}")
        print(data.info())
        for col in data.select_dtypes(exclude=np.number).columns:
            if pd.api.types.is_categorical_dtype(data[col]):
                display(data[col].value_counts())
