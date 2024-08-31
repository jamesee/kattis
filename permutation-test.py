


def counter(my_list: list[str]):
    element_count = {}

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

# def create_graph(i: int,lst: list[str]) -> list[str]:
#     results = []
#     myset = set(lst)
#     perm = list(myset)
#     lst_count = counter(lst)
#     if i == 0:
#         return list(set(lst))
#     for y in perm:
#         for x in myset:
#             # element_count = counter(y+x)
#             # if element_count.get(perm[0]) != None and (element_count.get(perm[0]) <= lst_count.get(perm[0])):
#             #     results.append(y+x)
#             results.append(y+x)
#             print(results)
#     return create_graph(i - 1, lst, results)

# def create_graph(i: int, myset: set[str], perm: list[str]) -> list[str]:
#     results = []
#     if i == 0:     
#         return perm
#     for y in perm:
#         for x in myset:
#             results.append(y+x)
#     return create_graph(i - 1, myset, results)

def create_graph(i: int, lst: list[str], perm: list[str]) -> list[str]:
    results: list[str] = []
    if i == 0:
        lst_counter = counter(lst)
        while len(perm):
            x = perm.pop()
            if counter(x) == lst_counter and check_balanced_steps(x):
                results.append(x)
        return results
    else:
        while len(perm):
            y = perm.pop()
            for x in set(lst):
                results.append(y+x)
        return create_graph(i - 1, lst, results)

# def find_permutations(lst: list[str]) -> list[str]:
#     myset = set(lst)
#     lst_counter = counter(lst)
#     results = set(create_graph(len(lst) - 1, myset, list(myset)))
#     # results = set(create_graph(len(lst) - 1, lst))

#     permutations =[]
#     for x in results:
#         if counter(x) == lst_counter and check_balanced_steps(x):
#             permutations.append(x)
#     return permutations

def find_permutations(lst: list[str]) -> list[str]:
    return create_graph(len(lst) - 1, lst, list(set(lst)))


def main() -> None:
    lst = ['2', '2', '2', '2', '1', '1']

    i = 1
    for x in find_permutations(lst):
        print(i, x)
        i += 1

if __name__ == "__main__":
    main()