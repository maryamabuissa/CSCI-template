
# a rectangle with width w, height h, made of the character c
def rectangle(w, h, c):
    # print a line (print c w times)
    l = line(w, c)
    # add "\n" to the end of the line
    l = l + "\n"
    # do that h times
    return l * h

def line(w, c):
    # print c w times
    return w * c


r = rectangle(2, 3, "y")
print(r)