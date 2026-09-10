
def add(a, b):
    return a + b

def average(a, b):
    return add(a, b) / 2

if __name__ = "__main__":
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(average(a, b))
