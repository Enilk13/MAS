from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People
    from density_grid import Tile, Exit
from typing import List, Deque
from collections import deque
from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def go(
        self,
        person: People,
        aptitude: int,
        width: int,
        height: int,
        current_tile: Tile,
        exits: List[Exit] = None,
        previous_tile: Tile = None,
        traversed_tiles: Deque[Tile] = deque(),
        ) -> None:
        pass

    def out_of_bounds(self, new_x: int, new_y: int, width: int, height: int) -> bool:
        if (new_x < 0 or new_x >= width or new_y < 0 or new_y >= height):
            return True
        return False

