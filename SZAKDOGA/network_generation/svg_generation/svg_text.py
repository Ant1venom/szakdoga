class SvgText:
    """
    Class representing text in svg form.
    Contains x,y coordinates, as well as the text itself.
    """
    def __init__(self,x,y,text):
        self.x = x
        self.y = y
        self.text = text

    def add_to_svg(self):
        return f"<text x='{self.x}' y='{self.y}' font-family='verdana' font-size='9'>{self.text}</text>"