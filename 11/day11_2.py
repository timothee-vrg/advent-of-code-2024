memo_dict = {}

def number_of_stones(x: int, n: int) -> int:
    if n == 0:
        return 1
    if (x,n) in memo_dict:
        return memo_dict[(x,n)]
    
    if x == 0:
        res = number_of_stones(1, n-1)
        memo_dict[(x,n)] = res
        return res
    length_of_x = len(str(x))
    if length_of_x%2==0:
        res = number_of_stones(int(str(x)[:length_of_x//2]), n-1) + number_of_stones(int(str(x)[length_of_x//2:]), n-1)
        memo_dict[(x,n)] = res
        return res
    else:
        res = number_of_stones(x*2024, n-1)
        memo_dict[(x,n)] = res
        return res

def main():
    res = 0
    number_of_blinks = 75
    with open("11/input.txt", "r") as f:
        line = f.readline()
        numbers = list(map(int, line.split()))
        for number in numbers:
            res += number_of_stones(number, number_of_blinks)

    print(res)


if __name__ == "__main__":
    main()