class SvgSeparator:
    """
    Class for the svg representation of a separator.
    Contains x,y coordinates, width and height, as well as the element's id and its layer on the plane.
    """
    def __init__(self, x, y, id, layer):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 35
        self.style = "fill:rgb(255,255,255);stroke-width:1;stroke:rgb(0,0,0)"
        self.id = id
        self.layer = layer

    def add_to_svg(self):
        return f"<rect x='{self.x}' y='{self.y}' width='{self.width}' height='{self.height}' style='{self.style}' />"
