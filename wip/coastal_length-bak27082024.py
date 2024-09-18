# https://open.kattis.com/problems/coast

from dataclasses import dataclass, field

@dataclass
class Coastal:
    data: list[list[str]] = field(default_factory=list)
    count: int = 0

    def __post_init__(self):
        # padding
        for row in self.data:
            row.insert(0, '0')
            row.append('0')
        lst = list('0' * len(self.data[0]))
        self.data.insert(0, lst)
        self.data.append(lst)
        return self.coastal_length()
    
    def costal_1_check(self, y: int, x: int) -> None:
        def check(y: int, x:int) -> None:
            if self.data[y][x] == '0':
                self.count += 1
            return
        
        check(y - 1, x)
        check(y + 1, x)
        check(y, x - 1)
        check(y, x + 1)
        return
    
    def costal_0_check(self, y: int, x: int) -> None:
        def check(y: int, x: int) -> bool:
            if self.data[y][x] == '1':
                return True
            return False
        
        if  check(y - 1, x) and \
            check(y + 1, x) and \
            check(y, x - 1) and \
            check(y, x + 1):
            self.count -= 4
        return
    
    def coastal_length(self) -> None:
        for y in range(1, len(self.data) - 1):
            for x in range(1, len(self.data[y]) -1):
                if self.data[y][x] == '1':
                    self.costal_1_check(y, x)
                else:
                    self.costal_0_check(y, x)
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


if __name__ == "__main__":
    main()
