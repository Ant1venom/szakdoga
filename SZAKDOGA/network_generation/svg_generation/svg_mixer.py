from network_generation.svg_generation.random_color import random_color


class SvgMixer:
    """
    Class for the svg representation of a mixer.
    Contains three x,y coordinate pairs, a text containing its components, the element's id, as well as the x coordinate
    and color for its appropriate connection.
    """
    def __init__(self, x1, y1, text, id):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + 35
        self.y2 = y1 + 30
        self.x3 = x1
        self.y3 = y1 + 60
        self.style = "fill:rgb(255,255,255);stroke-width:1;stroke:rgb(0,0,0)"
        self.text = text
        self.id = id
        self.connection_x = 0
        self.connection_color = random_color()

    def add_to_svg(self):
        return f"<polygon points='{self.x1},{self.y1} {self.x2},{self.y2} {self.x3},{self.y3}' style='{self.style}'/>" \
               f"{self.text.add_to_svg()}"
