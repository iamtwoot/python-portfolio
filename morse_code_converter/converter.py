from data import MORSE_CODE, TEXT_CODE

class Converter:

    def __init__(self, strict=False):
        self.morse_code = MORSE_CODE
        self.text_code = TEXT_CODE
        self.strict = strict

    def encode(self, text: str) -> str:
        """Convert plain text to Morse code."""
        if self.strict:
            encoded = []
            for char in text:
                try:
                    encoded.append(self.morse_code[char.upper()])
                except KeyError:
                    raise ValueError(f"Unsupported character: '{char}'")
        else:
            encoded = [self.morse_code.get(char.upper(), char) for char in text]
        return " ".join(encoded)

    def decode(self, text: str) -> str:
        """Convert Morse code to plain text."""
        if self.strict:
            decoded = []
            for code in text.split():
                try:
                    decoded.append(self.text_code[code])
                except KeyError:
                    raise ValueError(f"Unsupported morse code: '{code}'")
        else:
            decoded = [self.text_code.get(code, code) for code in text.split()]
        return "".join(decoded)