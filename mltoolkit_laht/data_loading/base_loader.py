from abc import ABC, abstractmethod
import pandas as pd


class BaseLoader(ABC):

    @abstractmethod
    def load_data(self):
        raise NotImplementedError("Subclasses should implement this method.")

    @abstractmethod
    def get_schema(self):
        raise NotImplementedError("Subclasses should implement this method.")

    @abstractmethod
    def update_schema(self):
        raise NotImplementedError("Subclasses should implement this method.")

    @abstractmethod
    def show_info(self):
        raise NotImplementedError("Subclasses should implement this method.")
