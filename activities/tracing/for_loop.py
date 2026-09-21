# What does this print if I type "monument"?
# What does this print if I type "carrot"?

# Change this code to take a letter
# def has_letter(word, letter):
def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            print('This word has an "e"')
            # break

def main():
    word = input()
    has_e(word)

if __name__ == "__main__":
    main()