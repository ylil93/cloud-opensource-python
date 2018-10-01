class PokeBall(object):
    def __init__(self):
        self.CATCH_RATE = 1.0

    def get_catch_rate(self):
        return self.CATCH_RATE


class GreatBall(PokeBall):
    def __init__(self):
        self.CATCH_RATE = 1.5


class UltraBall(PokeBall):
    def __init__(self):
        self.CATCH_RATE = 2.0


class MasterBall(PokeBall):
    def __init__(self):
        self.CATCH_RATE = 225
