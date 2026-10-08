
def remove_last(lst):
    last_index = len(lst) - 1
    removed = lst.pop(last_index)
    return removed

def main():
    list_input = input().split()
    a = remove_last(list_input)
    list_input = [a] +  list_input
    b = remove_last(list_input)
    list_input = [b] +  list_input
    print(list_input)

if __name__ == "__main__":
    main()
