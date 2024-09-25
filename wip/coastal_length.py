# https://open.kattis.com/problems/coast

from dataclasses import dataclass, field
from pprint import pprint
from collections import deque

DEBUG   = False

@dataclass
class Coastal:
    map: list[list[str]] = field(default_factory=list)
    queue: deque = field(default_factory=deque, init=False)
    # created queue_set to improve time complexity in find element in set O(1) rather than in list O(n)
    # queue_set: deque = field(default_factory=set, init=False)
    count: int = 0

    def __post_init__(self):
        self.padding()
        self.row, self.col = len(self.map) - 1, len(self.map[0]) - 1
        self.run()
        return
    
    def padding(self) -> None:
        # padding
        for row in self.map:
            row.insert(0, '0')
            row.append('0')
        lst = list('0' * len(self.map[0]))
        self.map.insert(0, lst)
        self.map.append(lst)
        return
    
    def floodfill_sea_dfs(self) -> None:
        dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def dfs(r: int, c: int) -> None:
            if r < 0 or r > self.row or c < 0 or c > self.col or self.map[r][c] == '~':
                return

            if self.map[r][c] == '1':
                self.count += 1
                return
            elif self.map[r][c] == '0':
                self.map[r][c] = '~'
                for dr, dc in dir:
                    dfs(r + dr, c + dc)
            return
        # start 
        dfs(0, 0)
        return

    def floodfill_sea_bfs(self) -> None:
        dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while self.queue:
            y, x = self.queue.popleft()
            # self.queue_set.discard((y,x))

            self.map[y][x] = '~'
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if (0 <= ny <= self.row) and (0 <= nx <= self.col) and self.map[ny][nx] != '~':
                    if self.map[ny][nx] == '1':
                        self.count += 1
                    elif self.map[ny][nx] == '0' and (ny, nx) not in self.queue:
                    # elif self.map[ny][nx] == '0' and (ny, nx) not in self.queue_set:
                        self.queue.append((ny, nx))
                        # self.queue_set.add((ny, nx))
               
        return
    
    def run_bfs(self, case: str) -> None:
        if case == 'Case1':
            starts = [(0,0)] # Case 1
        elif case == 'Case2':
            starts = [(0,0), (self.row, self.col)] # Case 2
        elif case == 'Case3':
            starts = [(0,0), (self.row, self.col), (0, self.col), (self.row, 0)] # Case 3
        else:
            # Case 4
            starts = list()
            for x in range(self.col + 1):
                starts.append((0, x))
            for y in range(1, self.row):
                starts.append((y,0))
                starts.append((y, self.col))
            for x in range(self.col + 1):
                starts.append((self.row, x))

        for y, x in starts:
            self.queue.append((y, x))
            # self.queue_set.add((y, x))

        if DEBUG:
            print('-'*50, "[starting queue]")
            print(self.queue)

        return self.floodfill_sea_bfs()
    
    def run_dfs(self) -> None:
        return self.floodfill_sea_dfs()
    
    def run(self) -> None:
        '''
        Case0: Used floodfill with dfs and start at (0,0)
            1. count = 86 is wrong. (actual count should be 94)
            2. cannot understand why (8,7) cell cannot be reached i.e. self.map[8][7] = '0'
        '''
        # self.run_dfs()

        '''
        Case1 : Used floodfill with bfs and start at (0,0)
            1. same result as floodfill with dfs.
            2. count = 86 is wrong. (actual count should be 94)
            3. cannot understand why (8,7) cell cannot be reached i.e. self.map[8][7] = '0'
        '''
        # self.run_bfs('Case1')

        '''
        Case2 : Used floodfill with bfs and start at (0,0) and (9, 11)
            1. managed to reach (8, 7) ie self.map[8][7] = '~'
            2. but count = 91 is wrong. (actual count should be 94)
        '''
        # self.run_bfs('Case2')

        '''
        Case3 : Used floodfill with bfs and start at 4 corners [(0,0), (0, 11), (9, 0) (9, 11)]
            1. managed to reach (8, 7) ie self.map[8][7] = '~'
            2. count = 94 is correct. (actual count should be 94)
            3. faced time exceeded when submit to kattis i.e. too slow
        '''
        self.run_bfs('Case3')

        '''
        Case4 : Used floodfill with bfs and start at all cells along the perimeter of map.
            1. managed to reach (8, 7) ie self.map[8][7] = '~'
            2. count = 94 is correct. (actual count should be 94)
            3. no improvement in term of time. Still faced "time exceeded" when submit to kattis.
        '''
        # self.run_bfs('Case4')
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
    
    coastal = Coastal(map = lines)

    if DEBUG:
        print('-'*50, "[costal length]")
    print(coastal.count)
    if DEBUG:
        print('-'*50, "[map]")
        pprint(coastal.map)

