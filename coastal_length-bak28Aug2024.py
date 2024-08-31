# https://open.kattis.com/problems/coast

from dataclasses import dataclass, field
from typing import Callable
from pprint import pprint

@dataclass
class Coastal:
    data: list[list[str]] = field(default_factory=list)
    stackV: list[tuple[int, int]] = field(default_factory=list)
    stack1: list[tuple[int, int]] = field(default_factory=list)
    count: int = 0

    def __post_init__(self):
        # padding
        for row in self.data:
            row.insert(0, '~')
            row.append('~')
        lst = list('~' * len(self.data[0]))
        self.data.insert(0, lst)
        self.data.append(lst)
        return self.coastal_length()
    
    def calculate_walls(self, y: int, x: int) -> None:
        def is_coast(y: int, x:int) -> None:
            if self.data[y][x] == '~':
                self.count += 1
            return
        
        is_coast(y - 1, x)
        is_coast(y + 1, x)
        is_coast(y, x - 1)
        is_coast(y, x + 1)
        return
    
    def is_sea(self, y: int, x: int) -> bool:
            if self.data[y][x] == '~':
                return True
            return False
            
    def look_for_zeros(self, y: int, x: int) -> None:
        if  self.is_sea(y - 1, x) or self.is_sea(y + 1, x) or \
            self.is_sea(y, x - 1) or self.is_sea(y, x + 1):
            self.data[y][x] = '~'
        else:
            self.data[y][x] = '#'
            self.stackV.append((y,x))
        return
    
    def backtrack(self) -> None:
        while len(self.stackV):
            y, x = self.stackV.pop()
            if  self.is_sea(y - 1, x) or self.is_sea(y + 1, x) or \
                self.is_sea(y, x - 1) or self.is_sea(y, x + 1):
                self.data[y][x] = '~'
    
    def process_ones(self):
        while len(self.stack1):
            y, x = self.stack1.pop()
            self.calculate_walls(y, x)

    def forward(self, f: Callable[[int, int], None], target: str) -> None:
        for y in range(1, len(self.data) - 1):
            for x in range(1, len(self.data[y]) -1):
                if self.data[y][x] == '0':
                    f(y, x)

    def coastal_length(self) -> None:
        # self.forward(self.look_for_zeros, '0')
        for y in range(1, len(self.data) - 1):
            for x in range(1, len(self.data[y]) -1):
                if self.data[y][x] == '0':
                    self.look_for_zeros(y, x)
                elif self.data[y][x] == '1':
                    self.stack1.append((y, x))
        # self.backtrack()
        # self.process_ones()
        return

def parse_inputs() -> list[list[int]]:
    n, m = input().strip().split()
    n = int(n)
    lines = list()
    while n:
        try:
            line = input().strip()
            if len(line) != int(m):
                raise TypeError(f"TypeError: Length of string must be {m}.")
            line = list(line)
            lines.append(line)
            n -= 1
        except TypeError as e:
            print(e)
            return
    return lines

def main() -> None:
    lines = parse_inputs()
    if not lines:
        return
    coastal = Coastal(data = lines)
    print(coastal.count)
    pprint(coastal.data)
    print(coastal.stackV)

if __name__ == "__main__":
    main()
'''



echo "5 6
011110
010010
110100
001010
000000
" | python3 coastal_length.py



echo "5 6
011110
010010
100100
011010
000000
" | python3 coastal_length.py
22

echo "5 8
01111100
01010010
10010010
00101100
00000000
" | python3 coastal_length.py

[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '1', '1', '1', '1', '1', '~', '~', '~'],
 ['~', '~', '1', '#', '1', '#', '#', '1', '~', '~'],
 ['~', '1', '~', '#', '1', '#', '#', '1', '~', '~'],
 ['~', '~', '~', '1', '~', '1', '1', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

'''