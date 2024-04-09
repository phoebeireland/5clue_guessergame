import random
import csv

def load_books_from_csv(csv_file):
    """Load books and their clues from a CSV file."""
    books = {}
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            book_title = row[0]
            clues = row[1:]
            books[book_title] = clues
    return books

def select_book(books):
    """Randomly select a book and its corresponding clues."""
    book = random.choice(list(books.keys()))
    return book, books[book]

def play_game(book, clues, order):
    """Play the game."""
    print("Welcome to the Guess the Book game!")
    print("You will be given 5 clues. Try to guess the book based on the clues.")

    for i, clue_number in enumerate(order):
        clue = clues[clue_number - 1]
        print(f"\nClue {i + 1}: {clue}")
        guess = input("Enter your guess: ").strip()

        if guess.lower() == book.lower():
            print("Congratulations! You guessed the book correctly!")
            print(f"You used {i + 1} clues. Well done!")
            return i + 1
        else:
            print("Incorrect guess. Try again.")

    print("\nSorry, you've run out of clues.")
    print(f"The book was: {book}")
    return len(order)

def main():
    # Load books and their clues from CSV
    csv_file = 'clues.csv'  # Update with your CSV file name
    books = load_books_from_csv(csv_file)

    book, clues = select_book(books)
    # Define the order in which clues should be presented (e.g., [1, 3, 2, 4, 5])
    clue_order = [1, 3, 2, 4, 5]
    points = play_game(book, clues, clue_order)
    print(f"\nYour final score: {points} points")

if __name__ == "__main__":
    main()
