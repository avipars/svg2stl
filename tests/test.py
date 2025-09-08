# import from src folder

import ..src.svg2stl as svg2stl
# from ..src.svg2stl import convert_svg_to_stl
svg2stl.convert_svg_to_stl("example.svg", thickness=2.0)