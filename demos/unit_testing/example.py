
def add(a, b):
    sum = a + b
    return sum

def average(p, m):
    return (p + m) / 2

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    result = average(a, b)
    print(result)

if __name__ == "__main__":
    main()
