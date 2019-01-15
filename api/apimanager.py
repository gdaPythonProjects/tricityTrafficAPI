from api.notificationserializer import NotificationSerializer
from shared.models import Notification


class ApiManager:

    def get(self, params):
        notifications = Notification.objects.all()
        if params is None or len(params):
            pass
        return NotificationSerializer(notifications, many=True).data
