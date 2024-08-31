from itertools import combinations
from typing import Tuple, List

def generate_combinations(boxes :List[int]) -> List[(int,int,int)]:
    return list(combinations(boxes, 3))

def generate_graph(boxes :List[int]) -> List[(int,int,int)]:
    graph_lst = []
    for j in range(len(boxes) - 2):
        for k in range(j + 1, len(boxes) - 1):
            for i in range (k + 1, len(boxes)):
                graph_lst.append((boxes[j], boxes[k], boxes[i]))
    return graph_lst

def parse_input() -> Tuple[List[int], List[int]]:
    raw_input = input().split()
    boxes = sorted(map(int, raw_input[:-2]), reverse=True)
    towers = list(map(int, raw_input[len(raw_input) - 2:]))
    return (boxes, towers)

def main() -> None:
    boxes, towers = parse_input()

    #sum_lst = map(lambda x: (x, sum(x)), generate_combinations(boxes))
    sum_lst = map(lambda x: (x, sum(x)), generate_graph(boxes))
    result1 = list(x[0] for x in sum_lst if  x[1] == towers[0])
    result2 = list(x[0] for x in sum_lst if  x[1] == towers[1])

    if len(result1) != 0: 
        output1 = result1[0]
        output2 = [x for x in boxes if x not in output1]
    elif len(result2) != 0:
        output2 = result2[0]
        output1 = [x for x in boxes if x not in output2]
    else:
        print("No result")

    print(*output1, *output2)

if __name__ == "__main__":
    main()


