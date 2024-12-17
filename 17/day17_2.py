def parse_input(lines: list[str]) -> list[int]:
    _, value = lines[4].split(":")
    return list(map(int,value.split(",")))

def get_output(a: int, b: int, c: int, prog: list[int]) -> list[int]:

    def get_literal_operand(operand: int) -> int:
        return operand
    
    def get_combo_operand(operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        elif 4 <= operand <= 6:
            return registers[operand-4]
        raise Exception("Invalid program")
    
    def adv(op: int) -> None:
        operand = get_combo_operand(op)
        registers[0] //= 2**operand
    
    def bxl(op: int) -> None:
        operand = get_literal_operand(op)
        registers[1] ^= operand

    def bst(op: int) -> None:
        operand = get_combo_operand(op)
        registers[1] = operand % 8

    def jnz(op: int) -> None:
        if registers[0] == 0: return
        operand = get_literal_operand(op)
        instruction_pointer[0] = operand - 2
    
    def bxc(_: int) -> None:
        registers[1] ^= registers[2] 

    def out(op: int) -> None:
        operand = get_combo_operand(op)
        res.append(operand%8)
    
    def bdv(op: int) -> None:
        operand = get_combo_operand(op)
        registers[1] = registers[0]//(2**operand)
    
    def cdv(op: int) -> None:
        operand = get_combo_operand(op)
        registers[2] = registers[0]//(2**operand) 

    registers = [a,b,c]
    instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    
    res = []
    instruction_pointer = [0]

    while instruction_pointer[0] < len(prog) - 1:
        instruction = instructions[prog[instruction_pointer[0]]]
        operand = prog[instruction_pointer[0]+1]
        instruction(operand)
        instruction_pointer[0] += 2
    
    return res

def minimal_copy(prog: list[int]) -> int:
    valid = [0]
    for length in range(1, len(prog)+1):
        old_valid, valid = valid, []
        for number in old_valid:
            for offset in range(8):
                new_number = 8 * number + offset
                if get_output(new_number, 0, 0, prog) == prog[-length:]:
                    valid.append(new_number)

    answer = min(valid)
    return answer

def main():
    with open("17/input.txt", "r") as f:
        lines = f.readlines()
        prog = parse_input(lines)
    print(minimal_copy(prog))


if __name__ == "__main__":
    main()