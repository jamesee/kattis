
def three_in_a_row(n :int) -> int:
    a = 1
    while a * (a + 1) *(a + 2) < n:
        a += 1
    return a - 1

def main() -> None:
    while True:
        n :int = int(input())
        if n >= 1 and n <= 1_000_000_000:
            print(three_in_a_row(n))
            return

if __name__ == "__main__":
    main()
