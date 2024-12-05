import re

def sum_of_mult(s: str) -> int:
    res = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    occurences = re.findall(regex,s)
    for a, b in occurences:
        res += int(a)*int(b)
    return res

def main():
    res = 0
    with open("03/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            res += sum_of_mult(line)
    print(res)


if __name__ == "__main__":
    main()