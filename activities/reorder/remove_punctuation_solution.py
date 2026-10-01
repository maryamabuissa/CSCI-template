# Edit this buggy code to remove all excessive non-letters from the end of a string

string = input()
# start at the end of the string
i = len(string) - 1
# count the number of excessive punctuation
while i >= 0:
    # check if the character isn't alphabetical
    if not string[i].isalpha():
        i = i - 1
    # stop when we hit a letter
    else:
        break

print(f"A better string would be {string[:i + 2]}")

