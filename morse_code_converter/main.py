from converter import Converter

converter = Converter(strict=True)

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
