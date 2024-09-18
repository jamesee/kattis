'''
0.  find the combination of elements where total equal to K

1.  find permuation

2.  set() to get rid of the duplicates

3.  to check the even(left) steps and odd(right) steps must be equal, else discard


'''
from itertools import permutations
from typing import Tuple, List

def find_permutations(lst :List[str]):
        return list(permutations(lst))

def check_balanced_steps(y:str) -> bool:
    even :int = 0
    odd : int = 0
    for index in range(len(y)):
        if index % 2 == 0:
            even += int(y[index])
        else:
            odd += int(y[index])
    return even == odd

def number_of_ways(lst :List[str]) -> int:
    result :List[str] = []
    output :List[str] = []
    for x in find_permutations(lst):
        result.append("".join(x))

    result_no_duplicates = set(result)
    
    for x in result_no_duplicates:
        if check_balanced_steps(x):
            output.append(x) 
    return len(output)

def running_steps(k :int, s:int) -> Tuple[int, int]:
    lst :List[List[str]] = []
    
    no_of_twos :int = int( s /4)
    no_of_ones :int = int((s % 4) / 2)
    while no_of_twos >= no_of_ones:
        ones :List[str] = []
        twos :List[str] = []
        #print(no_of_twos, no_of_ones)
        for _ in range(no_of_ones):
            ones.append('1')
            ones.append('1')
        for _ in range(no_of_twos):
            twos.append('2')
            twos.append('2')
        lst.append(twos + ones)
        no_of_twos -= 1
        no_of_ones += 2

    count :int = 0
    for x in lst:
        count += number_of_ways(x)
    #print(k, count)
    return (k, count)

def main() -> None:
    results :List[(int,int)] = []
    n :int = int(input())
    for i in range(n):
        k, s = input().strip().split()
        results.append(running_steps(int(k), int(s)))

    for result in results:
        print(*result)

if __name__ == "__main__":
    main()