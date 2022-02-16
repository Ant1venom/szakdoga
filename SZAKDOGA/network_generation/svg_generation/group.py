class Group:
    """
    Class representing a group, containing a separator and its two dividers, as well as text for each element,
    with their corresponding components.
    """
    def __init__(self, sep, div1, div2, septext=None, div1text=None, div2text=None):
        self.x = 0
        self.y = 0
        self.sep = sep  # svgSeparator or Separator
        self.div1 = div1
        self.div2 = div2  # both svgDividers or Dividers
        self.septext = septext
        self.div1text = div1text
        self.div2text = div2text

    def add_to_svg(self):
        sepsvg = self.sep.add_to_svg()
        div1svg = self.div1.add_to_svg()
        div2svg = self.div2.add_to_svg()

        return f"<svg x='{self.x}' y='{self.y}' width='300' height='200'> {sepsvg}{self.septext.add_to_svg()}" \
               f" {div1svg}{self.div1text.add_to_svg()} {div2svg}{self.div2text.add_to_svg()} </svg>"
