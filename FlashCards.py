class Flashcards:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return f"{self.word}: {self.meaning}"

flash = []
print("Welcome to the Flashcards program!")

while True:
    word = input("Enter a word (or type 'exit' to quit): ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(Flashcards(word, meaning))
    option = input("Do you want to add another flashcard? (yes/no): ")
    if option.lower() != 'yes':
        break
print("\nHere are your flashcards:")
for i in flash:
    print(">", i)