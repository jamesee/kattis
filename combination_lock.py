# https://open.kattis.com/problems/combinationlock

from dataclasses import dataclass, field
from enum import Enum, auto

class Dial(Enum):
    CLOCKWISE = auto()
    ANTI_CLOCKWISE = auto()

@dataclass
class CombinationLock:
    offset: int 
    first_num: int
    second_num: int
    third_num: int
    angle:  int = 0
    dial_lst: list = field(default_factory= lambda:list(range(40)))
    ANGLE_PER_UNIT = 9

    def dial(self, target: int, direction: Dial) -> int:
        if self.dial_lst[0] == target:
            return 0
        count = 0
        while self.dial_lst[0] != target:
            if direction == Dial.CLOCKWISE:
                self.dial_lst.insert(0, self.dial_lst.pop())
            else:
                self.dial_lst.append(self.dial_lst.pop(0))
            count += 1
        return count
    
    def dial_1st_num(self):
        self.angle += 720
        self.angle += self.dial(self.first_num, Dial.CLOCKWISE) * self.ANGLE_PER_UNIT
        return

    def dial_2nd_num(self):
        self.angle += 360
        self.angle += self.dial(self.second_num, Dial.ANTI_CLOCKWISE) * self.ANGLE_PER_UNIT
        return

    def dial_3rd_num(self):
        self.angle += self.dial(self.third_num, Dial.CLOCKWISE) * self.ANGLE_PER_UNIT
        return

    def run(self):
        self.dial(self.offset, Dial.CLOCKWISE)
        self.dial_1st_num()
        self.dial_2nd_num()
        self.dial_3rd_num()
        return

def parse_inputs() -> list[int]:
    data = input().strip().split()
    return list(map(int, data))

def dial_lock(lst: list[int]):
    lock = CombinationLock(*lst)
    lock.run()
    print(lock.angle) 

def validate_inputs(lst: list[int]) -> bool:
    for x in lst:
        if x < 0 or x > 39:
            return False
    if len(lst) != 4:
        return False
    return True

def main() -> None:
    n = 2000
    while n:
        lst = parse_inputs()
        if not validate_inputs(lst):
            continue
        if sum(lst) == 0:
            break
        dial_lock(lst)
        n -= 1

if __name__ == "__main__":
    main()
