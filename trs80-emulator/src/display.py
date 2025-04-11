class Display:
    def __init__(self):
        self.screen = [[' ' for _ in range(64)] for _ in range(16)]  # 64x16 character display

    def render(self):
        for row in self.screen:
            print(''.join(row))

    def clear(self):
        self.screen = [[' ' for _ in range(64)] for _ in range(16)]  # Clear the display to blank spaces