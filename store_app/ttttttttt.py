

from enum import IntEnum

class A(IntEnum):
    open = 0
    close = 1
    dummy = 2

print([x.value for x in A])