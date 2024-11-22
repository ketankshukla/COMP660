'''
Question 4

Explain what happens when the following recursive function is called with
the value “alucard” and 0 as arguments:

I have answered the above question in the markdown file and made this program interactive.

'''

def semordnilap(aString, index):
    if index < len(aString):
        semordnilap(aString, index + 1)
        print(aString[index], end="")

def main():
    while True:
        user_input = input("Enter a word to reverse (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Thank you for using the word reverser. Goodbye!")
            break

        if not user_input or not user_input.isalpha():
            print("Error: Please enter a non-empty word containing only letters.")
        else:
            print("Reversed word: ", end="")
            semordnilap(user_input, 0)
            print()  # New line after the reversed word

        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()