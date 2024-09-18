# https://open.kattis.com/problems/coast


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

def padding(lines: list[list[str]]) -> list[list[str]]:
    for row in lines:
        row.insert(0, '0')
        row.append('0')
    lst = list('0' * len(lines[0]))
    lines.insert(0, lst)
    lines.append(lst)
    return lines

# def costal_1_check(y: int, x: int, lines: list[list[str]]) -> int:
#     if lines[y][x] == '0':
#         return 1
#     return 0

def costal_1_check(y: int, x: int, lines: list[list[str]]) -> int:
    count = 0
    if  lines[y - 1][x] == '0':
        count += 1 
    if  lines[y + 1][x] == '0':
        count += 1 
    if  lines[y][x - 1] == '0':
        count += 1 
    if  lines[y][x + 1] == '0':
        count += 1 
    return count

def costal_0_check(y: int, x: int, lines: list[list[str]]) -> int:
    count = 0
    if  lines[y - 1][x] == '1' and \
        lines[y + 1][x] == '1' and \
        lines[y][x - 1] == '1' and \
        lines[y][x + 1] == '1':
        return -4
    return 0

def costal_length(lines: list[str]) -> int:
    count = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[y]) -1):
            if lines[y][x] == '1':
                count += costal_1_check(y, x, lines)
            else:
                count += costal_0_check(y, x, lines)
    return count

def main() -> None:
    lines = parse_inputs()
    if not lines:
        return
    lines = padding(lines)
    print(costal_length(lines))

if __name__ == "__main__":
    main()

