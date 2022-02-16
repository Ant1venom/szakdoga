from network_generation.svg_generation.canvas import Canvas
from network_generation.svg_generation.svg_separator import SvgSeparator
from network_generation.svg_generation.svg_divider import SvgDivider
from network_generation.svg_generation.svg_structure import SvgStructure
from network_generation.svg_generation.group import Group
from network_generation.svg_generation.svg_text import SvgText
from network_generation.svg_generation.svg_connection import SvgConnection
from network_generation.svg_generation.svg_mixer import SvgMixer


def svg_generator(ss):
    # TODO cleanup, for sure - check comments
    # TODO speaking of comments, make better comments
    groups = []

    # create groups from each separator and its dividers
    for sep in ss.separators:
        dividers = []
        for div in ss.dividers:
            for con in ss.connections:
                if con.from_id == sep.id and con.to_id == div.id:
                    dividers.append(div)
        groups.append(Group(sep, dividers[0], dividers[1]))

    svg_groups = []
    groups_per_layer = []
    for i in range(ss.layers):
        groups_per_layer.append(0)

    # place each element on the plane relative to their group
    for g in groups:
        svg_groups.append(Group(SvgSeparator(100, 35, g.sep.id, g.sep.layer),
                                SvgDivider(80, 100, g.div1.id),
                                SvgDivider(220, 100, g.div2.id),
                                SvgText(160, 30, f"{g.sep.comps} / {g.sep.cuts_at}"),
                                SvgText(85, 100, f"{g.div1.comps}"), SvgText(225, 100, f"{g.div2.comps}")))
        groups_per_layer[g.sep.layer] += 1
    groups_per_layer = [g for g in groups_per_layer if g != 0]

    # define width and height of canvas based on the number of groups
    width = 300*max(groups_per_layer)+300
    height = 200*(len(groups_per_layer)+2)

    svg = SvgStructure(Canvas(width, height))

    # place dividers on plane for each feed stream
    count = 0
    offset = 300
    for div in ss.dividers:
        if div.layer == 1:
            svg.feed_streams.append(SvgDivider(count * 300 + offset, 75, div.id))
            count += 1
            if count >= 1:
                offset = 600
        else:
            break
    del count

    i = 0
    # place each group on the plane
    for j in groups_per_layer:
        for k in range(j):
            svg_groups[i].x = k * 300
            svg_groups[i].y = (svg_groups[i].sep.layer - 1) * 200
            svg.groups.append(svg_groups[i])
            i += 1
    del i

    # place mixers on the plane
    offset = height / len(ss.mixers) if len(ss.mixers) > 1 else height / 2
    for i, mix in enumerate(ss.mixers):
        small_offset = 10 * (i + 1)
        svgmix = SvgMixer(width - 150, offset * i + (offset / 2),
                          SvgText(width - 150, offset * i + (offset / 2) - 5,
                                  f"{mix.comps}"),
                          mix.id)
        svgmix.connection_x = svgmix.x2 - 35 - small_offset
        svg.mixers.append(svgmix)
        svg.connections.append(SvgConnection(f"{svgmix.connection_x},{svgmix.y2} "
                                             f"{svgmix.x2 - 35},{svgmix.y2}",
                                             svgmix.connection_color))
        svg.connections.append(SvgConnection(f"{svgmix.connection_x},{0} "
                                             f"{svgmix.connection_x},{height}",
                                             svgmix.connection_color))

    # draw connections between separators and dividers

    # draw connections from feed streams to separators and mixers
    for g in svg.feed_streams:  # TODO cleanup here, probably
        x_rso = -20
        y_rso = 0  # small offsets, incrementing with each connection drawn, resetting on each new layer
        for sg in svg_groups:
            x_offset = sg.x
            y_offset = sg.y
            for con in ss.connections:
                if con.from_id == g.id and con.to_id == sg.sep.id:
                    svg.connections.append(SvgConnection(
                        f"{g.x1+ x_rso},{g.y1 + 35} {g.x1 +x_rso},{g.y1 + 40+y_rso} "
                        f"{x_offset + sg.sep.x + 50},{g.y1 + 40+y_rso} "
                        f"{x_offset + sg.sep.x + 50},{y_offset + sg.sep.y}"))
            x_rso += 5
            y_rso += 7
        for mix in svg.mixers:
            for con in ss.connections:
                if con.from_id == g.id and con.to_id == mix.id:
                    if con.to_id == mix.id:
                        svg.connections.append(
                            SvgConnection(f"{g.x1 + x_rso},{g.y1 + 35} "
                                          f"{g.x1+ x_rso},{g.y1+ 40 + y_rso} "
                                          f"{mix.connection_x},{g.y1 + 40 + y_rso}", mix.connection_color))
                        x_rso += 5
                        y_rso += 7

    y_rso = 0
    for i, sg in enumerate(svg_groups):  # TODO cleanup here for sure aswell
        x_rso = -20
        if i > 1 and svg_groups[i-1].sep.layer != svg_groups[i].sep.layer:
            y_rso = 0
        x_offset = sg.x
        y_offset = sg.y  # offset for the dividers' group
        # connections between the groups' separator and dividers
        svg.connections.append(SvgConnection(f"{x_offset + sg.sep.x},{y_offset + sg.sep.y + 17.5} "
                                             f"{x_offset + sg.sep.x - 20},{y_offset+sg.sep.y+17.5} "
                                             f"{x_offset+sg.div1.x1},{y_offset+sg.div1.y1}"))
        svg.connections.append(SvgConnection(f"{x_offset + sg.sep.x + 100},{y_offset + sg.sep.y + 17.5} "
                                             f"{x_offset + sg.sep.x + 120},{y_offset+sg.sep.y+17.5} "
                                             f"{x_offset+sg.div2.x1},{y_offset+sg.div2.y1}"))
        div1_cons = []
        div2_cons = []

        # connections between dividers and other groups' separators
        for con in ss.connections:
            if con.from_id == sg.div1.id:
                div1_cons.append(con)
            if con.from_id == sg.div2.id:
                div2_cons.append(con)

        # connections from the first divider

        for con in div1_cons:
            for g in svg_groups:  # to separators
                if con.to_id == g.sep.id:
                    x_offset2 = g.x
                    y_offset2 = g.y  # offset for the separator's group
                    svg.connections.append(SvgConnection(f"{x_offset + sg.div1.x1 + x_rso},{y_offset + sg.div1.y1 + 35} "
                                                         f"{x_offset+sg.div1.x1+x_rso},{y_offset+sg.div1.y1+40+y_rso} "
                                                         f"{x_offset2+g.sep.x+50},{y_offset+sg.div1.y1+40+y_rso} "
                                                         f"{x_offset2+g.sep.x+50},{y_offset2+g.sep.y}"))
                    x_rso += 5
                    y_rso += 7

            for mix in svg.mixers:  # to mixers
                if con.to_id == mix.id:
                    svg.connections.append(SvgConnection(f"{x_offset + sg.div1.x1 + x_rso},{y_offset + sg.div1.y1 + 35} "
                                                         f"{x_offset+sg.div1.x1+x_rso},{y_offset+sg.div1.y1+40+y_rso} "
                                                         f"{mix.connection_x},{y_offset+sg.div1.y1+40+y_rso}",
                                                         mix.connection_color))
                    x_rso += 5
                    y_rso += 7

        # connections from the second divider
        for con in div2_cons:
            for g in svg_groups:  # to separators
                if con.to_id == g.sep.id:
                    x_offset2 = g.x
                    y_offset2 = g.y
                    svg.connections.append(SvgConnection(f"{x_offset + sg.div2.x1 + x_rso},{y_offset + sg.div2.y1 + 35} "
                                                         f"{x_offset+sg.div2.x1+x_rso},{y_offset+sg.div2.y1 + 40+y_rso} "
                                                         f"{x_offset2+g.sep.x+50},{y_offset+sg.div2.y1+40+y_rso} "
                                                         f"{x_offset2+g.sep.x+50},{y_offset2+g.sep.y}"))
                    x_rso += 5
                    y_rso += 7
            for mix in svg.mixers:  # to mixers
                if con.to_id == mix.id:
                    svg.connections.append(SvgConnection(f"{x_offset + sg.div2.x1 + x_rso},{y_offset + sg.div2.y1 + 35} "
                                                         f"{x_offset+sg.div2.x1+x_rso},{y_offset+sg.div2.y1+40+y_rso} "
                                                         f"{mix.connection_x},{y_offset+sg.div2.y1+40+y_rso}",
                                                         mix.connection_color))
                    x_rso += 5
                    y_rso += 7

    return svg













