# Data model for Foo() and Bar() should be the same

class Foo(object):
    def foo():
        pass

    def moo():
        pass

class Bar(Foo):
    pass