if __name__ == "__main__":
    main()

'''
❯ echo "8 10
0111011100
0100000011
0111111010
1000000011
1111111100
1000001010
0110101000
0000110111
" | python3 coastal_length.py

====================================================================[dfs]
-------------------------------------------------- [costal length]
86
-------------------------------------------------- [map]
[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '1', '1', '1', '~', '1', '1', '1', '~', '~', '~'],
 ['~', '~', '1', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '~', '1', '1', '1', '1', '1', '1', '~', '1', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '1', '1', '1', '1', '1', '1', '1', '1', '~', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '1', '~', '1', '~', '~'],
 ['~', '~', '1', '1', '~', '1', '~', '1', '~', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '1', '1', '0', '1', '1', '1', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
====================================================================[bfs-Case 1]
-------------------------------------------------- [starting queue]
[(0, 0)]
-------------------------------------------------- [costal length]
86
-------------------------------------------------- [map]
[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '1', '1', '1', '~', '1', '1', '1', '~', '~', '~'],
 ['~', '~', '1', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '~', '1', '1', '1', '1', '1', '1', '~', '1', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '1', '1', '1', '1', '1', '1', '1', '1', '~', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '1', '~', '1', '~', '~'],
 ['~', '~', '1', '1', '~', '1', '~', '1', '~', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '1', '1', '0', '1', '1', '1', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
 
====================================================================[bfs-Case 2]
-------------------------------------------------- [starting queue]
[(0, 0), (9, 11)]
-------------------------------------------------- [costal length]
91
-------------------------------------------------- [map]
[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '1', '1', '1', '~', '1', '1', '1', '~', '~', '~'],
 ['~', '~', '1', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '~', '1', '1', '1', '1', '1', '1', '~', '1', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '1', '1', '1', '1', '1', '1', '1', '1', '~', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '1', '~', '1', '~', '~'],
 ['~', '~', '1', '1', '~', '1', '~', '1', '~', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '1', '1', '~', '1', '1', '1', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

====================================================================[bfs-Case 3]
-------------------------------------------------- [starting queue]
[(0, 0), (9, 11), (0, 11), (9, 0)]
-------------------------------------------------- [costal length]
94
-------------------------------------------------- [map]
[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '1', '1', '1', '~', '1', '1', '1', '~', '~', '~'],
 ['~', '~', '1', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '~', '1', '1', '1', '1', '1', '1', '~', '1', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '1', '1', '1', '1', '1', '1', '1', '1', '~', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '1', '~', '1', '~', '~'],
 ['~', '~', '1', '1', '~', '1', '~', '1', '~', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '1', '1', '~', '1', '1', '1', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

====================================================================[bfs-Case 4]
 -------------------------------------------------- [starting queue]
[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), 
(1, 0), (1, 11), (2, 0), (2, 11), (3, 0), (3, 11), (4, 0), (4, 11), (5, 0), (5, 11), (6, 0), (6, 11), (7, 0), (7, 11), (8, 0), (8, 11), 
(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11)]
-------------------------------------------------- [costal length]
94
-------------------------------------------------- [map]
[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
 ['~', '~', '1', '1', '1', '~', '1', '1', '1', '~', '~', '~'],
 ['~', '~', '1', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '~', '1', '1', '1', '1', '1', '1', '~', '1', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '~', '~', '1', '1', '~'],
 ['~', '1', '1', '1', '1', '1', '1', '1', '1', '~', '~', '~'],
 ['~', '1', '~', '~', '~', '~', '~', '1', '~', '1', '~', '~'],
 ['~', '~', '1', '1', '~', '1', '~', '1', '~', '~', '~', '~'],
 ['~', '~', '~', '~', '~', '1', '1', '~', '1', '1', '1', '~'],
 ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
'''