
def sort(a:int, b:int)-> (int, int):
    if a > b:
        return b, a
    else:
        return  a, b

def first_2_integers(line:str) -> (int, int):
    lst: list[int] = []
    for word in line.split():
        if word.isdigit() and int(word) >= 0 and int(word) <= 1_000_000:
                lst.append(int(word))
    return int(lst[0]), int(lst[1])

a, b = first_2_integers(str(input()))
a, b = sort( a, b)
print( a, b)
