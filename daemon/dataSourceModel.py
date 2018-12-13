from abc import ABC, abstractmethod
from shared.models import Notification


class dataSourceModel(ABC):
    def __init__(self, date=None):
        self.notification_list = []
        self.date = date

    @abstractmethod
    def get_data(self):
        pass

    @staticmethod
    def create_notification(title, content, date, source):
        notification = Notification()
        notification.title = title
        notification.content = content
        notification.date = date
        notification.source = source

        return notification
