from api.notificationserializer import NotificationSerializer
from shared.models import Notification


class ApiManager:

    def __init__(self):
        self.filters = {
            'last': self.filter_last
        }

    def get(self, params):
        notifications = Notification.objects.all()

        for filter, func in self.filters.items():
            if filter in params:
                notifications = func(notifications, params[filter])

        return NotificationSerializer(notifications, many=True).data

    def filter_last(self, notifications, param):
        return notifications[:int(param)]
