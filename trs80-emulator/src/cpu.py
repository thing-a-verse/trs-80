class CPU:
    def __init__(self):
        self.registers = [0] * 8  # Example: 8 general-purpose registers
        self.program_counter = 0
        self.stack_pointer = 0
        self.memory = [0] * 65536  # 64KB of memory
        self.reset()

    def reset(self):
        self.registers = [0] * 8
        self.program_counter = 0
        self.stack_pointer = 0

    def execute_instruction(self, instruction):
        # Placeholder for instruction execution logic
        pass

    def load_program(self, program):
        # Load a program into memory
        self.memory[:len(program)] = program

    def get_state(self):
        return {
            'registers': self.registers,
            'program_counter': self.program_counter,
            'stack_pointer': self.stack_pointer
        }