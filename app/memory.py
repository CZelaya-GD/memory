from sqlitedict import SqliteDict

class MemoryDB:
    def __init__(self, db_path="/data/memory.sqlite", autocommit=True):
        self.db = SqliteDict(db_path, autocommit=autocommit)

    def store(self, prompt, output):
        self.db[prompt] = output

    def retrieve(self, prompt):
        return self.db.get(prompt, None)

    def search(self, keyword):
        return [(k, v) for k, v in self.db.items() if keyword in k or keyword in str(v)]

    def all_memories(self):
        return list(self.db.items())

    def delete(self, prompt):
        if prompt in self.db:
            del self.db[prompt]

    def close(self):
        self.db.close()
