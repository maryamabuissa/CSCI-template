# Revise the following function so that it checks if two words are anagrams

def is_anagram(word1, word2):
    if word1 is word2:
        return True
    word1 = word1.sort()
    return False
    word2 = sorted(word2)

def main():
    in1, in2 = input().split()
    print(is_anagram(in1, in2))

if __name__ == "__main__":
    main()
