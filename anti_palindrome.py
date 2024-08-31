
def is_palindrome(words:str) -> bool:
    return words == words[::-1]

def extract_alphabets(line:str)-> list[str]:
    lst:list[str] = []
    for i in range(len(line)):
        if line[i].isalpha():
            lst.append(line.lower()[i])
    return lst

def main() -> None:
    line:str = str(input())
    lst:list[str] = extract_alphabets(line)

    for n in range(2, len(lst) + 1):
        for window in range(len(lst) + 1 - n):
            test:list[str] = lst[window:window + n]
            if is_palindrome(test):
                return print("Palindrome")
    return print("Anti-palindrome")
    
if __name__ == "__main__":
    main()
