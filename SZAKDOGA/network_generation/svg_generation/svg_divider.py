class SvgDivider:
    """
    Class for the svg representation of a divider.
    Contains three x,y coordinate pairs and the element's id.
    """
    def __init__(self, x1, y1, id):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1+30
        self.y2 = y1+35
        self.x3 = x1-30
        self.y3 = y1+35
        self.style = "fill:rgb(255,255,255);stroke-width:1;stroke:rgb(0,0,0)"
        self.id = id

    def add_to_svg(self):
        return f"<polygon points='{self.x1},{self.y1} {self.x2},{self.y2} {self.x3},{self.y3}' style='{self.style}'/>"