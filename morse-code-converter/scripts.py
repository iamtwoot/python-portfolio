from data import morse_code, morse_code_reverse

class MorseCodeConverter:
    
    def encode(self, text: str) -> str:
        words = text.upper().split()
        encoded = []
        for word in words:
            encoded.append(' '.join(morse_code.get(ch, '?') for ch in word))
        return ' / '.join(encoded)

    def decode(self, text:str):
        morse_words = text.strip().split('/')
        print(morse_words)
        decoded = []
        for word in morse_words:
            letters = [morse_code_reverse.get(ch, '?') for ch in word.split()]
            decoded.append(''.join(letters))
        return ' '.join(decoded)

    def is_on(self):
        return input('Do you want to continue? (y/n): ').lower() == 'y'


    def greeting(self):
        print('Morse Code Converter')
        print('Made in 2025 by Twoot')

