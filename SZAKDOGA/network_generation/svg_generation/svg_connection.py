class SvgConnection:
    """
    Class for the svg representation of a connection.
    Contains x,y coordinate pairs and the color of the line.
    """
    def __init__(self, points, color="black"):
        self.points = points
        self.color = color

    def add_to_svg(self):
        return f"<polyline points='{self.points}' style='fill:none;stroke:{self.color};stroke-width:1'/>"
