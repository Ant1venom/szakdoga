from uuid import uuid4


class Connection:
    """
    Class representing a connection.
    Contains its own id, as well as the ids of the two elements that it is connecting.
    """
    def __init__(self, from_id, to_id):
        self.id = uuid4().int
        self.from_id = from_id
        self.to_id = to_id
