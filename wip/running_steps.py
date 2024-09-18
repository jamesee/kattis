'''
0.  find the combination of elements where total equal to K

1.  find permuation

2.  set() to get rid of the duplicates

3.  to check the even(left) steps and odd(right) steps must be equal, else discard


'''
# from collections import defaultdict

# def counter(my_list: list[str]):
#     element_count = defaultdict(int)

#     for element in my_list:
#         element_count[element] += 1
#     return element_count


def counter(my_list: list[str]):
    element_count = {'1': 0, '2': 0}

    for element in my_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

def check_balanced_steps(y:str) -> bool:
    even :int = 0
    odd : int = 0
    for index in range(len(y)):
        if index % 2 == 0:
            even += int(y[index])
        else:
            odd += int(y[index])
    return even == odd

def mybool(x: list[str], lst: list[str]) -> bool:
    # perm = list(set(lst))
    # perm = ['1', '2']
    lst_counter = counter(lst)
    el_counter = counter(x)

    # if len(el_counter) != 2:
    #     return True
    return el_counter.get('1') <= lst_counter.get('1') and el_counter.get('2') <= lst_counter.get('2')

def create_graph(i: int, lst: list[str], perm: list[str]) -> list[str]:
    results: list[str] = []
    if i == 0:
        lst_counter = counter(lst)
        while len(perm):
            y = perm.pop()
            if counter(y) == lst_counter and check_balanced_steps(y):
                results.append(y)
        return results
    else:
        while len(perm):
            y = perm.pop()
            for x in set(lst):
                if mybool(y+x, lst) == False:
                    continue
                results.append(y+x)
        return create_graph(i - 1, lst, results)

def number_of_ways(lst :list[str]) -> int:
    return len(create_graph(len(lst) - 1, lst, list(set(lst))))

def running_steps(k :int, s:int) -> tuple[int, int]:
    results :list[list[str]] = []
    
    no_of_twos :int = int( s /4)
    no_of_ones :int = int((s % 4) / 2)
    while no_of_twos >= no_of_ones:
        ones :list[str] = []
        twos :list[str] = []
        #print(no_of_twos, no_of_ones)
        for _ in range(no_of_ones):
            ones.append('1')
            ones.append('1')
        for _ in range(no_of_twos):
            twos.append('2')
            twos.append('2')
        results.append(number_of_ways(twos + ones))
        no_of_twos -= 1
        no_of_ones += 2
    return (k, sum(results))

def main() -> None:
    results :list[(int,int)] = []
    n :int = int(input())
    for i in range(n):
        k, s = input().strip().split()
        results.append(running_steps(int(k), int(s)))

    for result in results:
        print(*result)

if __name__ == "__main__":
    main()