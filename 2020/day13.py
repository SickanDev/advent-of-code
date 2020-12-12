import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 13).getData()
# i = Input(2020, 13).getFromExample()


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)

    return 0


def PartTwo(info):
    # noParseInfo = info
    info = strToArr(info)

    return 0


print("Input:\n", i)
print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
print("\n--------Runtime--------")
print("Part 1:", str((timeit.timeit(
    f"PartOne(i)", globals=locals(), number=1000))) + "ms")
print("Part 2:", str((timeit.timeit(
    f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
