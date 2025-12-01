class Dial:
    def __init__(self):
        self.position = 50
        self.count_zeros = 0
        self.count_pass_zero = 0

    def turn(self, steps):
        dir = 1 if steps >= 0 else -1
        for _ in range(abs(steps)):
            self.turn_once(dir)
        if self.position == 0:
            self.count_zeros += 1
    
    def turn_once(self, step):
        self.position = (self.position + step) % 100
        self.count_pass_zero += self.position == 0

    def get_count_zeros(self):
        return self.count_zeros
    
    def get_count_pass_zero(self):
        return self.count_pass_zero


if __name__ == "__main__":
    with open("inputs/01.txt") as f:
        instructions = [
            int(ins[1:]) * (-1 if ins[0] == "L" else 1) for ins in f.readlines()
        ]
    dial = Dial()
    for step in instructions:
        dial.turn(step)
    print(dial.get_count_zeros())
    print(dial.get_count_pass_zero())
