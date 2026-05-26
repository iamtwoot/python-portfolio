from data import MORSE_CODE, TEXT_CODE


class Converter:

    def __init__(self):
        self.morse_code = MORSE_CODE
        self.text_code = TEXT_CODE

    def encode(self, text: str) -> str:
        """Convert plain text to Morse code."""
        encoded = [self.morse_code.get(char.upper(), char) for char in text]
        return " ".join(encoded)

    def decode(self, text: str) -> str:
        """Convert Morse code to plain text."""
        decoded = [self.text_code.get(code, code) for code in text.split()]
        return "".join(decoded)


converter = Converter()

while True:
    choice = input("Type 'e' for encode or 'd' for decode: ").lower()

    if choice == 'e':
        user_input = input("Text to encode: ")
        print(converter.encode(user_input))

    elif choice == 'd':
        user_input = input("Text to decode: ")
        print(converter.decode(user_input))

    else:
        print("Invalid choice")
