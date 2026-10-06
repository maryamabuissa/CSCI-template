# What will this code print if I type:
# cat racecar palindrome madam Deified

def is_palindrome(word):
    return reversed(word) == list(word)

def main():
    word_list = input().split()
    for word in word_list:
        if len(word) >= 7 and is_palindrome(word):
            print(word)

if __name__ == "__main__":
    main()
