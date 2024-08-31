line = str(input())
words = line[:80].split()
words_set = set(words)

if len(words) == len(words_set):
    print("yes")
else:
    print("no")
