from scripts import MorseCodeConverter

morse_code_converter = MorseCodeConverter()

morse_code_converter.greeting()
while morse_code_converter.is_on():
    response = input('Type "d" for decode and "e" for encode: ').lower()
    print('Please, enter the morse code separated with spaces.')
    input_text = input('Enter the text to be converted: ')

    if response == 'd':
        text = morse_code_converter.decode(input_text)
        print(text)
    elif response == 'e':
        text =  morse_code_converter.encode(input_text)
        print(text)
    else:
        print('Invalid input.')
