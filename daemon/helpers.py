from shared.models import Notification


def create_notification(title, content, date, source):
    notification = Notification()
    notification.title = title
    notification.content = content
    notification.date = date
    notification.source = source

    return notification
