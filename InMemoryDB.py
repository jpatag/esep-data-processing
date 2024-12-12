class InMemoryDB:
    def __init__(self):
        self.database = {}
        self.current = []
        self.transaction = False

    def get(self, key):
        return self.database.get(key, None)

    def put(self, key, val):
        if self.transaction:
            self.current.append((key, val))
        else:
            raise Exception("Error: Transaction has not yet begun")

    def begin_transaction(self):
        self.transaction = True
        self.current = []

    def commit(self):
        if self.transaction:
            for key, val in self.current:
                self.database[key] = val
        else:
            raise Exception("Error: Transaction has not yet begun")
        self.current = []
        self.transaction = False

    def rollback(self):
        if self.transaction:
            self.current = []
        else:
            raise Exception("Error: Transaction has not yet begun")
        self.transaction = False





