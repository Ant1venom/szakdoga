from uuid import uuid4


class OpUnit:
    def __init__(self, input_comps, layer):
        self.id = uuid4().int
        self.comps = input_comps
        self.layer = layer