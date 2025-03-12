class Flashcard:
    def __init__(self, number, roman):
        self.number = number
        self.roman = roman

    def __str__(self):
        return f"{self.number} -> {self.roman}"

def integer_to_roman(num):
    num_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    result = ""
    for value, numeral in num_map:
        while num >= value:
            result += numeral
            num -= value
    return result

flashcards = []
print("Welcome to the Flashcard Application!")

while True:
    number = int(input("Enter a number: "))
    roman = integer_to_roman(number)
    flashcards.append(Flashcard(number, roman))
    
    if int(input("Enter 0 to add more or 1 to stop: ")):
        break

print("\nYour Flashcards:")
for card in flashcards:
    print(">", card)
