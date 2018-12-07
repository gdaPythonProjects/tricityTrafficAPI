from abc import ABC, abstractmethod


class dataSourceModel(ABC):

    @abstractmethod
    def get(self, date=None):
        pass
