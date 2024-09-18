# https://open.kattis.com/problems/primaryarithmetic

def validate(line: list[str]) -> None:
    numbers = list(map(int, line))
    if len(line) != 2:
        raise TypeError("Expecting exactly 2 inputs.")
    if sum(numbers) == 0:
        raise EOFError
    for number in numbers:
        if number < 0:
            raise ValueError("Negative values not allowed.")
        elif number > 1_000_000_000:
            raise ValueError("Only non-negative less than 10-digits allowed.")

def parse_inputs(max: int) -> list[list[str]]:
    n = max + 1
    lines: list[list[str]] = list()
    while n:
        try:
            line = input().strip().split()
            validate(line)
            lines.append(line)
            n -= 1
        except (ValueError, TypeError) as e:
            print(f"Input error: {e}")
            return
        except EOFError:
            return lines
    print(f"Exceeded maximum {max} lines of inputs.")

def carry_count(numbers: list[int]) -> int:
    number1 = list(map(int, list(numbers[0])))
    number2 = list(map(int, list(numbers[1])))

    # padding zeros up to 10-digits
    while len(number1) < 10:
        number1.insert(0, 0)
    while len(number2) < 10:
        number2.insert(0, 0)
    
    count = 0
    carry = 0
    while len(number1):
        if number1.pop() + number2.pop() + carry > 9:
            count += 1
            carry = 1
        else:
            carry = 0
    return count

def main() -> None:
    lines = parse_inputs(max=3)
    if not lines:
        return

    for line in lines:
        carry = carry_count(line)
        if carry > 1:
            print(f"{carry} carry operations.")
        elif carry == 1:
            print(f"{carry} carry operation.")
        else:
            print("No carry operation.")

if __name__ == "__main__":
    main()