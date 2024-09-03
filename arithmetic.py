# https://open.kattis.com/problems/arithmetic

import sys

# def convert_octal_to_base(octal_num: str, base: str) -> str:

#     octal = list(octal_num)
#     power = 0
#     decimal = 0
#     while octal:
#         lsb = octal.pop()
#         decimal += int(lsb) * 8**power
#         power += 1

#     result = list()
#     while int(decimal):
#         result.insert(0, base[int(decimal % len(base))])
#         decimal /= len(base)
#     return "".join(result)

# def convert_octal_to_hex(octal_num: str) -> str:
    
#     base = '0123456789ABCDEF'
#     binary = bin(int(octal_num, 8))[2:]

#     result = [base[int(binary[-4 :], 2)]]
#     for n in range(-4, -len(binary), -4):
#         start, end = n - 4 , n
#         result.insert(0, base[int(binary[start:end], 2)])
#     return  ''.join(result)

def convert_octal_to_hex(octal_num: str) -> str:
    return hex(int(octal_num, 8))[2:].upper()

def main() -> None:
    sys.set_int_max_str_digits(200_000)
    try:
        n = input().strip()
        if int(n, 8) < 0 or len(n) >= 200_000:
            raise ValueError
        print(convert_octal_to_hex(n))
    except ValueError as e:
        print(f'Error: {e}')
        return

if __name__ == "__main__":
    main()