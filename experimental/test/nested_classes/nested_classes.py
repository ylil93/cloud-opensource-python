class NestedClass(object):
    def __init__(self, i, j, k):
        pass

    def top_function(self, i):
        pass

    class LevelOne(object):
        def __init__(self, x):
            pass

        def one(self, x, y):
            pass

        class LevelTwo(object):
            def __init__(self, a, b):
                pass

            def two(self, a):
                pass

            class LevelThree(object):
                pass

        class EmptyTwo(object):
            pass

    class _LevelIchi(object):
        class LevelNi(object):
            pass

        def ichi(self):
            pass

    class EmptyOne(object):
        pass

