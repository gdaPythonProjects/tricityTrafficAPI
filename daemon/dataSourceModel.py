from abc import ABC, abstractmethod


def dataSourceModel(ABC):

    @abstractmethod
    def get(self):
        pass
