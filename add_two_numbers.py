
def add(a:int, b:int) -> int:
    return a + b

mynumlst =[]
line:str = str(input())
for word in line.split():
    if word.isdigit():
        mynumlst.append(int(word))

print(add(mynumlst[0], mynumlst[1]))
