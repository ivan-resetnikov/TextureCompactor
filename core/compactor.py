from dataclasses import dataclass
from .error import *

import pygame as pg


def _combine_textures(
        map_0: pg.Surface|str=None,
        map_1: pg.Surface|str=None,
        map_2: pg.Surface|str=None,
        output: str=""
    ) -> pg.Surface:

    """
    Function "_combine_textures()", combines three single-color maps into a single image.

    Arguments:
    map_0 = Map file or a path to the file, can be a pygame.Surface or a string 
    map_1 = Map file or a path to the file, can be a pygame.Surface or a string 
    map_2 = Map file or a path to the file, can be a pygame.Surface or a string 
    output = Path to the output file, must be a string

    The way textures are being combined, is by storing values from the map 0 on the red channel,
    storing values from the map 1 on the green chanel and values from map 2 on the blue channel.
    """

    use_map_0: bool = True
    use_map_1: bool = True
    use_map_2: bool = True

    
    if isinstance(map_0, str):
        try:
            print("Specified file path for map 0, loading file...")
            print(f"  Source: {map_0}")
            map_0: pg.Surface = pg.image.load(map_0)
            print(f"  Resolution: {map_0.get_size()}")

        except Exception as error:
            print("Error occured white trying to open the map file")
            print(error)

            use_map_0 = False
    
    if isinstance(map_1, str):
        try:
            print("Specified metalness map path, loading file...")
            print(f"  Source: {map_1}")
            map_1: pg.Surface = pg.image.load(map_1)
            print(f"  Resolution: {map_1.get_size()}")
    
        except Exception as error:
            print("Error occured white trying to open the map file")
            print(error)

            use_map_1 = False

    if isinstance(map_2, str):
        try:
            print("Specified AO map path, loading file...")
            print(f"  Source: {map_2}")
            map_2: pg.Surface = pg.image.load(map_2)
            print(f"  Resolution: {map_2.get_size()}")

        except Exception as error:
            print("Error occured white trying to open the map file")
            print(error)
            
            use_map_2 = False

    print("Using maps:")
    print(f"  Using roughness map: {use_map_0}")
    print(f"  Using metalness map {use_map_1}")
    print(f"  Using AO map {use_map_2}")

    if not any([use_map_0, use_map_1, use_map_2]):
        raise AttributeError(ERROR_NO_MAP_IS_USED)


    roughness_map_size_matches: bool = False
    metalness_map_size_matches: bool = False
    ambient_occlusion_map_size_matches: bool = False


    map_size: pg.math.Vector2

    if use_map_0:
        map_size = map_0.get_size()
    
    elif use_map_1:
        map_size = map_1.get_size()
    
    elif use_map_2:
        map_size = map_2.get_size()

    print("Creating output surface...")
    print(f"  Size: {map_size}")

    output_map: pg.Surface = pg.Surface(map_size)


    if not use_map_0 or map_0.get_size() == map_size:
        map_0_size_matches = True

    if not use_map_1 or map_1.get_size() == map_size:
        map_1_size_matches = True
    
    if not use_map_2 or map_2.get_size() == map_size:
        map_2_size_matches = True

    if not all([map_0_size_matches, map_1_size_matches, map_2_size_matches]):
        raise AttributeError(ERROR_MAP_SIZES_DO_NOT_MATCH)

    print("Combining maps...")
    
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            output_map.set_at((x, y), pg.Color(
                map_0.get_at((x, y)).r if use_map_0 else 0,
                map_1.get_at((x, y)).g if use_map_1 else 0,
                map_2.get_at((x, y)).b if use_map_2 else 0
            ))

    print("Saving output map")
    print(f"  Path: {output}")

    pg.image.save(output_map, output)


def _compress_textures(
        texture: pg.Surface|str,
        size: pg.math.Vector2|tuple[int]|list[int]
    ) -> None:

    """
    
    """

    pass


@dataclass
class compactor:
    combine_textures = _combine_textures
    compress_textures = _compress_textures