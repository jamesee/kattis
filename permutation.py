def permute(lst):
    def backtrack(start, end):
        if start == end:
            permutations.append(lst[:])
        for i in range(start, end):
            lst[start], lst[i] = lst[i], lst[start]  # Swap
            backtrack(start + 1, end)
            lst[start], lst[i] = lst[i], lst[start]  # Swap back to restore the original list

    permutations = []
    backtrack(0, len(lst))
    return permutations

def iterative_permutations(lst):
    stack = [(lst, [])]  # Stack initialized with a tuple (remaining elements, current permutation)
    permutations = []

    while stack:
        remaining, current = stack.pop()

        if not remaining:
            if current not in permutations:
                permutations.append(current)
        else:
            for i in range(len(remaining)):
                new_remaining = remaining[:i] + remaining[i+1:]  # Remaining elements excluding the i-th element
                new_current = current + [remaining[i]]           # Append the i-th element to the current permutation
                stack.append((new_remaining, new_current))

    return permutations

def permutations_by_graph(lst):
    stack = [([], lst)]  # Stack initialized with a tuple (current path, remaining elements)
    permutations = []

    while stack:
        path, elements = stack.pop()

        if not elements:
            if path not in permutations:
                permutations.append(path)  # If no elements left, a complete permutation is found
        else:
            for i in range(len(elements)):
                new_path = path + [elements[i]]
                new_elements = elements[:i] + elements[i+1:]
                stack.append((new_path, new_elements))  # Push new state onto the stack

    return permutations

def check_balanced_steps(y:str) -> bool:
    even :int = 0
    odd : int = 0
    for index in range(len(y)):
        if index % 2 == 0:
            even += int(y[index])
        else:
            odd += int(y[index])
    return even == odd

def find_permutations(lst):
    stack = [([], lst)]  # Stack initialized with a tuple (current path, remaining elements)
    permutations = []

    while stack:
        path, elements = stack.pop()

        if not elements:
            if path not in permutations and check_balanced_steps(path):
                permutations.append(path)  # If no elements left, a complete permutation is found
        else:
            for i in range(len(elements)):
                new_path = path + [elements[i]]
                new_elements = elements[:i] + elements[i+1:]
                stack.append((new_path, new_elements))  # Push new state onto the stack

    return permutations


# lst = ['2', '2', '2','2', '1', '1','1','1']
# permutations = find_permutations(lst)

lst = ['A', 'A', 'A','B','B']
permutations = iterative_permutations(lst)
# permutations = permute(lst)
# permutations = permutations_by_graph(lst)

for permutation in permutations:
    print(permutation) # Uncomment to see the result
