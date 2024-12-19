def number_of_possibilities(design: str, patterns: list[str]) -> int:

    memo = {}

    def number_of_possibilities_rec(beg: int) -> int:
        if beg in memo:
            return memo[beg]
        
        res = 0
        if beg == len(design):
            return 1
        for pattern in patterns:
            if design[beg:beg+len(pattern)] == pattern:
                res += number_of_possibilities_rec(beg+len(pattern))
        
        memo[beg] = res
        return res

    return number_of_possibilities_rec(0)

def main():
    res = 0
    with open("19/input.txt", "r") as f:
        lines = f.readlines()
        patterns = lines[0].strip().split(", ")
        for line in lines[2:]:
            res += number_of_possibilities(line.strip(), patterns)
    print(res)


if __name__ == "__main__":
    main()