class Canvas:
    """
    Class representing the canvas for the svg structure.
    Contains the canvas' width and height.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_canvas(self):
        return f"<svg width = '{self.width}' height = '{self.height}' style=''>"