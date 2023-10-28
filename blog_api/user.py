class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }