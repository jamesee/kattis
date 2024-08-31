
def choice1():
    y = 1000
    if y < 10:
        x = 2
    else:
        if y > 100:
            x = 2

    print(x)


def choice2():
    y = 1000
    if y > 0:
        x = 1
    elif y > 100:
        x = 2
    elif y > 1000:
        x = 3
    print(x)


#def sum_odd_n(n):
#    sum = 0
#    for x in range(2*n):
#        if x % 2:
#            sum += x
#    return sum
#

# def sum_odd_n(n):
#     sum = 0
#     x = 2 * n - 1
#     while x:
#         if x % 2:
#             sum += x
#         x -= 1
#     return sum

#def sum_n_squares(n):
#    result = 0
#    for counter in range(n+1):
#        result += counter ** 2
#    return result
#
# def sum_n_squares(n):
#     counter, result = 1, 0
#     while counter <= n:
#         result += counter**2
#         counter += 1
#     return result

# def multiply_two_things(a, b):
#     return a*b

def sum_odd_n(n):
    if n == 1:
        return 1
    return sum_odd_n(n - 1) + 2 * n -1

if __name__ == "__main__":
    #choice1()
    #choice2()
#    print(sum_odd_n(5))
#    print(sum_odd_n(4))
#    print(sum_odd_n(1))
#
#    print(sum_n_squares(5))
#    print(sum_n_squares(4))
#    print(sum_n_squares(1))
#
    print(sum_odd_n(5))
    print(sum_odd_n(4))
    print(sum_odd_n(1))