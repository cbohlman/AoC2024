class Program:
    def __init__(self, A, B, C, instructions, part):
        self.A = A
        self.B = B
        self.C = C
        self.instructions = instructions
        self.output = []
        self.part = part

    def get_literal_operand(self, opcode):
        return opcode
    
    def get_combo_operand(self, opcode):
        if opcode in range(0,4):
            return opcode
        elif opcode == 4:
            return self.A
        elif opcode == 5:
            return self.B
        elif opcode == 6:
            return self.C
        elif opcode == 7:
            print('Error: hit reserved 7 ')

    def run(self):
        start = 0
        pointer = start
        while True:
            try:
                operation = self.instructions[pointer]
                opcode = self.instructions[pointer + 1]
                if operation == 0:
                    self.adv(opcode)
                    pointer += 2
                elif operation == 1:
                    self.bxl(opcode)
                    pointer += 2
                elif operation == 2:
                    self.bst(opcode)
                    pointer += 2
                elif operation == 3:
                    out = self.jnz(opcode)
                    if out != None:
                        pointer = out
                    else:
                        pointer += 2
                elif operation == 4:
                    self.bxc(opcode)
                    pointer += 2
                elif operation == 5:
                    if self.part == 1:
                        self.out(opcode)
                        pointer += 2
                    elif self.part == 2:
                        valid = self.out(opcode)
                        if not valid:
                            return False
                        pointer += 2
                elif operation == 6:
                    self.bdv(opcode)
                    pointer += 2
                elif operation == 7:
                    self.cdv(opcode)
                    pointer += 2

            except IndexError:
                print('Program Complete')
                print(','.join(map(str, self.output)))
                return True


    def adv(self, opcode):
        numerator = self.A
        denominator = 2**self.get_combo_operand(opcode)
        res = int(numerator/denominator)
        # print(f'adv: {res}')
        self.A = res
    
    def bxl(self, opcode):
        res = self.B ^ self.get_literal_operand(opcode)
        # print(f'bxl: {res}')
        self.B = res

    def bst(self, opcode):
        res = self.get_combo_operand(opcode) % 8 
        # print(f'bst {res}')
        self.B = res

    def jnz(self, opcode):
        if self.A == 0:
            # print(f'jnz zero register')
            return None
        # print(f'jnz: {self.get_literal_operand(opcode)}')
        return self.get_literal_operand(opcode)
    
    def bxc(self, opcode):
        res = self.B ^ self.C
        # print(f'bxc: {res}')
        self.B = res
        
    def out(self, opcode):
        res = self.get_combo_operand(opcode) % 8
        if self.part == 1:
            # print(f'out: {res}')
            self.output.append(res)
        elif self.part == 2:
            if res == self.instructions[len(self.output) + 1]:
                self.output.append(res)
            else:
                return False

    def bdv(self, opcode):
        numerator = self.A
        denominator = 2**self.get_combo_operand(opcode)
        res = int(numerator/denominator)
        # print(f'bdv: {res}')
        self.B = res

    def cdv(self, opcode):
        numerator = self.A
        denominator = 2**self.get_combo_operand(opcode)
        res = int(numerator/denominator)
        # print(f'cdv: {res}')
        self.C = res


def part1(A, B, C, ins):
    prog = Program(A, B, C, ins, 1)
    prog.run()

def part2(A, B, C, ins):
    A = 0
    while True:
        prog = Program(A, B, C, ins, 2)
        if prog.run():
            break
        A += 1

with open('17.in') as f:
    regs, ins = f.read().split('\n\n')
    A, B, C = regs.split('\n')
    A = int(A.split(':')[1])
    B = int(B.split(':')[1])
    C = int(C.split(':')[1])
    ins = list(map(int, ins.split(':')[1].strip().split(',')))
    print(ins)
    print('Part 1:') 
    part1(A, B, C, ins)
    print('Part 2:') 
    part2(A, B, C, ins)