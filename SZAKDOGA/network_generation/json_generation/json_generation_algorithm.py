from network_generation.json_generation.structure import Structure
from network_generation.json_generation.separator import Separator
from network_generation.json_generation.connection import Connection
from network_generation.json_generation.op_unit import OpUnit


# TEMPORARY, FOR TESTING
feed_stream1 = {"id": 1, "comps": ["A", "B", "C", "D"], "layer": 1}
feed_stream2 = {"id": 1, "comps": ["D", "E", "F"], "layer": 1}
product_stream1 = {"id": 3, "comps": ["A", "B"]}
product_stream2 = {"id": 4, "comps": ["B", "C"]}
product_stream3 = {"id": 4, "comps": ["A", "C"]}
product_stream4 = {"id": 4, "comps": ["A", "B", "C"]}


def json_generator():
    """
    From user given feed streams and product streams, it generates a rigorous super-structure.
    """

    ss = Structure()

    # TEMPORARY, FOR TESTING TODO USER INPUTS FOR FEED STREAMS AND PRODUCT STREAMS
    ss.feed_streams.append(feed_stream1)
    # ss.feed_streams.append(feed_stream2)
    ss.product_streams.append(product_stream1)
    ss.product_streams.append(product_stream2)
    # ss.product_streams.append(product_stream3)
    # ss.product_streams.append(product_stream4)
    # ---

    # required for drawing the graph
    layers = 1
    max_dividers_in_single_layer = 0

    # create first dividers for each feed stream
    for fs in ss.feed_streams:
        if len(fs["comps"]) > 1:
            new_div = OpUnit(fs["comps"], layers)
            ss.dividers.append(new_div)
            ss.connections.append(Connection(fs["id"], new_div.id))

    # list of ignored dividers and separators, so as not to make duplicates
    ignored_divs = []

    layers += 1
    while True:
        count = 0
        new_separators = []
        # iterate through each divider
        for div in ss.dividers:
            if div not in ignored_divs:  # create separators only if they don't already exist
                if len(div.comps) > 1:
                    for i in range(1, len(div.comps)):
                        new_sep = Separator(div.comps, i, layers)
                        new_con = Connection(div.id, new_sep.id)
                        ss.separators.append(new_sep)
                        new_separators.append(new_sep)
                        ss.connections.append(new_con)
                    ignored_divs.append(div)
            else:  # count ignored dividers
                count += 1

        if count == len(ignored_divs):
            break

        no_of_new_dividers = 0
        # iterate through each separator
        for sep in new_separators:  # create dividers only if they don't already exist
            # all separators need 2 dividers
            new_div1 = OpUnit(sep.output[0], layers)
            new_div2 = OpUnit(sep.output[1], layers)
            ss.dividers.append(new_div1)
            ss.dividers.append(new_div2)
            ss.connections.append(Connection(sep.id, new_div1.id))
            ss.connections.append(Connection(sep.id, new_div2.id))
            no_of_new_dividers += 2
        if no_of_new_dividers > max_dividers_in_single_layer:
            max_dividers_in_single_layer = no_of_new_dividers
        layers += 1

    # create mixers for each product stream
    for ps in ss.product_streams:
        ss.mixers.append(OpUnit(ps["comps"], layers))

    # create bypass from all dividers
    for div in ss.dividers:
        for mix in ss.mixers:
            if set(div.comps).issubset(mix.comps):
                ss.connections.append(Connection(div.id, mix.id))

    ss.max_dividers_in_single_layer = max_dividers_in_single_layer
    ss.layers = layers

    return ss





