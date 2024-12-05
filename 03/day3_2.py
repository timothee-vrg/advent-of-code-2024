import re

def sum_of_mult(s: str, enabled: bool) -> int:
    res = 0
    regex = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"
    instructions = re.findall(regex,s)
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            a, b = map(int, re.findall(r"\d{1,3}", instruction))
            res += int(a)*int(b)
    return res, enabled

def main():
    res = 0
    enabled = True
    with open("03/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            res_line, enabled = sum_of_mult(line, enabled)
            res += res_line
    print(res)


if __name__ == "__main__":
    main()