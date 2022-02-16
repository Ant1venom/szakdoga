def separate_component(comps, sep_at):
    sep = comps[:sep_at]
    others = comps[sep_at:]
    return sep, others

