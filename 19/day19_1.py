def is_possible(design: str, patterns: list[str]) -> bool:
    
    used = [False for _ in range(len(patterns))]

    def is_possible_rec(beg: int) -> str:
        if beg == len(design):
            return True
        
        for i, pattern in enumerate(patterns):
            if not used[i] and design[beg:beg+len(pattern)] == pattern:
                used[i] = True
                if is_possible_rec(beg+len(pattern)):
                    return True
                used[i] = False
        return False

    return is_possible_rec(0)

def main():
    res = 0
    with open("19/input.txt", "r") as f:
        lines = f.readlines()
        patterns = lines[0].strip().split(", ")
        for line in lines[2:]:
            if is_possible(line.strip(), patterns):
                res += 1
    print(res)


if __name__ == "__main__":
    main()