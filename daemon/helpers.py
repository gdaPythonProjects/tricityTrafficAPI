from shared.models import Notification


def create_notification(title, content, date, source):
    notification = Notification(
        title=title,
        content=content,
        date=date,
        source=source
    )

    return notification
