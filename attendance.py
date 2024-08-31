def print_absentees(absentees :list[str]) -> None:
    if len(absentees) == 0:
        print("No Absences")
    else:
        for absentee in absentees[::-1]:
            print(absentee)

def get_absentees_lst(callout_lst :list[str]) -> list[str]:
    absentees :list[str] =[]
    while len(callout_lst):
        callout = callout_lst.pop()
        if callout == "Present!":
            callout_lst.pop()
        else:
            absentees.append(callout)
    return absentees

def get_callout_lst(n :int) -> list[str]:
    callout_lst :list[str] = []
    while n:
        callout_lst.append(input().strip())
        n -= 1
    return callout_lst

def main() -> None:
    while True:
        student_num = input()
        if student_num.isdigit() and int(student_num) >= 1 and int(student_num) <= 200:
            callout_lst :list[str] = get_callout_lst(int(student_num))
            absentees_lst :list[str] = get_absentees_lst(callout_lst)
            print_absentees(absentees_lst)
            return

if __name__ == "__main__":
    main()
