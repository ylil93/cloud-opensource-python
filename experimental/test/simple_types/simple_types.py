import collections
import enum

MyNamedTuple = collections.namedtuple('MyNamedTuple', ['x', 'y'])

class MyEnum(enum.Enum):
    LOW = enum.auto()
    MEDIUM = enum.auto()
    HIGH = enum.auto()

class MyIntEnum(enum.IntEnum):
    ON = 1
    OFF = 2

class MyIntFlag(enum.IntFlag):
    R = 4
    W = 2
    X = 1

class MyFlag(enum.Flag):
    RED = enum.auto()
    GREEN = enum.auto()
    BLUE = enum.auto()

class MyClass(object):
    def __init__(self, x, y):
        pass

    def foo(self, a, b, c):
        pass

    def boo(self):
        pass

class _IgnoredClass():
    pass

def my_function(a, b):
    pass

def _ignored_function():
    pass

