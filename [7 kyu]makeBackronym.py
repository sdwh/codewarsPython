#preloaded variable: "dictionary"

def make_backronym(acronym):
    return ' '.join([dictionary[c.upper()] for c in acronym])