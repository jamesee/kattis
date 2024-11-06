
def calculate_areas(w_list: list[int], h_list: list[int]) -> tuple[int, int, int]:

    n = 3
    colors = dict.fromkeys(list(range(n)), 0)
    h_sums = dict.fromkeys(list(range(n)), 0)
    w_sums = dict.fromkeys(list(range(n)), 0)

    for j, h in enumerate(h_list):
        h_sums[j % n] += h
    for i, w in enumerate(w_list):
        w_sums[i % n] += w        

    for i in range(n):
        for j in range(n):
            colors[(i + j) % n] += w_sums[i] * h_sums[j] 

    return tuple(colors.values())



def nthAuspiciousNum(n: int) -> str:
    num = ['8', '9']
    
    result = ''
    i = 1
    while (n - (2**i -1 )) >= 0:
        result = num[(n - (2**i - 1))//2**(i-1)  % 2] + result
        i += 1
    return result