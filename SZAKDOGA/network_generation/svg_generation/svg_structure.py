class SvgStructure:
    """
    Class representing the entire svg structure.
    Contains all feed streams, mixers, groups, connections and the canvas, all stored in lists.
    """
    def __init__(self, canvas):
        self.feed_streams = []
        self.mixers = []
        self.groups = []
        self.connections = []
        self.canvas = canvas
