from pymongo import MongoClient


class MongoDB:
    def __init__(self) -> None:
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.db = 'GJJ_DB'

        self.devices_coll = self.client[self.db]['Devices']
        self.users_coll = self.client[self.db]['Users']
        self.transactions_coll = self.client[self.db]['Transactions']
        self.notifications_coll = self.client[self.db]['Notifications']