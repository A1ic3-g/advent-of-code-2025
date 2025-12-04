def max_index(lst):
    max_i = 0
    max_v = lst[0]
    for i, v in enumerate(lst):
        if v > max_v:
            max_v = v
            max_i = i
    return max_i

class Bank:
    def __init__(self, batteries: str):
        self.batts = [b for b in batteries]
    
    def calc_max_jolts_1(self):
        first_i = max_index(self.batts[:-1])
        second_i = max_index(self.batts[first_i + 1 :]) + first_i + 1
        
        return int(f"{self.batts[first_i]}{self.batts[second_i]}")

    def calc_max_jolts_2(self):
        prev_i = 0
        sel = ""
        len_batts = len(self.batts)
        for remaining in range(12, 0, -1):
            i = max_index(self.batts[prev_i:len_batts - remaining + 1])
            sel = sel + self.batts[prev_i + i]
            prev_i = prev_i + i + 1

        return int(sel)
if __name__ == "__main__":
    with open("inputs/03.txt") as f:
        banks = [Bank(line.strip()) for line in f.readlines()]
    
    print("Part 1:")
    print(sum([bank.calc_max_jolts_1() for bank in banks]))
    print("Part 2:")
    print(sum([bank.calc_max_jolts_2() for bank in banks]))
    