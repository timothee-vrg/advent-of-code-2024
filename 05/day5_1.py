def compute_score(query: list[int]) -> int:
    length = len(query)

    for i in range(length):
        for j in range(i):
            if (query[i],query[j]) in priority_rules:
                return 0
    
    return query[length//2]

def main():
    global priority_rules
    res = 0
    priority_rules = set()
    with open("05/input.txt", "r") as f:
        PARSE_RULES = 1
        PARSE_QUERY = 2
        lines = f.readlines()
        parse_type = PARSE_RULES
        for line in lines:
            if line == "\n":
                parse_type = PARSE_QUERY
            elif parse_type == PARSE_RULES:
                priority_rules.add(tuple(map(int, line.split("|"))))
            elif parse_type == PARSE_QUERY:
                query = list(map(int,line.split(",")))
                res += compute_score(query)
    print(res)


if __name__ == "__main__":
    main()