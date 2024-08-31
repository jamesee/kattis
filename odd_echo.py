import sys

num : int = int(input())

x = 0
words = []
while x < num:
    x += 1
    word : str = str(input())
    if len(word) > 100:
        sys.exit("ERROR: Word input must be less than 100.")
    if x % 2 != 0:
        words.append(word)

for word in words:
    print(word)
