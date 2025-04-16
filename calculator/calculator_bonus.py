import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

MESSAGE_KEYS = {
    'WELCOME':              '1',
    'FIRST_NUMBER':         '2',
    'SECOND_NUMBER':        '3',
    'INVALID_NUMBER':       '4',
    'OPERATION':            '5',
    'CHOOSE':               '6',
    'ANOTHER_OPERATION':    '7',
    'YES_OR_NO':            '8',
    'RESULT':               '9',
    'CHOOSE_LANGUAGE':      '10',
    'TRY_AGAIN':            '11',
    'ZERO DIVISION':        '12',
}

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def get_number(prompt_key):
    while True:
        prompt(data[interface][prompt_key])
        number = input()
        if not invalid_number(number):
            return number
        prompt(data[interface][MESSAGE_KEYS['INVALID_NUMBER']])

def choose_language():
    language_map = {
        'en': 'english',
        'fr': 'french',
        'es': 'spanish',
        'de': 'german',
    }

    # Display language options
    prompt("Please choose your language: ")
    for lang in language_map.values():
        prompt(data[lang][MESSAGE_KEYS['CHOOSE_LANGUAGE']])

    while True:
        input_lang = input()
        if input_lang in language_map:
            return language_map[input_lang]

        # Handle invalid input
        prompt(data['english'][MESSAGE_KEYS['TRY_AGAIN']])
        for lang in language_map.values():
            prompt(data[lang][MESSAGE_KEYS['CHOOSE_LANGUAGE']])

interface = choose_language()

prompt(data[interface][MESSAGE_KEYS['WELCOME']])

while True:
    number1 = get_number(MESSAGE_KEYS['FIRST_NUMBER'])
    number2 = get_number(MESSAGE_KEYS['SECOND_NUMBER'])

    prompt(data[interface][MESSAGE_KEYS['OPERATION']])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data[interface][MESSAGE_KEYS['CHOOSE']])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            if float(number2) == 0:
                prompt(data[interface][MESSAGE_KEYS['ZERO DIVISION']])
                continue
            output = float(number1) / float(number2)

    if output.is_integer():
        prompt(data[interface][MESSAGE_KEYS['RESULT']] + f"{int(output)}")
    else:
        prompt(data[interface][MESSAGE_KEYS['RESULT']] + f"{output:.2f}")

    prompt(data[interface][MESSAGE_KEYS['ANOTHER_OPERATION']])
    answer = input()

    while answer not in ['y', 'n']:
        prompt(data[interface][MESSAGE_KEYS['YES_OR_NO']])
        answer = input()

    if answer == 'n':
        break
