
def turn_odd(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return turn_odd(n // 10) * 10 + (n % 10)
    else:
        return  turn_odd(n // 10) * 10 + (n % 10) + 1

print(turn_odd(222111))

print(turn_odd(1234567890))

def diff_pair(lst, n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] - lst[j] == -n or lst[i] - lst[j] == n:
                count += 1

    return count


lst = [75, 80, 90, 77, 88, 91, 60, 74, 73, 70, 55, 93, 59]

print(diff_pair(lst, 10))
print(diff_pair(lst, 14))

