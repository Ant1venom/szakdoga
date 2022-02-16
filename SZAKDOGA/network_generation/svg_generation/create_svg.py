def create_svg(struct):
    """
    Creates html file from the structure generated by svg_generation_algorithm.py.
    It iterates through each element of the structure, calling the elements' add_to_svg() function,
    then writes the completed string into an html file.

    :param struct:
    :return:
    """
    html = "<!DOCTYPE html>"\
            "<html>"\
            "<body>"
    html += struct.canvas.create_canvas()
    for g in struct.groups:
        html += g.add_to_svg()
    for con in struct.connections:
        html += con.add_to_svg()
    for fs in struct.feed_streams:
        html += fs.add_to_svg()
    for mix in struct.mixers:
        html += mix.add_to_svg()
    html += "</svg>" \
            "</body>"\
            "</html>"

    with open("generated_html.html","w") as f:
        f.write(html)
