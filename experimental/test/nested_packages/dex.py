class PokeDex(object):
    def __init__(self):
        self.lookup = {}

    def get_size(self):
        return len(self.lookup)

    def add_pokemon(self, mon, info):
        self.lookup[mon] = info
