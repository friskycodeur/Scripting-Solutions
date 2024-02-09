"""
Make sure to install fontTools library before use
via pip install fontTools
"""

#!/usr/bin/env python
from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

with TTFont(
    sys.argv[1], 0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1
) as ttf:
    chars = chain.from_iterable(
        [y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables
    )
    if len(sys.argv) == 2:
        for c in chars:
            print(c)
    elif len(sys.argv) >= 3:
        code_points = {c[0] for c in chars}
        for i in sys.argv[2:]:
            code_point = int(i)
            #code_point = ord(i)  # search character
            print(Unicode[code_point])
            print(code_point in code_points)