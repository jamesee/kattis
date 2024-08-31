#def my_reverse(n :int) -> None:
#    numbers :List[str] = []
#    max_digit :int = 1
#    while n:
#        num :str = input()
#        if len(num) > max_digit:
#            max_digit = len(num)
#        numbers.append(num)
#        n -= 1
#
#    for length in range( 1, max_digit + 1):
#        for el in sorted(filter(lambda x: len(x) == length, numbers), reverse=True):
#            print(el)
#

from typing import List

def my_reverse(n :int) -> None:
    numbers :List[int] = []
    while n:
        numbers.append(int(input()))
        n -= 1

    while len(numbers):
        print(numbers.pop())

def main() -> None:
    n = int(input())
    if n >= 1 and n <= 100_0000:
        my_reverse(n)
    
if __name__ == "__main__":
    main()
