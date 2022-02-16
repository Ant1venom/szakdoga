from svg_generation_algorithm import svg_generator
from create_svg import create_svg
from network_generation.json_generation.json_generation_algorithm import json_generator
from network_generation.json_generation.create_json import create_json


def main():
    ss = json_generator()  # create structure for json file
    create_json(ss)  # write data to json file
    svg = svg_generator(ss)  # create structure for svg
    create_svg(svg)  # write data to html


if __name__ == "__main__":
    main()
