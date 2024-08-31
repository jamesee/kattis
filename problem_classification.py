# https://open.kattis.com/problems/problemclassification
import sys

def words_count(category: list[str, list[str]], statements: list[str] ) -> dict[str, int]:
    # print(set(category[1][1]))

    #initialise mydict
    mydict = {}
    while len(category[1][1]):
        mydict[category[1][1].pop()] = 0

    for key in mydict:
        # print(key)
        for word in statements:
            if word == key:
                mydict[key] += 1
    # print(mydict, sum(mydict.values()))
    return category[0], sum(mydict.values())

def parse_inputs() -> tuple[dict[str, list[int, list[str]]], list[str]]:
    categories = {}
    num_of_cat = int(input().strip())
    while num_of_cat:
        cat = input().strip().split()
        categories[cat.pop(0)] = [cat.pop(1), cat]
        num_of_cat -= 1

    statements = list()
    while True:
        try:
            statement = input().strip().split()
        except EOFError:
            break
        statements.append(statement)

    flatten_statements = [item for sublist in statements for item in sublist]

    return categories, flatten_statements 

def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

# def parse_inputs() -> tuple[dict[str, list[int, list[str]]], list[str]]:
#     categories = {}
#     lines = readlines()
#     num_of_cat = int(next(lines))
#     while num_of_cat:
#         cat = next(lines).split()
#         categories[cat.pop(0)] = [cat.pop(1), cat]
#         num_of_cat -= 1

#     statements = list()
#     while True:
#         try:
#             statement = next(lines).split()
#         except StopIteration:
#             break
#         statements.append(statement)

#     # print(statements)
#     flatten_statements = [item for sublist in statements for item in sublist]

#     return categories, flatten_statements 


def main() -> None:
    # parse_inputs()
    categories, statements = parse_inputs()


    # print("-"*30, "[categories]", len(categories))
    # print(categories)
    # print('-'*30, '[statements]')
    # print(statements)

    results = list()
    # print('-'*30, '[category]')
    for category in categories.items():
        # print(list(category))
        results.append(words_count(category, statements))

    # print(sorted(results))
    max_count = max(map(lambda x: x[1], results))
    for x in sorted(results):
        if x[1] == max_count:
            print(x[0])

if __name__ == "__main__":
    main()

    # parse_inputs()