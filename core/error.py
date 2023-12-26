ERROR_MAP_SIZES_DO_NOT_MATCH: str = \
"""
Resolution of maps texture files do not match.
They have to be the same size.

I.E. if roughness map is 4k resolution, all the other maps
(metalness and ambient oclussion map) have to be the same 4k resolution.
"""

ERROR_NO_MAP_IS_USED: str = \
"""
No map was passed to the core.combinator.combine() function.
At least one map is required.
"""