# trs80-emulator/src/main.py

from cpu import CPU
from memory import Memory
from display import Display
from keyboard import Keyboard
import argparse

def load_program(memory, filename):
    """Load a binary program into memory"""
    try:
        with open(filename, 'rb') as f:
            program_data = f.read()
            # TRS-80 programs typically load at 0x5200
            start_address = 0x5200
            for i, byte in enumerate(program_data):
                memory.write(start_address + i, byte)
        return True
    except FileNotFoundError:
        print(f"Error: Program file '{filename}' not found")
        return False

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='TRS-80 Emulator')
    parser.add_argument('--program', type=str, help='Path to program file to load')
    args = parser.parse_args()

    # Initialize components
    cpu = CPU()
    memory = Memory()
    display = Display()
    keyboard = Keyboard()

    # Load program if specified
    if args.program:
        if not load_program(memory, args.program):
            return

    # Main emulation loop
    while True:
        # Get user input
        user_input = keyboard.get_input()
        
        # Process the input and execute instructions
        cpu.execute_instruction(user_input)
        
        # Update the display
        display.render()

if __name__ == "__main__":
    main()