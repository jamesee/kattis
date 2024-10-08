# https://open.kattis.com/problems/rot

from pprint import pprint
from dataclasses import dataclass, field
from typing import Self

DEBUG = True

@dataclass
class Rot:
    rotate: int
    data: list =field(default_factory=list)
    rotated: int = 0

    def __post_init__(self) -> None:
        if DEBUG:
            print('-'*38, '[self.data @ __post_init__]')
            pprint(self.data)
        return self.run()
    
    def rotate_45(self) -> list[list[str]]:
        row, col = len(self.data), len(self.data[0])
        nrow = row + col - 1
        ncol = nrow

        ndata =[[' ' for _ in range(ncol)] for _ in range(nrow)]

        for r in range(row):
            for c in range(col):
                ndata[r + c][c - r + row - 1] = self.data[r][c]
        
        self.data = ndata

        self.rotated += 45
        if self.rotated % 90 == 0:
            self.trim_data()

        if DEBUG:
            print('-'*38, '[self.data after trim]')
            pprint(self.data)      
        return
    
    # def trim_data(self) -> None:
    #     ndata = list()
    #     while self.data:
    #         row = self.data.pop(0)
    #         temp_lst = list()
    #         while row:
    #             ch = row.pop(0)
    #             if ch != ' ':
    #                 temp_lst.append(ch)
    #         if temp_lst != []:
    #             ndata.append(''.join(temp_lst))
    #     self.data = ndata
    #     return

    def trim_data(self) -> None:
        self.data = [ [element for element in row if element != ' '] for row in self.data if any(element != ' ' for element in row)]
        return
        
    def print_data(self) -> None:
        for row in self.data:
            print(''.join(row))
        return
    
    def run(self) -> None:
        while self.rotate:
            self.rotate_45()
            self.rotate -= 45
        return

    @classmethod
    def parse_inputs(cls) -> Self:
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
                print(f"Error: {e}")
                return None
        try:
            rotate = int(input().strip())
            if rotate % 45 != 0:
                raise ValueError("rotate angle must be multiple of 45 [degrees].")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        return cls(rotate=rotate, data=lines)

def main() -> None:

    table = Rot.parse_inputs()
    if not table:
        return

    if DEBUG:
        print('-'*38, '[self.data@main]')
        print(table.rotated)
        pprint(table.data)
        print('-'*38, '[output]')
    return table.print_data()



if __name__ == "__main__":
    main()

'''
echo "3 5
damir
marko
darko
45" | python3 rot.py


echo "3 5
damir
marko
darko
90" | python3 rot.py

echo " 5 5
abcde
bcdef
cdefg
defgh
efghi
315 " | python3 rot.py


'''