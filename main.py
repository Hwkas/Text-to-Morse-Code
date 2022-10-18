#  Text to morse code conveter...


rosetta_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/", "!": "-.-.--", "@": ".--.-.",
    "&": ".-...", "(": "-.--.", ")": "-.--.-", "+": ".-.-.", "=": "-...-",
    ":": "---...", '"': ".-..-.", "'": ".----.", ",": "--..--", "/": "-..-.",
    "?": "..--..",
}


def text_to_morse(text):
    morse_code = ""

    for letter in text:
        try: 
            morse_code += rosetta_dict[letter.upper()]+" "
        except Exception as e:
            return (f"This symbol '{letter}' is not in the rosetta_dict.")

    return morse_code


text = input("Enter the Text you want to covert to Morse Code...\n")

print(text_to_morse(text))
