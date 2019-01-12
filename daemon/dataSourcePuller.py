

class DataSourcePuller:
    def __init__(self):
        self.sources = [

        ]

    def pull_data(self):
        for source in self.sources:
            try:
                s = source()
                for notification in s.get_data():
                    notification.save()
            except:
                pass
