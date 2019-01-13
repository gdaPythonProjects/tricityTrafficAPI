from daemon.dataSources import TrojmiastoDataSource


class Fetcher:
    def __init__(self):
        self.sources = [
            TrojmiastoDataSource
        ]

    def fetch(self):
        for source in self.sources:
            try:
                s = source()
                for notification in s.get_data():
                    notification.save()
            except:
                pass
