from network_generation.json_generation.separate_component import separate_component
from network_generation.json_generation.op_unit import OpUnit


class Separator(OpUnit):
    def __init__(self, input_comps, cuts_at, layer):
        super().__init__(input_comps, layer)
        self.cuts_at = cuts_at
        self.output = separate_component(self.comps, self.cuts_at)
